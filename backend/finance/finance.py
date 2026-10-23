from decimal import Decimal

PERSONAL_ALLOWANCE = Decimal("12570")

# Income-taxable amounts after a full Personal Allowance.
UK_BANDS = [
    (Decimal("37700"), Decimal("0.20")),
    (Decimal("125140"), Decimal("0.40")),
    (None, Decimal("0.45")),
]

SCOTTISH_BANDS = {
    "2025-26": [
        (Decimal("2827"), Decimal("0.19")),
        (Decimal("14921"), Decimal("0.20")),
        (Decimal("31092"), Decimal("0.21")),
        (Decimal("62430"), Decimal("0.42")),
        (Decimal("112570"), Decimal("0.45")),
        (None, Decimal("0.48")),
    ],
    "2026-27": [
        (Decimal("3967"), Decimal("0.19")),
        (Decimal("16956"), Decimal("0.20")),
        (Decimal("31092"), Decimal("0.21")),
        (Decimal("62430"), Decimal("0.42")),
        (Decimal("112570"), Decimal("0.45")),
        (None, Decimal("0.48")),
    ],
}


def _tax_in_bands(taxable_income, bands):
    total = Decimal("0")
    lower = Decimal("0")
    for upper, rate in bands:
        if taxable_income <= lower:
            break
        taxable_top = taxable_income if upper is None else min(taxable_income, upper)
        total += max(Decimal("0"), taxable_top - lower) * rate
        if upper is None or taxable_income <= upper:
            break
        lower = upper
    return total


def estimate_uk_tax(gross_income, region, tax_year):
    """Estimate annual salary income tax and employee category-A Class 1 NI."""
    income = Decimal(str(gross_income))
    if income < 0:
        raise ValueError("Income must be zero or more.")
    if tax_year not in ("2025-26", "2026-27"):
        raise ValueError("Choose tax year 2025-26 or 2026-27.")
    if region not in ("england", "wales", "northern-ireland", "scotland"):
        raise ValueError("Choose a valid UK region.")

    personal_allowance = max(
        Decimal("0"), PERSONAL_ALLOWANCE - max(Decimal("0"), income - Decimal("100000")) / 2
    )
    taxable_income = max(Decimal("0"), income - personal_allowance)
    bands = SCOTTISH_BANDS[tax_year] if region == "scotland" else UK_BANDS
    income_tax = _tax_in_bands(taxable_income, bands)

    # Annualised estimate for a standard employee on NI category A.
    national_insurance = max(Decimal("0"), min(income, Decimal("50270")) - Decimal("12570")) * Decimal("0.08")
    national_insurance += max(Decimal("0"), income - Decimal("50270")) * Decimal("0.02")

    money = lambda value: value.quantize(Decimal("0.01"))
    return {
        "gross_income": money(income),
        "personal_allowance": money(personal_allowance),
        "taxable_income": money(taxable_income),
        "income_tax": money(income_tax),
        "national_insurance": money(national_insurance),
        "take_home": money(income - income_tax - national_insurance),
        "effective_tax_rate": money(income_tax / income * 100 if income else Decimal("0")),
    }
