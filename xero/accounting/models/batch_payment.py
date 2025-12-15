from xero.models import BaseModel


class BatchPayment(BaseModel):
    openapi_types = {
        "account": "Account",
        "reference": "str",
        "particulars": "str",
        "code": "str",
        "details": "str",
        "narrative": "str",
        "batch_payment_id": "str",
        "date_string": "str",
        "date": "date[ms-format]",
        "amount": "float",
        "payments": "list[Payment]",
        "type": "str",
        "status": "str",
        "total_amount": "float",
        "updated_date_utc": "datetime[ms-format]",
        "is_reconciled": "bool",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "account": "Account",
        "reference": "Reference",
        "particulars": "Particulars",
        "code": "Code",
        "details": "Details",
        "narrative": "Narrative",
        "batch_payment_id": "BatchPaymentID",
        "date_string": "DateString",
        "date": "Date",
        "amount": "Amount",
        "payments": "Payments",
        "type": "Type",
        "status": "Status",
        "total_amount": "TotalAmount",
        "updated_date_utc": "UpdatedDateUTC",
        "is_reconciled": "IsReconciled",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        account=None,
        reference=None,
        particulars=None,
        code=None,
        details=None,
        narrative=None,
        batch_payment_id=None,
        date_string=None,
        date=None,
        amount=None,
        payments=None,
        type=None,
        status=None,
        total_amount=None,
        updated_date_utc=None,
        is_reconciled=None,
        validation_errors=None,
    ):
        self._account = None
        self._reference = None
        self._particulars = None
        self._code = None
        self._details = None
        self._narrative = None
        self._batch_payment_id = None
        self._date_string = None
        self._date = None
        self._amount = None
        self._payments = None
        self._type = None
        self._status = None
        self._total_amount = None
        self._updated_date_utc = None
        self._is_reconciled = None
        self._validation_errors = None
        self.discriminator = None
        if account is not None:
            self.account = account
        if reference is not None:
            self.reference = reference
        if particulars is not None:
            self.particulars = particulars
        if code is not None:
            self.code = code
        if details is not None:
            self.details = details
        if narrative is not None:
            self.narrative = narrative
        if batch_payment_id is not None:
            self.batch_payment_id = batch_payment_id
        if date_string is not None:
            self.date_string = date_string
        if date is not None:
            self.date = date
        if amount is not None:
            self.amount = amount
        if payments is not None:
            self.payments = payments
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if total_amount is not None:
            self.total_amount = total_amount
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if is_reconciled is not None:
            self.is_reconciled = is_reconciled
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, account):
        self._account = account

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if reference is not None and len(reference) > 255:
            raise ValueError(
                "Invalid value for `reference`, "
                "length must be less than or equal to `255`"
            )
        self._reference = reference

    @property
    def particulars(self):
        return self._particulars

    @particulars.setter
    def particulars(self, particulars):
        if particulars is not None and len(particulars) > 12:
            raise ValueError(
                "Invalid value for `particulars`, "
                "length must be less than or equal to `12`"
            )
        self._particulars = particulars

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if code is not None and len(code) > 12:
            raise ValueError(
                "Invalid value for `code`, length must be less than or equal to `12`"
            )
        self._code = code

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

    @property
    def narrative(self):
        return self._narrative

    @narrative.setter
    def narrative(self, narrative):
        if narrative is not None and len(narrative) > 18:
            raise ValueError(
                "Invalid value for `narrative`, "
                "length must be less than or equal to `18`"
            )
        self._narrative = narrative

    @property
    def batch_payment_id(self):
        return self._batch_payment_id

    @batch_payment_id.setter
    def batch_payment_id(self, batch_payment_id):
        self._batch_payment_id = batch_payment_id

    @property
    def date_string(self):
        return self._date_string

    @date_string.setter
    def date_string(self, date_string):
        self._date_string = date_string

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def payments(self):
        return self._payments

    @payments.setter
    def payments(self, payments):
        self._payments = payments

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_values = ["PAYBATCH", "RECBATCH", "None"]
        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(
                        type, allowed_values
                    )
                )
        self._type = type

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["AUTHORISED", "DELETED", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def is_reconciled(self):
        return self._is_reconciled

    @is_reconciled.setter
    def is_reconciled(self, is_reconciled):
        self._is_reconciled = is_reconciled

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
