# Pocketwise Personal Finance Tracker

A private, account-based web application to track expenses, income, savings goals and estimated UK salary take-home pay. Users enter information manually or import a CSV statement; there is no bank connection.

## Features

- User registration and sign-in with Django password hashing and session authentication.
- A monthly overview for income, expenses, and balance, plus recent activity and expense categories.
- Add, edit, delete, filter, search, and export your own transaction history. Loan repayments and EMIs can be recorded as expenses.
- Import up to 1,000 transactions from a CSV statement (2 MB maximum).
- Manual savings goals with progress tracking; these are not linked to bank accounts.
- UK PAYE estimates for up to four weekly or monthly jobs, including hourly-rate-to-gross conversion, separate tax codes such as 1257L/BR, estimated Income Tax, employee NI, net pay, and optional year-to-date comparison.
- Temporary, review-first text extraction from searchable PDF or DOCX payslips; uploaded payslips are not saved. Image-only/scanned PDFs are not OCRed. These pay estimates are indicative, not official payroll calculations.
- GBP, USD, EUR and INR transaction labels. Different currencies remain separate; no exchange rate is assumed.
- Financial records are scoped to the signed-in account.

## Run locally

Requires Python 3.12 or newer. From the repository root, open PowerShell:

```powershell
cd backend
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Store your database on D:\ (Windows)

The project workspace does not move automatically onto your computer's D: drive. The SQLite database can be configured to live there while the application code is wherever you keep the project:

```powershell
New-Item -ItemType Directory -Force D:\PersonalFinance
$env:FINANCE_DB_PATH = 'D:\PersonalFinance\data.sqlite3'
```

Set `FINANCE_DB_PATH` before running Django in each new PowerShell session. For a persistent setting, configure it in Windows Environment Variables. The setting is optional; without it the database is `backend/db.sqlite3`.

For a non-production local development secret, Django supplies a local fallback. For persistent or hosted use, set a private secret and optional host list in the environment. See [backend/.env.example](backend/.env.example) for variable names and the D: path example; the app does not load `.env` files automatically.

Continue in the activated `backend` directory:

```powershell
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

Open <http://127.0.0.1:8000/> and create an account. Registration is open in this initial version. Use a production-grade secret, `DJANGO_DEBUG=False`, a restricted host list, HTTPS and a production database before deployment.

## CSV statement format

Upload `.csv` files with the following header row and ISO dates. Required columns: `date`, `type`, `amount`, `category`. Optional columns: `description`, `currency` (defaults to GBP).

```csv
date,type,amount,category,description,currency
2026-04-06,expense,42.50,Groceries,Weekly shop,GBP
2026-04-30,expense,320.00,Loan,Car EMI,GBP
2026-04-30,income,2500.00,Salary,Monthly pay,GBP
```

Rows are validated before any are saved. Supported currencies are GBP, USD, EUR and INR. CSV only; PDF and image statement import is not included. Review imported rows in transaction history. Export downloads the signed-in user's original amounts and currencies.

## PAYE planner scope and payslip privacy

The PAYE planner estimates each job separately. It starts with 1257L for the main job and BR for additional jobs as suggestions, but you can select other listed codes. Confirm the exact code (including any S/C prefix or W1/M1 basis) on your HMRC notice/payslip. If you enter taxable pay earlier this tax year and Income Tax deducted before this payday, the planner estimates an illustrative cumulative deduction; entering the payslip tax as well compares actual to estimated tax-to-date. It does not reproduce HMRC payroll tables, tax-code notices or payroll rounding. NI is an indicative category-A employee estimate. Pension, student-loan, benefits, other deductions, irregular pay and HMRC adjustments may change actual net pay. For official results, check [HMRC's Income Tax estimator](https://www.gov.uk/estimate-income-tax) or [PAYE calculator](https://www.gov.uk/guidance/work-out-an-employees-income-tax).

Payslip uploads accept PDF and Word DOCX up to 5 MB (10 PDF pages maximum). The uploaded file and extracted text are used in memory for that request and are not stored in the application database. Extraction only suggests a tax code, gross pay and tax amount; it does not fill or submit the calculator automatically, and the user must verify all values. Scanned/image-only PDFs are not OCRed, and encrypted PDFs are rejected. Sources: [HMRC tax codes](https://www.gov.uk/tax-codes/what-your-tax-code-means), [HMRC multi-job guidance](https://www.gov.uk/guidance/how-tax-works-if-you-have-more-than-one-job), and [HMRC rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027).

## Checks

```powershell
python manage.py test finance
python manage.py check
```
