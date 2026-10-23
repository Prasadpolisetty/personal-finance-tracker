from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Transaction(models.Model):
    INCOME = "income"
    EXPENSE = "expense"
    TYPE_CHOICES = [(INCOME, "Income"), (EXPENSE, "Expense")]
    COMMON_CURRENCIES = [(code, code) for code in ("GBP", "USD", "EUR", "INR")]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=8, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    date = models.DateField()
    category = models.CharField(max_length=80)
    description = models.CharField(max_length=240, blank=True)
    currency = models.CharField(max_length=3, choices=COMMON_CURRENCIES, default="GBP")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.transaction_type}: {self.currency} {self.amount}"


class SavingsGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="savings_goals")
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    saved_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    target_date = models.DateField(null=True, blank=True)
    currency = models.CharField(max_length=3, choices=Transaction.COMMON_CURRENCIES, default="GBP")

    class Meta:
        ordering = ["name"]

    @property
    def progress(self):
        if not self.target_amount:
            return 0
        return min(100, int(self.saved_amount / self.target_amount * 100))

    def __str__(self):
        return self.name
