from xero.models import BaseModel


class RepeatingInvoice(BaseModel):
    openapi_types = {
        "type": "str",
        "contact": "Contact",
        "schedule": "Schedule",
        "line_items": "list[LineItem]",
        "line_amount_types": "LineAmountTypes",
        "reference": "str",
        "branding_theme_id": "str",
        "currency_code": "CurrencyCode",
        "status": "str",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "repeating_invoice_id": "str",
        "id": "str",
        "has_attachments": "bool",
        "attachments": "list[Attachment]",
        "approved_for_sending": "bool",
        "send_copy": "bool",
        "mark_as_sent": "bool",
        "include_pdf": "bool",
    }
    attribute_map = {
        "type": "Type",
        "contact": "Contact",
        "schedule": "Schedule",
        "line_items": "LineItems",
        "line_amount_types": "LineAmountTypes",
        "reference": "Reference",
        "branding_theme_id": "BrandingThemeID",
        "currency_code": "CurrencyCode",
        "status": "Status",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "repeating_invoice_id": "RepeatingInvoiceID",
        "id": "ID",
        "has_attachments": "HasAttachments",
        "attachments": "Attachments",
        "approved_for_sending": "ApprovedForSending",
        "send_copy": "SendCopy",
        "mark_as_sent": "MarkAsSent",
        "include_pdf": "IncludePDF",
    }

    def __init__(
        self,
        type=None,
        contact=None,
        schedule=None,
        line_items=None,
        line_amount_types=None,
        reference=None,
        branding_theme_id=None,
        currency_code=None,
        status=None,
        sub_total=None,
        total_tax=None,
        total=None,
        repeating_invoice_id=None,
        id=None,
        has_attachments=False,
        attachments=None,
        approved_for_sending=False,
        send_copy=False,
        mark_as_sent=False,
        include_pdf=False,
    ):
        self._type = None
        self._contact = None
        self._schedule = None
        self._line_items = None
        self._line_amount_types = None
        self._reference = None
        self._branding_theme_id = None
        self._currency_code = None
        self._status = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._repeating_invoice_id = None
        self._id = None
        self._has_attachments = None
        self._attachments = None
        self._approved_for_sending = None
        self._send_copy = None
        self._mark_as_sent = None
        self._include_pdf = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if contact is not None:
            self.contact = contact
        if schedule is not None:
            self.schedule = schedule
        if line_items is not None:
            self.line_items = line_items
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if reference is not None:
            self.reference = reference
        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if currency_code is not None:
            self.currency_code = currency_code
        if status is not None:
            self.status = status
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if repeating_invoice_id is not None:
            self.repeating_invoice_id = repeating_invoice_id
        if id is not None:
            self.id = id
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if attachments is not None:
            self.attachments = attachments
        if approved_for_sending is not None:
            self.approved_for_sending = approved_for_sending
        if send_copy is not None:
            self.send_copy = send_copy
        if mark_as_sent is not None:
            self.mark_as_sent = mark_as_sent
        if include_pdf is not None:
            self.include_pdf = include_pdf

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_values = ["ACCPAY", "ACCREC", "None"]
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
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        self._schedule = schedule

    @property
    def line_items(self):
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        self._line_items = line_items

    @property
    def line_amount_types(self):
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        self._line_amount_types = line_amount_types

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
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        self._currency_code = currency_code

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["DRAFT", "AUTHORISED", "DELETED", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

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
    def repeating_invoice_id(self):
        return self._repeating_invoice_id

    @repeating_invoice_id.setter
    def repeating_invoice_id(self, repeating_invoice_id):
        self._repeating_invoice_id = repeating_invoice_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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

    @property
    def approved_for_sending(self):
        return self._approved_for_sending

    @approved_for_sending.setter
    def approved_for_sending(self, approved_for_sending):
        self._approved_for_sending = approved_for_sending

    @property
    def send_copy(self):
        return self._send_copy

    @send_copy.setter
    def send_copy(self, send_copy):
        self._send_copy = send_copy

    @property
    def mark_as_sent(self):
        return self._mark_as_sent

    @mark_as_sent.setter
    def mark_as_sent(self, mark_as_sent):
        self._mark_as_sent = mark_as_sent

    @property
    def include_pdf(self):
        return self._include_pdf

    @include_pdf.setter
    def include_pdf(self, include_pdf):
        self._include_pdf = include_pdf
