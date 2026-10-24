from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import SavingsGoal, Transaction


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ("transaction_type", "amount", "date", "category", "description", "currency")
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}

    def clean_category(self):
        category = self.cleaned_data["category"].strip()
        if not category:
            raise forms.ValidationError("Enter a category, such as groceries, rent, loan or EMI.")
        return category


class SavingsGoalForm(forms.ModelForm):
    class Meta:
        model = SavingsGoal
        fields = ("name", "target_amount", "saved_amount", "target_date", "currency")
        widgets = {"target_date": forms.DateInput(attrs={"type": "date"})}


class TaxJobForm(forms.Form):
    JOB_TYPES = (("main", "Main job"), ("additional", "Additional job"))
    FREQUENCIES = (("monthly", "Monthly"), ("weekly", "Weekly"))
    CODES = (
        ("1257L", "1257L — standard allowance"), ("BR", "BR — basic rate"),
        ("D0", "D0 — higher rate"), ("D1", "D1 — additional rate"),
        ("S1257L", "S1257L — Scottish allowance"), ("SBR", "SBR — Scottish basic"),
        ("SD0", "SD0 — Scottish intermediate"), ("SD1", "SD1 — Scottish higher"),
        ("SD2", "SD2 — Scottish advanced"), ("SD3", "SD3 — Scottish top"),
        ("C1257L", "C1257L — Welsh allowance"), ("CBR", "CBR — Welsh basic"),
        ("CD0", "CD0 — Welsh higher"), ("CD1", "CD1 — Welsh additional"),
    )
    job_type = forms.ChoiceField(choices=JOB_TYPES, required=False)
    pay_frequency = forms.ChoiceField(choices=FREQUENCIES, required=False)
    pay_basis = forms.ChoiceField(choices=(("gross", "Gross pay this payday"), ("hourly", "Hourly rate and hours per week")), required=False)
    gross_pay = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2, required=False, label="Gross pay this payday (£)")
    hourly_rate = forms.DecimalField(min_value=0, max_digits=8, decimal_places=2, required=False, label="Hourly rate (£)")
    hours_per_week = forms.DecimalField(min_value=0, max_value=168, max_digits=6, decimal_places=2, required=False, label="Hours each week")
    tax_code = forms.ChoiceField(choices=CODES, required=False)
    taxable_pay_ytd = forms.DecimalField(min_value=0, max_digits=11, decimal_places=2, required=False, label="Taxable pay before this payday (£, optional)")
    tax_deducted_ytd = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2, required=False, label="Income Tax deducted before this payday (£, optional)")
    actual_tax_this_pay = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2, required=False, label="Income Tax on this payslip (£, optional)")

    def clean(self):
        cleaned = super().clean()
        if not any(cleaned.values()):
            return cleaned
        if not cleaned.get("job_type") or not cleaned.get("pay_frequency") or not cleaned.get("tax_code"):
            raise forms.ValidationError("Choose the job type, pay frequency and tax code.")
        rate, hours, gross = cleaned.get("hourly_rate"), cleaned.get("hours_per_week"), cleaned.get("gross_pay")
        basis = cleaned.get("pay_basis")
        if basis == "hourly" and (rate is None or hours is None):
            raise forms.ValidationError("For hourly pay, enter both the hourly rate and hours per week.")
        if basis == "gross" and gross is None:
            raise forms.ValidationError("Enter gross pay for this payday.")
        if (cleaned.get("taxable_pay_ytd") is None) != (cleaned.get("tax_deducted_ytd") is None):
            raise forms.ValidationError("For a year-to-date comparison, enter both taxable pay before this payday and tax deducted before it.")
        if cleaned.get("actual_tax_this_pay") is not None and cleaned.get("taxable_pay_ytd") is None:
            raise forms.ValidationError("Enter the year-to-date figures before comparing actual payslip tax.")
        return cleaned


class TaxForm(forms.Form):
    TAX_YEARS = (("2026-27", "2026/27"), ("2025-26", "2025/26"))
    REGIONS = (("england", "England"), ("wales", "Wales"), ("northern-ireland", "Northern Ireland"), ("scotland", "Scotland"))
    tax_year = forms.ChoiceField(choices=TAX_YEARS)
    region = forms.ChoiceField(choices=REGIONS)
    pay_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), label="Pay date")
    jobs_count = forms.ChoiceField(choices=((str(i), str(i)) for i in range(1, 5)), label="Number of jobs")

    def clean(self):
        cleaned = super().clean()
        pay_date, tax_year = cleaned.get("pay_date"), cleaned.get("tax_year")
        if pay_date and tax_year:
            year = int(tax_year[:4])
            if not date(year, 4, 6) <= pay_date <= date(year + 1, 4, 5):
                self.add_error("pay_date", "Pay date must fall within the selected UK tax year.")
        return cleaned
