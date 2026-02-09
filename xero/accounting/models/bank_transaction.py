from xero.models import BaseModel


class BankTransaction(BaseModel):
    openapi_types = {
        "type": "str",
        "contact": "Contact",
        "line_items": "list[LineItem]",
        "bank_account": "Account",
        "is_reconciled": "bool",
        "date": "date[ms-format]",
        "reference": "str",
        "currency_code": "CurrencyCode",
        "currency_rate": "float",
        "url": "str",
        "status": "str",
        "line_amount_types": "LineAmountTypes",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "bank_transaction_id": "str",
        "prepayment_id": "str",
        "overpayment_id": "str",
        "updated_date_utc": "datetime[ms-format]",
        "has_attachments": "bool",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "type": "Type",
        "contact": "Contact",
        "line_items": "LineItems",
        "bank_account": "BankAccount",
        "is_reconciled": "IsReconciled",
        "date": "Date",
        "reference": "Reference",
        "currency_code": "CurrencyCode",
        "currency_rate": "CurrencyRate",
        "url": "Url",
        "status": "Status",
        "line_amount_types": "LineAmountTypes",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "bank_transaction_id": "BankTransactionID",
        "prepayment_id": "PrepaymentID",
        "overpayment_id": "OverpaymentID",
        "updated_date_utc": "UpdatedDateUTC",
        "has_attachments": "HasAttachments",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        type=None,
        contact=None,
        line_items=None,
        bank_account=None,
        is_reconciled=None,
        date=None,
        reference=None,
        currency_code=None,
        currency_rate=None,
        url=None,
        status=None,
        line_amount_types=None,
        sub_total=None,
        total_tax=None,
        total=None,
        bank_transaction_id=None,
        prepayment_id=None,
        overpayment_id=None,
        updated_date_utc=None,
        has_attachments=False,
        status_attribute_string=None,
        validation_errors=None,
    ):
        self._type = None
        self._contact = None
        self._line_items = None
        self._bank_account = None
        self._is_reconciled = None
        self._date = None
        self._reference = None
        self._currency_code = None
        self._currency_rate = None
        self._url = None
        self._status = None
        self._line_amount_types = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._bank_transaction_id = None
        self._prepayment_id = None
        self._overpayment_id = None
        self._updated_date_utc = None
        self._has_attachments = None
        self._status_attribute_string = None
        self._validation_errors = None
        self.discriminator = None
        self.type = type
        if contact is not None:
            self.contact = contact
        self.line_items = line_items
        self.bank_account = bank_account
        if is_reconciled is not None:
            self.is_reconciled = is_reconciled
        if date is not None:
            self.date = date
        if reference is not None:
            self.reference = reference
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if url is not None:
            self.url = url
        if status is not None:
            self.status = status
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if bank_transaction_id is not None:
            self.bank_transaction_id = bank_transaction_id
        if prepayment_id is not None:
            self.prepayment_id = prepayment_id
        if overpayment_id is not None:
            self.overpayment_id = overpayment_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = [
            "RECEIVE",
            "RECEIVE-OVERPAYMENT",
            "RECEIVE-PREPAYMENT",
            "SPEND",
            "SPEND-OVERPAYMENT",
            "SPEND-PREPAYMENT",
            "RECEIVE-TRANSFER",
            "SPEND-TRANSFER",
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
        if line_items is None:
            raise ValueError("Invalid value for `line_items`, must not be `None`")
        self._line_items = line_items

    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        if bank_account is None:
            raise ValueError("Invalid value for `bank_account`, must not be `None`")
        self._bank_account = bank_account

    @property
    def is_reconciled(self):
        return self._is_reconciled

    @is_reconciled.setter
    def is_reconciled(self, is_reconciled):
        self._is_reconciled = is_reconciled

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

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
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["AUTHORISED", "DELETED", "VOIDED", "None"]
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
    def bank_transaction_id(self):
        return self._bank_transaction_id

    @bank_transaction_id.setter
    def bank_transaction_id(self, bank_transaction_id):
        self._bank_transaction_id = bank_transaction_id

    @property
    def prepayment_id(self):
        return self._prepayment_id

    @prepayment_id.setter
    def prepayment_id(self, prepayment_id):
        self._prepayment_id = prepayment_id

    @property
    def overpayment_id(self):
        return self._overpayment_id

    @overpayment_id.setter
    def overpayment_id(self, overpayment_id):
        self._overpayment_id = overpayment_id

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
