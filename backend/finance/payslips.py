import re
from decimal import Decimal, InvalidOperation

from docx import Document
from docx.text.paragraph import Paragraph
from pypdf import PdfReader

MAX_PAYSLIP_SIZE = 5 * 1024 * 1024


def extract_payslip_text(upload):
    """Read a PDF/DOCX into memory only; never persist its contents."""
    if upload.size > MAX_PAYSLIP_SIZE:
        raise ValueError("Payslips must be 5 MB or smaller.")
    suffix = upload.name.lower().rsplit(".", 1)[-1] if "." in upload.name else ""
    upload.seek(0)
    if suffix == "pdf":
        reader = PdfReader(upload, strict=True)
        if reader.is_encrypted:
            raise ValueError("This PDF is password protected. Save an unprotected copy and try again.")
        if len(reader.pages) > 10:
            raise ValueError("Payslips must contain no more than 10 pages.")
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        if not text.strip():
            raise ValueError("No selectable text found. Scanned/image-only PDFs are not supported.")
        return text
    if suffix == "docx":
        document = Document(upload)
        parts = []
        for block in document.iter_inner_content():
            if isinstance(block, Paragraph):
                parts.append(block.text)
            else:
                parts.extend(cell.text for row in block.rows for cell in row.cells)
        text = "\n".join(parts)
        if not text.strip():
            raise ValueError("No readable text found in this DOCX document.")
        return text
    raise ValueError("Choose a PDF or Word DOCX payslip.")


def _find_money(text, label_pattern):
    match = re.search(
        rf"(?im)\b(?:{label_pattern})\b[^\r\n£0-9-]{{0,30}}(?:£\s*)?([0-9][0-9,]*(?:\.\d{{1,2}})?)",
        text,
    )
    if not match:
        return None
    try:
        return Decimal(match.group(1).replace(",", ""))
    except InvalidOperation:
        return None


def _find_labeled_tax(text):
    """Recognize common UK payslip tax labels, including table-separated values."""
    labels = r"income\s+tax|tax\s+deducted|tax(?!\s*(?:code|ytd|year[ -]?to[ -]?date))|paye(?:\s+tax)?"
    value = _find_money(text, labels)
    if value is not None:
        return value

    # Some PDF extractors put the label and amount on adjacent lines.
    match = re.search(
        rf"(?im)^\s*(?:{labels})\s*[:\-]?\s*\n\s*(?:£\s*)?([0-9][0-9,]*(?:\.\d{{1,2}})?)\s*$",
        text,
    )
    if not match:
        return None
    try:
        return Decimal(match.group(1).replace(",", ""))
    except InvalidOperation:
        return None


def review_payslip_text(text):
    """Return suggestions only; a user must verify each parsed payslip field."""
    code = re.search(r"(?i)\b(S?1257L|C1257L|BR|D0|D1|SD0|SD1|SD2|SD3|SBR|CBR|CD0|CD1)(?:\s*(W1|M1|X))?\b", text)
    return {
        "suggested_tax_code": "" if not code else "".join(part for part in code.groups() if part).upper(),
        "suggested_gross_pay": _find_money(text, r"gross\s*(?:pay|earnings)?|total\s*earnings|taxable\s*pay"),
        "suggested_tax_deducted": _find_labeled_tax(text),
    }
