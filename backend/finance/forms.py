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


class TaxForm(forms.Form):
    TAX_YEARS = (("2026-27", "2026/27"), ("2025-26", "2025/26"))
    REGIONS = (
        ("england", "England"),
        ("wales", "Wales"),
        ("northern-ireland", "Northern Ireland"),
        ("scotland", "Scotland"),
    )
    gross_income = forms.DecimalField(min_value=0, max_digits=12, decimal_places=2, label="Annual gross salary (£)")
    tax_year = forms.ChoiceField(choices=TAX_YEARS)
    region = forms.ChoiceField(choices=REGIONS)
