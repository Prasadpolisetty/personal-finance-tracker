from datetime import date
from decimal import Decimal

from .finance import PERSONAL_ALLOWANCE, SCOTTISH_BANDS

ZERO = Decimal("0")
NI_PRIMARY_THRESHOLDS = {"weekly": Decimal("242"), "monthly": Decimal("1048")}
NI_UPPER_LIMITS = {"weekly": Decimal("967"), "monthly": Decimal("4189")}
PERIODS_PER_YEAR = {"weekly": Decimal("52"), "monthly": Decimal("12")}


def gross_for_period(*, pay_basis, gross_pay, hourly_rate, hours_per_week, frequency):
    if pay_basis == "gross":
        return gross_pay
    weekly = hourly_rate * hours_per_week
    return weekly if frequency == "weekly" else weekly * Decimal("52") / Decimal("12")


def periods_elapsed(pay_date, tax_year, frequency):
    year = int(tax_year[:4])
    start = date(year, 4, 6)
    if not start <= pay_date <= date(year + 1, 4, 5):
        raise ValueError("Pay date must fall within the selected UK tax year.")
    if frequency == "monthly":
        return (pay_date.year - year) * 12 + pay_date.month - 4 - int(pay_date.day < 6) + 1
    return min(52, ((pay_date - start).days // 7) + 1)


def _fixed_rate(code):
    return {
        "BR": Decimal("0.20"), "CBR": Decimal("0.20"), "SBR": Decimal("0.20"),
        "D0": Decimal("0.40"), "CD0": Decimal("0.40"), "D1": Decimal("0.45"), "CD1": Decimal("0.45"),
        "SD0": Decimal("0.21"), "SD1": Decimal("0.42"), "SD2": Decimal("0.45"), "SD3": Decimal("0.48"),
    }.get(code)


def _progressive_tax(taxable, bands):
    total = ZERO
    lower = ZERO
    for upper, rate in bands:
        if taxable <= lower:
            break
        top = taxable if upper is None else min(taxable, upper)
        total += max(ZERO, top - lower) * rate
        if upper is None or taxable <= upper:
            break
        lower = upper
    return total


def _cumulative_target(pay_to_date, periods, frequency, tax_code, region, tax_year):
    code = tax_code.upper().replace(" ", "")
    base = code.removesuffix("W1").removesuffix("M1").removesuffix("X")
    factor = Decimal(periods)
    allowance = NI_PRIMARY_THRESHOLDS[frequency] * factor if base.endswith("1257L") else ZERO
    taxable = max(ZERO, pay_to_date - allowance)
    fixed = _fixed_rate(base)
    if fixed is not None:
        return taxable * fixed
    if not base.endswith("1257L"):
        raise ValueError("Choose a supported 1257L, BR, D0, D1 or regional tax code.")

    if base.startswith("S") or region == "scotland":
        annual_bands = [
            (None if upper is None else max(ZERO, upper - PERSONAL_ALLOWANCE), rate)
            for upper, rate in SCOTTISH_BANDS[tax_year]
        ]
    else:
        annual_bands = [
            (Decimal("37700"), Decimal("0.20")),
            (Decimal("112570"), Decimal("0.40")),
            (None, Decimal("0.45")),
        ]
    period_bands = [(None if upper is None else upper * factor, rate) for upper, rate in annual_bands]
    return _progressive_tax(taxable, period_bands)


def estimate_job_payroll(
    *, gross_pay, frequency, tax_code, region, tax_year, pay_date,
    taxable_pay_ytd=None, tax_deducted_before_payday=None, actual_tax_this_pay=None,
):
    """Estimate a job's payday tax and NI; it is not an HMRC payroll-table calculation."""
    if frequency not in PERIODS_PER_YEAR:
        raise ValueError("Pay frequency must be weekly or monthly.")
    periods = periods_elapsed(pay_date, tax_year, frequency)
    code = tax_code.upper().replace(" ", "")
    period_only = code.endswith(("W1", "M1", "X"))
    if (code.endswith("W1") and frequency != "weekly") or (code.endswith("M1") and frequency != "monthly"):
        raise ValueError("W1 must be weekly and M1 must be monthly.")
    if code.startswith("S"):
        region = "scotland"
    elif code.startswith("C"):
        region = "wales"

    if period_only:
        target = _cumulative_target(gross_pay, 1, frequency, tax_code, region, tax_year)
        income_tax = target
        ytd_difference = None
    elif taxable_pay_ytd is not None and tax_deducted_before_payday is not None:
        prior_periods = max(0, periods - 1)
        prior_target = _cumulative_target(taxable_pay_ytd, prior_periods, frequency, tax_code, region, tax_year) if prior_periods else ZERO
        target = _cumulative_target(taxable_pay_ytd + gross_pay, periods, frequency, tax_code, region, tax_year)
        income_tax = target - tax_deducted_before_payday
        ytd_difference = (
            tax_deducted_before_payday + actual_tax_this_pay - target
            if actual_tax_this_pay is not None
            else tax_deducted_before_payday - prior_target
        )
    else:
        target = _cumulative_target(gross_pay, 1, frequency, tax_code, region, tax_year)
        income_tax = target
        ytd_difference = None

    threshold = NI_PRIMARY_THRESHOLDS[frequency]
    upper = NI_UPPER_LIMITS[frequency]
    national_insurance = max(ZERO, min(gross_pay, upper) - threshold) * Decimal("0.08")
    national_insurance += max(ZERO, gross_pay - upper) * Decimal("0.02")
    money = lambda value: value.quantize(Decimal("0.01"))
    return {
        "gross_pay": money(gross_pay),
        "income_tax": money(income_tax),
        "national_insurance": money(national_insurance),
        "net_pay": money(gross_pay - income_tax - national_insurance),
        "estimated_tax_to_date": money(target),
        "ytd_difference": None if ytd_difference is None else money(ytd_difference),
        "actual_tax_this_pay": actual_tax_this_pay,
        "periods_elapsed": periods,
        "period_only": period_only,
        "ytd_compares_before_payday": taxable_pay_ytd is not None,
    }
