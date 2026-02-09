from xero.models import BaseModel


class Invoice(BaseModel):
    openapi_types = {
        "type": "str",
        "contact": "Contact",
        "line_items": "list[LineItem]",
        "date": "date[ms-format]",
        "due_date": "date[ms-format]",
        "line_amount_types": "LineAmountTypes",
        "invoice_number": "str",
        "reference": "str",
        "branding_theme_id": "str",
        "url": "str",
        "currency_code": "CurrencyCode",
        "currency_rate": "float",
        "status": "str",
        "sent_to_contact": "bool",
        "expected_payment_date": "date[ms-format]",
        "planned_payment_date": "date[ms-format]",
        "cis_deduction": "float",
        "cis_rate": "float",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "total_discount": "float",
        "invoice_id": "str",
        "repeating_invoice_id": "str",
        "has_attachments": "bool",
        "is_discounted": "bool",
        "payments": "list[Payment]",
        "prepayments": "list[Prepayment]",
        "overpayments": "list[Overpayment]",
        "amount_due": "float",
        "amount_paid": "float",
        "fully_paid_on_date": "date[ms-format]",
        "amount_credited": "float",
        "updated_date_utc": "datetime[ms-format]",
        "credit_notes": "list[CreditNote]",
        "attachments": "list[Attachment]",
        "has_errors": "bool",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
        "warnings": "list[ValidationError]",
        "invoice_addresses": "list[InvoiceAddress]",
    }
    attribute_map = {
        "type": "Type",
        "contact": "Contact",
        "line_items": "LineItems",
        "date": "Date",
        "due_date": "DueDate",
        "line_amount_types": "LineAmountTypes",
        "invoice_number": "InvoiceNumber",
        "reference": "Reference",
        "branding_theme_id": "BrandingThemeID",
        "url": "Url",
        "currency_code": "CurrencyCode",
        "currency_rate": "CurrencyRate",
        "status": "Status",
        "sent_to_contact": "SentToContact",
        "expected_payment_date": "ExpectedPaymentDate",
        "planned_payment_date": "PlannedPaymentDate",
        "cis_deduction": "CISDeduction",
        "cis_rate": "CISRate",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "total_discount": "TotalDiscount",
        "invoice_id": "InvoiceID",
        "repeating_invoice_id": "RepeatingInvoiceID",
        "has_attachments": "HasAttachments",
        "is_discounted": "IsDiscounted",
        "payments": "Payments",
        "prepayments": "Prepayments",
        "overpayments": "Overpayments",
        "amount_due": "AmountDue",
        "amount_paid": "AmountPaid",
        "fully_paid_on_date": "FullyPaidOnDate",
        "amount_credited": "AmountCredited",
        "updated_date_utc": "UpdatedDateUTC",
        "credit_notes": "CreditNotes",
        "attachments": "Attachments",
        "has_errors": "HasErrors",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
        "warnings": "Warnings",
        "invoice_addresses": "InvoiceAddresses",
    }

    def __init__(
        self,
        type=None,
        contact=None,
        line_items=None,
        date=None,
        due_date=None,
        line_amount_types=None,
        invoice_number=None,
        reference=None,
        branding_theme_id=None,
        url=None,
        currency_code=None,
        currency_rate=None,
        status=None,
        sent_to_contact=None,
        expected_payment_date=None,
        planned_payment_date=None,
        cis_deduction=None,
        cis_rate=None,
        sub_total=None,
        total_tax=None,
        total=None,
        total_discount=None,
        invoice_id=None,
        repeating_invoice_id=None,
        has_attachments=False,
        is_discounted=None,
        payments=None,
        prepayments=None,
        overpayments=None,
        amount_due=None,
        amount_paid=None,
        fully_paid_on_date=None,
        amount_credited=None,
        updated_date_utc=None,
        credit_notes=None,
        attachments=None,
        has_errors=False,
        status_attribute_string=None,
        validation_errors=None,
        warnings=None,
        invoice_addresses=None,
    ):
        self._type = None
        self._contact = None
        self._line_items = None
        self._date = None
        self._due_date = None
        self._line_amount_types = None
        self._invoice_number = None
        self._reference = None
        self._branding_theme_id = None
        self._url = None
        self._currency_code = None
        self._currency_rate = None
        self._status = None
        self._sent_to_contact = None
        self._expected_payment_date = None
        self._planned_payment_date = None
        self._cis_deduction = None
        self._cis_rate = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._total_discount = None
        self._invoice_id = None
        self._repeating_invoice_id = None
        self._has_attachments = None
        self._is_discounted = None
        self._payments = None
        self._prepayments = None
        self._overpayments = None
        self._amount_due = None
        self._amount_paid = None
        self._fully_paid_on_date = None
        self._amount_credited = None
        self._updated_date_utc = None
        self._credit_notes = None
        self._attachments = None
        self._has_errors = None
        self._status_attribute_string = None
        self._validation_errors = None
        self._warnings = None
        self._invoice_addresses = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if contact is not None:
            self.contact = contact
        if line_items is not None:
            self.line_items = line_items
        if date is not None:
            self.date = date
        if due_date is not None:
            self.due_date = due_date
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if reference is not None:
            self.reference = reference
        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if url is not None:
            self.url = url
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if status is not None:
            self.status = status
        if sent_to_contact is not None:
            self.sent_to_contact = sent_to_contact
        if expected_payment_date is not None:
            self.expected_payment_date = expected_payment_date
        if planned_payment_date is not None:
            self.planned_payment_date = planned_payment_date
        if cis_deduction is not None:
            self.cis_deduction = cis_deduction
        if cis_rate is not None:
            self.cis_rate = cis_rate
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if total_discount is not None:
            self.total_discount = total_discount
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if repeating_invoice_id is not None:
            self.repeating_invoice_id = repeating_invoice_id
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if is_discounted is not None:
            self.is_discounted = is_discounted
        if payments is not None:
            self.payments = payments
        if prepayments is not None:
            self.prepayments = prepayments
        if overpayments is not None:
            self.overpayments = overpayments
        if amount_due is not None:
            self.amount_due = amount_due
        if amount_paid is not None:
            self.amount_paid = amount_paid
        if fully_paid_on_date is not None:
            self.fully_paid_on_date = fully_paid_on_date
        if amount_credited is not None:
            self.amount_credited = amount_credited
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if credit_notes is not None:
            self.credit_notes = credit_notes
        if attachments is not None:
            self.attachments = attachments
        if has_errors is not None:
            self.has_errors = has_errors
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if warnings is not None:
            self.warnings = warnings
        if invoice_addresses is not None:
            self.invoice_addresses = invoice_addresses

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_values = [
            "ACCPAY",
            "ACCPAYCREDIT",
            "APOVERPAYMENT",
            "APPREPAYMENT",
            "ACCREC",
            "ACCRECCREDIT",
            "AROVERPAYMENT",
            "ARPREPAYMENT",
            "None",
        ]
        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(
                        type, allowed_values
                    )
                )
        self._type = type

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def line_items(self):
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        self._line_items = line_items

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        self._due_date = due_date

    @property
    def line_amount_types(self):
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        self._line_amount_types = line_amount_types

    @property
    def invoice_number(self):
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        if invoice_number is not None and len(invoice_number) > 255:
            raise ValueError(
                "Invalid value for `invoice_number`, "
                "length must be less than or equal to `255`"
            )
        self._invoice_number = invoice_number

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def branding_theme_id(self):
        return self._branding_theme_id

    @branding_theme_id.setter
    def branding_theme_id(self, branding_theme_id):
        self._branding_theme_id = branding_theme_id

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        self._currency_code = currency_code

    @property
    def currency_rate(self):
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        self._currency_rate = currency_rate

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = [
            "DRAFT",
            "SUBMITTED",
            "DELETED",
            "AUTHORISED",
            "PAID",
            "VOIDED",
            "None",
        ]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def sent_to_contact(self):
        return self._sent_to_contact

    @sent_to_contact.setter
    def sent_to_contact(self, sent_to_contact):
        self._sent_to_contact = sent_to_contact

    @property
    def expected_payment_date(self):
        return self._expected_payment_date

    @expected_payment_date.setter
    def expected_payment_date(self, expected_payment_date):
        self._expected_payment_date = expected_payment_date

    @property
    def planned_payment_date(self):
        return self._planned_payment_date

    @planned_payment_date.setter
    def planned_payment_date(self, planned_payment_date):
        self._planned_payment_date = planned_payment_date

    @property
    def cis_deduction(self):
        return self._cis_deduction

    @cis_deduction.setter
    def cis_deduction(self, cis_deduction):
        self._cis_deduction = cis_deduction

    @property
    def cis_rate(self):
        return self._cis_rate

    @cis_rate.setter
    def cis_rate(self, cis_rate):
        self._cis_rate = cis_rate

    @property
    def sub_total(self):
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        self._sub_total = sub_total

    @property
    def total_tax(self):
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        self._total_tax = total_tax

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def total_discount(self):
        return self._total_discount

    @total_discount.setter
    def total_discount(self, total_discount):
        self._total_discount = total_discount

    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        self._invoice_id = invoice_id

    @property
    def repeating_invoice_id(self):
        return self._repeating_invoice_id

    @repeating_invoice_id.setter
    def repeating_invoice_id(self, repeating_invoice_id):
        self._repeating_invoice_id = repeating_invoice_id

    @property
    def has_attachments(self):
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        self._has_attachments = has_attachments

    @property
    def is_discounted(self):
        return self._is_discounted

    @is_discounted.setter
    def is_discounted(self, is_discounted):
        self._is_discounted = is_discounted

    @property
    def payments(self):
        return self._payments

    @payments.setter
    def payments(self, payments):
        self._payments = payments

    @property
    def prepayments(self):
        return self._prepayments

    @prepayments.setter
    def prepayments(self, prepayments):
        self._prepayments = prepayments

    @property
    def overpayments(self):
        return self._overpayments

    @overpayments.setter
    def overpayments(self, overpayments):
        self._overpayments = overpayments

    @property
    def amount_due(self):
        return self._amount_due

    @amount_due.setter
    def amount_due(self, amount_due):
        self._amount_due = amount_due

    @property
    def amount_paid(self):
        return self._amount_paid

    @amount_paid.setter
    def amount_paid(self, amount_paid):
        self._amount_paid = amount_paid

    @property
    def fully_paid_on_date(self):
        return self._fully_paid_on_date

    @fully_paid_on_date.setter
    def fully_paid_on_date(self, fully_paid_on_date):
        self._fully_paid_on_date = fully_paid_on_date

    @property
    def amount_credited(self):
        return self._amount_credited

    @amount_credited.setter
    def amount_credited(self, amount_credited):
        self._amount_credited = amount_credited

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def credit_notes(self):
        return self._credit_notes

    @credit_notes.setter
    def credit_notes(self, credit_notes):
        self._credit_notes = credit_notes

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        self._attachments = attachments

    @property
    def has_errors(self):
        return self._has_errors

    @has_errors.setter
    def has_errors(self, has_errors):
        self._has_errors = has_errors

    @property
    def status_attribute_string(self):
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors

    @property
    def warnings(self):
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        self._warnings = warnings

    @property
    def invoice_addresses(self):
        return self._invoice_addresses

    @invoice_addresses.setter
    def invoice_addresses(self, invoice_addresses):
        self._invoice_addresses = invoice_addresses
