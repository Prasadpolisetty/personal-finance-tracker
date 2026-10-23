from django.contrib import admin

from .models import SavingsGoal, Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("date", "user", "transaction_type", "amount", "currency", "category")
    list_filter = ("transaction_type", "currency", "date")
    search_fields = ("user__username", "category", "description")


@admin.register(SavingsGoal)
class SavingsGoalAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "saved_amount", "target_amount", "currency")
    search_fields = ("user__username", "name")
