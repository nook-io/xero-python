from xero.models import BaseModel


class Prepayment(BaseModel):
    openapi_types = {
        "type": "str",
        "contact": "Contact",
        "date": "date[ms-format]",
        "status": "str",
        "line_amount_types": "LineAmountTypes",
        "line_items": "list[LineItem]",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "reference": "str",
        "updated_date_utc": "datetime[ms-format]",
        "currency_code": "CurrencyCode",
        "prepayment_id": "str",
        "currency_rate": "float",
        "remaining_credit": "float",
        "allocations": "list[Allocation]",
        "payments": "list[Payment]",
        "applied_amount": "float",
        "has_attachments": "bool",
        "attachments": "list[Attachment]",
    }
    attribute_map = {
        "type": "Type",
        "contact": "Contact",
        "date": "Date",
        "status": "Status",
        "line_amount_types": "LineAmountTypes",
        "line_items": "LineItems",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "reference": "Reference",
        "updated_date_utc": "UpdatedDateUTC",
        "currency_code": "CurrencyCode",
        "prepayment_id": "PrepaymentID",
        "currency_rate": "CurrencyRate",
        "remaining_credit": "RemainingCredit",
        "allocations": "Allocations",
        "payments": "Payments",
        "applied_amount": "AppliedAmount",
        "has_attachments": "HasAttachments",
        "attachments": "Attachments",
    }

    def __init__(
        self,
        type=None,
        contact=None,
        date=None,
        status=None,
        line_amount_types=None,
        line_items=None,
        sub_total=None,
        total_tax=None,
        total=None,
        reference=None,
        updated_date_utc=None,
        currency_code=None,
        prepayment_id=None,
        currency_rate=None,
        remaining_credit=None,
        allocations=None,
        payments=None,
        applied_amount=None,
        has_attachments=False,
        attachments=None,
    ):
        self._type = None
        self._contact = None
        self._date = None
        self._status = None
        self._line_amount_types = None
        self._line_items = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._reference = None
        self._updated_date_utc = None
        self._currency_code = None
        self._prepayment_id = None
        self._currency_rate = None
        self._remaining_credit = None
        self._allocations = None
        self._payments = None
        self._applied_amount = None
        self._has_attachments = None
        self._attachments = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if contact is not None:
            self.contact = contact
        if date is not None:
            self.date = date
        if status is not None:
            self.status = status
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if line_items is not None:
            self.line_items = line_items
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if reference is not None:
            self.reference = reference
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if currency_code is not None:
            self.currency_code = currency_code
        if prepayment_id is not None:
            self.prepayment_id = prepayment_id
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if remaining_credit is not None:
            self.remaining_credit = remaining_credit
        if allocations is not None:
            self.allocations = allocations
        if payments is not None:
            self.payments = payments
        if applied_amount is not None:
            self.applied_amount = applied_amount
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if attachments is not None:
            self.attachments = attachments

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_values = [
            "RECEIVE-PREPAYMENT",
            "SPEND-PREPAYMENT",
            "ARPREPAYMENT",
            "APPREPAYMENT",
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
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["AUTHORISED", "PAID", "VOIDED", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def line_amount_types(self):
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        self._line_amount_types = line_amount_types

    @property
    def line_items(self):
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        self._line_items = line_items

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
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        self._currency_code = currency_code

    @property
    def prepayment_id(self):
        return self._prepayment_id

    @prepayment_id.setter
    def prepayment_id(self, prepayment_id):
        self._prepayment_id = prepayment_id

    @property
    def currency_rate(self):
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        self._currency_rate = currency_rate

    @property
    def remaining_credit(self):
        return self._remaining_credit

    @remaining_credit.setter
    def remaining_credit(self, remaining_credit):
        self._remaining_credit = remaining_credit

    @property
    def allocations(self):
        return self._allocations

    @allocations.setter
    def allocations(self, allocations):
        self._allocations = allocations

    @property
    def payments(self):
        return self._payments

    @payments.setter
    def payments(self, payments):
        self._payments = payments

    @property
    def applied_amount(self):
        return self._applied_amount

    @applied_amount.setter
    def applied_amount(self, applied_amount):
        self._applied_amount = applied_amount

    @property
    def has_attachments(self):
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        self._has_attachments = has_attachments

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        self._attachments = attachments
