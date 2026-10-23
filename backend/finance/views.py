import csv
import io
from datetime import date
from decimal import Decimal, InvalidOperation

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .finance import estimate_uk_tax
from .forms import RegistrationForm, SavingsGoalForm, TaxForm, TransactionForm
from .models import SavingsGoal, Transaction


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("dashboard")
    return render(request, "finance/register.html", {"form": form})


@login_required
def dashboard(request):
    today = date.today()
    transactions = Transaction.objects.filter(user=request.user)
    period = request.GET.get("period", today.strftime("%Y-%m"))
    try:
        year, month = (int(part) for part in period.split("-"))
        if not (1 <= month <= 12 and 2000 <= year <= 2100):
            raise ValueError
        selected = transactions.filter(date__year=year, date__month=month)
    except (ValueError, TypeError):
        period = today.strftime("%Y-%m")
        selected = transactions.filter(date__year=today.year, date__month=today.month)

    def total(kind):
        return selected.filter(transaction_type=kind).aggregate(total=Sum("amount"))["total"] or Decimal("0")

    category_totals = (
        selected.filter(transaction_type=Transaction.EXPENSE)
        .values("category", "currency")
        .annotate(total=Sum("amount"))
        .order_by("-total")[:6]
    )
    return render(request, "finance/dashboard.html", {
        "period": period,
        "income": total(Transaction.INCOME),
        "expenses": total(Transaction.EXPENSE),
        "balance": total(Transaction.INCOME) - total(Transaction.EXPENSE),
        "transactions": transactions[:10],
        "category_totals": category_totals,
        "goals": SavingsGoal.objects.filter(user=request.user),
        "transaction_count": transactions.count(),
    })


@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    query = request.GET.get("q", "").strip()
    kind = request.GET.get("type", "")
    if query:
        transactions = transactions.filter(category__icontains=query) | transactions.filter(description__icontains=query)
    if kind in (Transaction.INCOME, Transaction.EXPENSE):
        transactions = transactions.filter(transaction_type=kind)
    return render(request, "finance/transactions.html", {"transactions": transactions, "query": query, "kind": kind})


@login_required
def transaction_create(request):
    form = TransactionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        transaction = form.save(commit=False)
        transaction.user = request.user
        transaction.save()
        messages.success(request, "Transaction saved.")
        return redirect("transactions")
    return render(request, "finance/form.html", {"form": form, "title": "Add transaction"})


@login_required
def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    form = TransactionForm(request.POST or None, instance=transaction)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Transaction updated.")
        return redirect("transactions")
    return render(request, "finance/form.html", {"form": form, "title": "Edit transaction"})


@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == "POST":
        transaction.delete()
        messages.success(request, "Transaction deleted.")
    return redirect("transactions")


@login_required
def savings_list(request):
    return render(request, "finance/savings.html", {"goals": SavingsGoal.objects.filter(user=request.user)})


@login_required
def savings_create(request):
    form = SavingsGoalForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        goal = form.save(commit=False)
        goal.user = request.user
        goal.save()
        messages.success(request, "Savings goal saved.")
        return redirect("savings")
    return render(request, "finance/form.html", {"form": form, "title": "Add savings goal"})


@login_required
def savings_edit(request, pk):
    goal = get_object_or_404(SavingsGoal, pk=pk, user=request.user)
    form = SavingsGoalForm(request.POST or None, instance=goal)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Savings goal updated.")
        return redirect("savings")
    return render(request, "finance/form.html", {"form": form, "title": "Update savings goal"})


@login_required
def savings_delete(request, pk):
    goal = get_object_or_404(SavingsGoal, pk=pk, user=request.user)
    if request.method == "POST":
        goal.delete()
        messages.success(request, "Savings goal deleted.")
    return redirect("savings")


@login_required
def upload_statement(request):
    if request.method == "POST":
        statement = request.FILES.get("statement")
        if not statement or not statement.name.lower().endswith(".csv"):
            messages.error(request, "Choose a CSV statement file.")
            return redirect("upload")
        if statement.size > 2 * 1024 * 1024:
            messages.error(request, "Statement must be smaller than 2 MB.")
            return redirect("upload")
        try:
            text = statement.read().decode("utf-8-sig")
            reader = csv.DictReader(io.StringIO(text))
            headers = {header.strip().lower() for header in (reader.fieldnames or [])}
            if not {"date", "amount", "category"}.issubset(headers):
                raise ValueError("CSV headers must include date, amount, category, and type.")
            if "type" not in headers:
                raise ValueError("CSV headers must include date, amount, category, and type.")
            imported = []
            for row in reader:
                normalized = {key.strip().lower(): (value or "").strip() for key, value in row.items() if key}
                kind = normalized["type"].lower()
                currency = normalized.get("currency", "GBP").upper()
                if currency not in dict(Transaction.COMMON_CURRENCIES):
                    raise ValueError("Use a supported currency: GBP, USD, EUR or INR.")
                row_form = TransactionForm(data={
                    "transaction_type": kind,
                    "amount": normalized["amount"].replace(",", "").replace("£", ""),
                    "date": normalized["date"],
                    "category": normalized["category"][:80],
                    "description": normalized.get("description", "")[:240],
                    "currency": currency,
                })
                if not row_form.is_valid():
                    raise ValueError(f"Invalid row: {row_form.errors.as_text()}")
                transaction = row_form.save(commit=False)
                transaction.user = request.user
                imported.append(transaction)
            if not imported:
                raise ValueError("The CSV file contains no transaction rows.")
            if len(imported) > 1000:
                raise ValueError("Upload no more than 1,000 transactions at a time.")
            Transaction.objects.bulk_create(imported)
            messages.success(request, f"Imported {len(imported)} transactions. Review them in transaction history.")
            return redirect("transactions")
        except (UnicodeDecodeError, csv.Error, KeyError, TypeError, ValueError, InvalidOperation) as error:
            messages.error(request, f"Statement not imported: {error}")
    return render(request, "finance/upload.html")


@login_required
def tax_calculator(request):
    form = TaxForm(request.POST or None, initial={"tax_year": "2026-27", "region": "england"})
    estimate = None
    if request.method == "POST" and form.is_valid():
        estimate = estimate_uk_tax(form.cleaned_data["gross_income"], form.cleaned_data["region"], form.cleaned_data["tax_year"])
        estimate["tax_year"] = form.cleaned_data["tax_year"]
        estimate["region"] = form.cleaned_data["region"].replace("-", " ").title()
    return render(request, "finance/tax.html", {"form": form, "estimate": estimate})


@login_required
def export_transactions(request):
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = 'attachment; filename="transactions.csv"'
    writer = csv.writer(response)
    writer.writerow(("date", "type", "amount", "currency", "category", "description"))
    for transaction in Transaction.objects.filter(user=request.user):
        writer.writerow((transaction.date, transaction.transaction_type, transaction.amount, transaction.currency, transaction.category, transaction.description))
    return response
