from xero.models import BaseModel


class Receipt(BaseModel):
    openapi_types = {
        "date": "date[ms-format]",
        "contact": "Contact",
        "line_items": "list[LineItem]",
        "user": "User",
        "reference": "str",
        "line_amount_types": "LineAmountTypes",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "receipt_id": "str",
        "status": "str",
        "receipt_number": "str",
        "updated_date_utc": "datetime[ms-format]",
        "has_attachments": "bool",
        "url": "str",
        "validation_errors": "list[ValidationError]",
        "warnings": "list[ValidationError]",
        "attachments": "list[Attachment]",
    }
    attribute_map = {
        "date": "Date",
        "contact": "Contact",
        "line_items": "LineItems",
        "user": "User",
        "reference": "Reference",
        "line_amount_types": "LineAmountTypes",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "receipt_id": "ReceiptID",
        "status": "Status",
        "receipt_number": "ReceiptNumber",
        "updated_date_utc": "UpdatedDateUTC",
        "has_attachments": "HasAttachments",
        "url": "Url",
        "validation_errors": "ValidationErrors",
        "warnings": "Warnings",
        "attachments": "Attachments",
    }

    def __init__(
        self,
        date=None,
        contact=None,
        line_items=None,
        user=None,
        reference=None,
        line_amount_types=None,
        sub_total=None,
        total_tax=None,
        total=None,
        receipt_id=None,
        status=None,
        receipt_number=None,
        updated_date_utc=None,
        has_attachments=False,
        url=None,
        validation_errors=None,
        warnings=None,
        attachments=None,
    ):
        self._date = None
        self._contact = None
        self._line_items = None
        self._user = None
        self._reference = None
        self._line_amount_types = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._receipt_id = None
        self._status = None
        self._receipt_number = None
        self._updated_date_utc = None
        self._has_attachments = None
        self._url = None
        self._validation_errors = None
        self._warnings = None
        self._attachments = None
        self.discriminator = None
        if date is not None:
            self.date = date
        if contact is not None:
            self.contact = contact
        if line_items is not None:
            self.line_items = line_items
        if user is not None:
            self.user = user
        if reference is not None:
            self.reference = reference
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if receipt_id is not None:
            self.receipt_id = receipt_id
        if status is not None:
            self.status = status
        if receipt_number is not None:
            self.receipt_number = receipt_number
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if url is not None:
            self.url = url
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if warnings is not None:
            self.warnings = warnings
        if attachments is not None:
            self.attachments = attachments

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

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
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def line_amount_types(self):
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        self._line_amount_types = line_amount_types

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
    def receipt_id(self):
        return self._receipt_id

    @receipt_id.setter
    def receipt_id(self, receipt_id):
        self._receipt_id = receipt_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = [
            "DRAFT",
            "SUBMITTED",
            "AUTHORISED",
            "DECLINED",
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
    def receipt_number(self):
        return self._receipt_number

    @receipt_number.setter
    def receipt_number(self, receipt_number):
        self._receipt_number = receipt_number

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def has_attachments(self):
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        self._has_attachments = has_attachments

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

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
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        self._attachments = attachments
