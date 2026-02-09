from xero.models import BaseModel


class PurchaseOrder(BaseModel):
    openapi_types = {
        "contact": "Contact",
        "line_items": "list[LineItem]",
        "date": "date[ms-format]",
        "delivery_date": "date[ms-format]",
        "line_amount_types": "LineAmountTypes",
        "purchase_order_number": "str",
        "reference": "str",
        "branding_theme_id": "str",
        "currency_code": "CurrencyCode",
        "status": "str",
        "sent_to_contact": "bool",
        "delivery_address": "str",
        "attention_to": "str",
        "telephone": "str",
        "delivery_instructions": "str",
        "expected_arrival_date": "date[ms-format]",
        "purchase_order_id": "str",
        "currency_rate": "float",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "total_discount": "float",
        "has_attachments": "bool",
        "updated_date_utc": "datetime[ms-format]",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
        "warnings": "list[ValidationError]",
        "attachments": "list[Attachment]",
    }
    attribute_map = {
        "contact": "Contact",
        "line_items": "LineItems",
        "date": "Date",
        "delivery_date": "DeliveryDate",
        "line_amount_types": "LineAmountTypes",
        "purchase_order_number": "PurchaseOrderNumber",
        "reference": "Reference",
        "branding_theme_id": "BrandingThemeID",
        "currency_code": "CurrencyCode",
        "status": "Status",
        "sent_to_contact": "SentToContact",
        "delivery_address": "DeliveryAddress",
        "attention_to": "AttentionTo",
        "telephone": "Telephone",
        "delivery_instructions": "DeliveryInstructions",
        "expected_arrival_date": "ExpectedArrivalDate",
        "purchase_order_id": "PurchaseOrderID",
        "currency_rate": "CurrencyRate",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "total_discount": "TotalDiscount",
        "has_attachments": "HasAttachments",
        "updated_date_utc": "UpdatedDateUTC",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
        "warnings": "Warnings",
        "attachments": "Attachments",
    }

    def __init__(
        self,
        contact=None,
        line_items=None,
        date=None,
        delivery_date=None,
        line_amount_types=None,
        purchase_order_number=None,
        reference=None,
        branding_theme_id=None,
        currency_code=None,
        status=None,
        sent_to_contact=None,
        delivery_address=None,
        attention_to=None,
        telephone=None,
        delivery_instructions=None,
        expected_arrival_date=None,
        purchase_order_id=None,
        currency_rate=None,
        sub_total=None,
        total_tax=None,
        total=None,
        total_discount=None,
        has_attachments=False,
        updated_date_utc=None,
        status_attribute_string=None,
        validation_errors=None,
        warnings=None,
        attachments=None,
    ):
        self._contact = None
        self._line_items = None
        self._date = None
        self._delivery_date = None
        self._line_amount_types = None
        self._purchase_order_number = None
        self._reference = None
        self._branding_theme_id = None
        self._currency_code = None
        self._status = None
        self._sent_to_contact = None
        self._delivery_address = None
        self._attention_to = None
        self._telephone = None
        self._delivery_instructions = None
        self._expected_arrival_date = None
        self._purchase_order_id = None
        self._currency_rate = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._total_discount = None
        self._has_attachments = None
        self._updated_date_utc = None
        self._status_attribute_string = None
        self._validation_errors = None
        self._warnings = None
        self._attachments = None
        self.discriminator = None
        if contact is not None:
            self.contact = contact
        if line_items is not None:
            self.line_items = line_items
        if date is not None:
            self.date = date
        if delivery_date is not None:
            self.delivery_date = delivery_date
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if reference is not None:
            self.reference = reference
        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if currency_code is not None:
            self.currency_code = currency_code
        if status is not None:
            self.status = status
        if sent_to_contact is not None:
            self.sent_to_contact = sent_to_contact
        if delivery_address is not None:
            self.delivery_address = delivery_address
        if attention_to is not None:
            self.attention_to = attention_to
        if telephone is not None:
            self.telephone = telephone
        if delivery_instructions is not None:
            self.delivery_instructions = delivery_instructions
        if expected_arrival_date is not None:
            self.expected_arrival_date = expected_arrival_date
        if purchase_order_id is not None:
            self.purchase_order_id = purchase_order_id
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if total_discount is not None:
            self.total_discount = total_discount
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if warnings is not None:
            self.warnings = warnings
        if attachments is not None:
            self.attachments = attachments

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
    def delivery_date(self):
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        self._delivery_date = delivery_date

    @property
    def line_amount_types(self):
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        self._line_amount_types = line_amount_types

    @property
    def purchase_order_number(self):
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        self._purchase_order_number = purchase_order_number

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
        allowed_values = [
            "DRAFT",
            "SUBMITTED",
            "AUTHORISED",
            "BILLED",
            "DELETED",
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
    def delivery_address(self):
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        self._delivery_address = delivery_address

    @property
    def attention_to(self):
        return self._attention_to

    @attention_to.setter
    def attention_to(self, attention_to):
        self._attention_to = attention_to

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        self._telephone = telephone

    @property
    def delivery_instructions(self):
        return self._delivery_instructions

    @delivery_instructions.setter
    def delivery_instructions(self, delivery_instructions):
        self._delivery_instructions = delivery_instructions

    @property
    def expected_arrival_date(self):
        return self._expected_arrival_date

    @expected_arrival_date.setter
    def expected_arrival_date(self, expected_arrival_date):
        self._expected_arrival_date = expected_arrival_date

    @property
    def purchase_order_id(self):
        return self._purchase_order_id

    @purchase_order_id.setter
    def purchase_order_id(self, purchase_order_id):
        self._purchase_order_id = purchase_order_id

    @property
    def currency_rate(self):
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        self._currency_rate = currency_rate

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
    def has_attachments(self):
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        self._has_attachments = has_attachments

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

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
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        self._attachments = attachments
