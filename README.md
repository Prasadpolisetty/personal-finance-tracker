# Pocketwise Personal Finance Tracker

A private, account-based web application to track expenses, income, savings goals and estimated UK salary take-home pay. Users enter information manually or import a CSV statement; there is no bank connection.

## Features

- User registration and sign-in with Django password hashing and session authentication.
- A monthly overview for income, expenses, and balance, plus recent activity and expense categories.
- Add, edit, delete, filter, search, and export your own transaction history. Loan repayments and EMIs can be recorded as expenses.
- Import up to 1,000 transactions from a CSV statement (2 MB maximum).
- Manual savings goals with progress tracking; these are not linked to bank accounts.
- UK annual salary Income Tax and employee Class 1 NI estimates for 2025/26 and 2026/27, with England, Wales, Northern Ireland and Scotland options.
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

## Tax estimate scope

The calculator provides an indicative annual estimate based on standard Personal Allowance and taper, the selected nation's salary income-tax bands, and annualised employee Class 1 category A NI. It does not calculate pension relief, student loans, benefits, tax codes, self-employment, dividends, savings income, employer NI, pay-period rounding, or other NI categories. Actual payroll deductions may differ. The calculator is for personal planning, not tax advice. Sources: [GOV.UK Income Tax rates](https://www.gov.uk/income-tax-rates), [Scottish Income Tax](https://www.gov.uk/scottish-income-tax), and [National Insurance rates](https://www.gov.uk/national-insurance/how-much-you-pay).

## Checks

```powershell
python manage.py test finance
python manage.py check
```
