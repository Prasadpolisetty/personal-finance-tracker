from datetime import date
from decimal import Decimal
import io

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .finance import estimate_uk_tax
from .models import SavingsGoal, Transaction


class TaxEstimateTests(TestCase):
    def test_basic_rate_employee_estimate(self):
        result = estimate_uk_tax("30000", "england", "2026-27")
        self.assertEqual(result["personal_allowance"], Decimal("12570.00"))
        self.assertEqual(result["income_tax"], Decimal("3486.00"))
        self.assertEqual(result["national_insurance"], Decimal("1394.40"))
        self.assertEqual(result["take_home"], Decimal("25119.60"))

    def test_personal_allowance_taper_and_additional_rate(self):
        result = estimate_uk_tax("150000", "england", "2025-26")
        self.assertEqual(result["personal_allowance"], Decimal("0.00"))
        self.assertEqual(result["income_tax"], Decimal("53703.00"))
        self.assertEqual(result["national_insurance"], Decimal("5010.60"))

    def test_taxable_band_thresholds_remain_income_based_during_allowance_taper(self):
        result = estimate_uk_tax("110000", "england", "2026-27")
        self.assertEqual(result["personal_allowance"], Decimal("7570.00"))
        self.assertEqual(result["taxable_income"], Decimal("102430.00"))
        self.assertEqual(result["income_tax"], Decimal("33432.00"))

    def test_scottish_tax_bands_change_by_year(self):
        older = estimate_uk_tax("30000", "scotland", "2025-26")
        newer = estimate_uk_tax("30000", "scotland", "2026-27")
        self.assertEqual(older["income_tax"], Decimal("3482.82"))
        self.assertEqual(newer["income_tax"], Decimal("3451.07"))

    def test_invalid_inputs_are_rejected(self):
        for args in ((-1, "england", "2026-27"), (100, "england", "2024-25"), (100, "ireland", "2026-27")):
            with self.subTest(args=args), self.assertRaises(ValueError):
                estimate_uk_tax(*args)


class FinanceViewsTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username="alice", password="CorrectHorse123!")
        self.bob = User.objects.create_user(username="bob", password="CorrectHorse123!")
        self.transaction = Transaction.objects.create(
            user=self.alice, transaction_type=Transaction.EXPENSE,
            amount=Decimal("25.50"), date=date(2026, 5, 3), category="Groceries",
        )

    def test_finance_pages_require_login(self):
        for name in ("dashboard", "transactions", "savings", "tax", "upload"):
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 302)
            self.assertIn(reverse("login"), response["Location"])

    def test_dashboard_and_history_are_scoped_to_signed_in_user(self):
        self.client.force_login(self.bob)
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["transaction_count"], 0)
        self.assertNotContains(response, "Groceries")
        response = self.client.get(reverse("transactions"))
        self.assertNotContains(response, "Groceries")

    def test_user_cannot_edit_or_delete_another_users_transaction(self):
        self.client.force_login(self.bob)
        self.assertEqual(self.client.get(reverse("transaction_edit", args=[self.transaction.pk])).status_code, 404)
        self.assertEqual(self.client.post(reverse("transaction_delete", args=[self.transaction.pk])).status_code, 404)
        self.assertTrue(Transaction.objects.filter(pk=self.transaction.pk).exists())

    def test_create_transaction_is_owned_by_current_user(self):
        self.client.force_login(self.alice)
        response = self.client.post(reverse("transaction_create"), {
            "transaction_type": "expense", "amount": "42.50", "date": "2026-06-01",
            "category": "Loan payment", "description": "Monthly EMI", "currency": "GBP",
        })
        self.assertRedirects(response, reverse("transactions"))
        saved = Transaction.objects.get(description="Monthly EMI")
        self.assertEqual(saved.user, self.alice)

    def test_csv_upload_saves_valid_rows_to_current_user(self):
        self.client.force_login(self.alice)
        file = SimpleUploadedFile(
            "statement.csv",
            b"date,type,amount,category,description,currency\n2026-06-02,expense,320,Loan,Car EMI,GBP\n",
            content_type="text/csv",
        )
        response = self.client.post(reverse("upload"), {"statement": file})
        self.assertRedirects(response, reverse("transactions"))
        self.assertTrue(Transaction.objects.filter(user=self.alice, description="Car EMI", amount="320.00").exists())

    def test_invalid_csv_does_not_import_any_rows(self):
        self.client.force_login(self.alice)
        file = SimpleUploadedFile(
            "statement.csv",
            b"date,type,amount,category\n2026-06-02,expense,-12,Loan\n",
            content_type="text/csv",
        )
        self.client.post(reverse("upload"), {"statement": file})
        self.assertEqual(Transaction.objects.filter(user=self.alice).count(), 1)

    def test_savings_goals_are_user_scoped(self):
        goal = SavingsGoal.objects.create(user=self.alice, name="Emergency fund", target_amount=1000)
        self.client.force_login(self.bob)
        self.assertEqual(self.client.get(reverse("savings_edit", args=[goal.pk])).status_code, 404)
        response = self.client.get(reverse("savings"))
        self.assertNotContains(response, "Emergency fund")
