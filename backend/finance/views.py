import csv
import io
from datetime import date
from decimal import Decimal, InvalidOperation

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django import forms
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegistrationForm, SavingsGoalForm, TaxForm, TaxJobForm, TransactionForm
from .models import SavingsGoal, Transaction
from .payroll import estimate_job_payroll, gross_for_period
from .payslips import extract_payslip_text, review_payslip_text


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
    initial = {"tax_year": "2026-27", "region": "england", "pay_date": date.today(), "jobs_count": "1"}
    form = TaxForm(request.POST or None, initial=initial)
    job_factory = forms.formset_factory(TaxJobForm, extra=4, max_num=4, validate_max=True)
    posted_calculation = request.method == "POST" and "calculate" in request.POST
    job_data = request.POST if posted_calculation else None
    if posted_calculation and request.POST.get("jobs_count"):
        job_data = request.POST.copy()
        count = int(request.POST["jobs_count"])
        job_data["job-TOTAL_FORMS"] = str(count)
        job_data["job-MAX_NUM_FORMS"] = str(count)
    jobs = job_factory(job_data, prefix="job")
    for index, job_form in enumerate(jobs.forms):
        job_form.fields["job_type"].initial = "main" if index == 0 else "additional"
        job_form.fields["pay_frequency"].initial = "monthly"
        job_form.fields["pay_basis"].initial = "hourly"
        job_form.fields["tax_code"].initial = "1257L" if index == 0 else "BR"

    estimates = []
    totals = None
    payslip_review = None
    if request.method == "POST" and "payslip" in request.FILES:
        upload = request.FILES["payslip"]
        try:
            if not upload.name.lower().endswith((".pdf", ".docx")):
                raise ValueError("Choose a PDF or Word DOCX payslip.")
            text = extract_payslip_text(upload)
            payslip_review = review_payslip_text(text)
            payslip_review["file_name"] = upload.name
            if not any(value is not None and value != "" for value in payslip_review.values()):
                payslip_review["message"] = "Readable text was found, but no common pay fields were recognised. Enter the details manually."
        except Exception:
            form.add_error(None, "This file could not be read as a supported payslip. Try an unprotected PDF with selectable text or a valid DOCX.")
        except (ValueError, OSError, KeyError) as error:
            form.add_error(None, str(error))
    elif posted_calculation and form.is_valid():
        if jobs.is_valid():
            for index, job_form in enumerate(jobs.forms):
                data = job_form.cleaned_data
                if not data:
                    continue
                frequency = data["pay_frequency"]
                gross = gross_for_period(
                    pay_basis=data["pay_basis"],
                    gross_pay=data.get("gross_pay") or Decimal("0"),
                    hourly_rate=data.get("hourly_rate") or Decimal("0"),
                    hours_per_week=data.get("hours_per_week") or Decimal("0"),
                    frequency=frequency,
                )
                try:
                    estimate = estimate_job_payroll(
                        gross_pay=gross,
                        frequency=frequency,
                        tax_code=data["tax_code"],
                        region=form.cleaned_data["region"],
                        tax_year=form.cleaned_data["tax_year"],
                        pay_date=form.cleaned_data["pay_date"],
                        taxable_pay_ytd=data.get("taxable_pay_ytd"),
                        tax_deducted_before_payday=data.get("tax_deducted_ytd"),
                        actual_tax_this_pay=data.get("actual_tax_this_pay"),
                    )
                except ValueError as error:
                    job_form.add_error("tax_code", str(error))
                    continue
                estimate.update({"job_type": data["job_type"], "frequency": frequency, "tax_code": data["tax_code"]})
                estimates.append(estimate)
        else:
            form.add_error(None, "Check the job details, including the pay basis and year-to-date values.")
        if estimates:
            totals = {
                "gross": sum((item["gross_pay"] for item in estimates), Decimal("0")),
                "tax": sum((item["income_tax"] for item in estimates), Decimal("0")),
                "ni": sum((item["national_insurance"] for item in estimates), Decimal("0")),
                "net": sum((item["net_pay"] for item in estimates), Decimal("0")),
            }
    return render(request, "finance/tax.html", {"form": form, "jobs": jobs, "estimates": estimates, "totals": totals, "payslip_review": payslip_review})


@login_required
def export_transactions(request):
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = 'attachment; filename="transactions.csv"'
    writer = csv.writer(response)
    writer.writerow(("date", "type", "amount", "currency", "category", "description"))
    for transaction in Transaction.objects.filter(user=request.user):
        writer.writerow((transaction.date, transaction.transaction_type, transaction.amount, transaction.currency, transaction.category, transaction.description))
    return response
