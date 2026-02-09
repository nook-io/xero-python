from xero.models import BaseModel


class Payment(BaseModel):
    openapi_types = {
        "invoice": "Invoice",
        "credit_note": "CreditNote",
        "prepayment": "Prepayment",
        "overpayment": "Overpayment",
        "invoice_number": "str",
        "credit_note_number": "str",
        "batch_payment": "BatchPayment",
        "account": "Account",
        "code": "str",
        "date": "date[ms-format]",
        "currency_rate": "float",
        "amount": "float",
        "bank_amount": "float",
        "reference": "str",
        "is_reconciled": "bool",
        "status": "str",
        "payment_type": "str",
        "updated_date_utc": "datetime[ms-format]",
        "payment_id": "str",
        "batch_payment_id": "str",
        "bank_account_number": "str",
        "particulars": "str",
        "details": "str",
        "has_account": "bool",
        "has_validation_errors": "bool",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
        "warnings": "list[ValidationError]",
    }
    attribute_map = {
        "invoice": "Invoice",
        "credit_note": "CreditNote",
        "prepayment": "Prepayment",
        "overpayment": "Overpayment",
        "invoice_number": "InvoiceNumber",
        "credit_note_number": "CreditNoteNumber",
        "batch_payment": "BatchPayment",
        "account": "Account",
        "code": "Code",
        "date": "Date",
        "currency_rate": "CurrencyRate",
        "amount": "Amount",
        "bank_amount": "BankAmount",
        "reference": "Reference",
        "is_reconciled": "IsReconciled",
        "status": "Status",
        "payment_type": "PaymentType",
        "updated_date_utc": "UpdatedDateUTC",
        "payment_id": "PaymentID",
        "batch_payment_id": "BatchPaymentID",
        "bank_account_number": "BankAccountNumber",
        "particulars": "Particulars",
        "details": "Details",
        "has_account": "HasAccount",
        "has_validation_errors": "HasValidationErrors",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
        "warnings": "Warnings",
    }

    def __init__(
        self,
        invoice=None,
        credit_note=None,
        prepayment=None,
        overpayment=None,
        invoice_number=None,
        credit_note_number=None,
        batch_payment=None,
        account=None,
        code=None,
        date=None,
        currency_rate=None,
        amount=None,
        bank_amount=None,
        reference=None,
        is_reconciled=None,
        status=None,
        payment_type=None,
        updated_date_utc=None,
        payment_id=None,
        batch_payment_id=None,
        bank_account_number=None,
        particulars=None,
        details=None,
        has_account=False,
        has_validation_errors=False,
        status_attribute_string=None,
        validation_errors=None,
        warnings=None,
    ):
        self._invoice = None
        self._credit_note = None
        self._prepayment = None
        self._overpayment = None
        self._invoice_number = None
        self._credit_note_number = None
        self._batch_payment = None
        self._account = None
        self._code = None
        self._date = None
        self._currency_rate = None
        self._amount = None
        self._bank_amount = None
        self._reference = None
        self._is_reconciled = None
        self._status = None
        self._payment_type = None
        self._updated_date_utc = None
        self._payment_id = None
        self._batch_payment_id = None
        self._bank_account_number = None
        self._particulars = None
        self._details = None
        self._has_account = None
        self._has_validation_errors = None
        self._status_attribute_string = None
        self._validation_errors = None
        self._warnings = None
        self.discriminator = None
        if invoice is not None:
            self.invoice = invoice
        if credit_note is not None:
            self.credit_note = credit_note
        if prepayment is not None:
            self.prepayment = prepayment
        if overpayment is not None:
            self.overpayment = overpayment
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if credit_note_number is not None:
            self.credit_note_number = credit_note_number
        if batch_payment is not None:
            self.batch_payment = batch_payment
        if account is not None:
            self.account = account
        if code is not None:
            self.code = code
        if date is not None:
            self.date = date
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if amount is not None:
            self.amount = amount
        if bank_amount is not None:
            self.bank_amount = bank_amount
        if reference is not None:
            self.reference = reference
        if is_reconciled is not None:
            self.is_reconciled = is_reconciled
        if status is not None:
            self.status = status
        if payment_type is not None:
            self.payment_type = payment_type
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if payment_id is not None:
            self.payment_id = payment_id
        if batch_payment_id is not None:
            self.batch_payment_id = batch_payment_id
        if bank_account_number is not None:
            self.bank_account_number = bank_account_number
        if particulars is not None:
            self.particulars = particulars
        if details is not None:
            self.details = details
        if has_account is not None:
            self.has_account = has_account
        if has_validation_errors is not None:
            self.has_validation_errors = has_validation_errors
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if warnings is not None:
            self.warnings = warnings

    @property
    def invoice(self):
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        self._invoice = invoice

    @property
    def credit_note(self):
        return self._credit_note

    @credit_note.setter
    def credit_note(self, credit_note):
        self._credit_note = credit_note

    @property
    def prepayment(self):
        return self._prepayment

    @prepayment.setter
    def prepayment(self, prepayment):
        self._prepayment = prepayment

    @property
    def overpayment(self):
        return self._overpayment

    @overpayment.setter
    def overpayment(self, overpayment):
        self._overpayment = overpayment

    @property
    def invoice_number(self):
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        self._invoice_number = invoice_number

    @property
    def credit_note_number(self):
        return self._credit_note_number

    @credit_note_number.setter
    def credit_note_number(self, credit_note_number):
        self._credit_note_number = credit_note_number

    @property
    def batch_payment(self):
        return self._batch_payment

    @batch_payment.setter
    def batch_payment(self, batch_payment):
        self._batch_payment = batch_payment

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, account):
        self._account = account

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def currency_rate(self):
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        self._currency_rate = currency_rate

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def bank_amount(self):
        return self._bank_amount

    @bank_amount.setter
    def bank_amount(self, bank_amount):
        self._bank_amount = bank_amount

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def is_reconciled(self):
        return self._is_reconciled

    @is_reconciled.setter
    def is_reconciled(self, is_reconciled):
        self._is_reconciled = is_reconciled

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
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        allowed_values = [
            "ACCRECPAYMENT",
            "ACCPAYPAYMENT",
            "ARCREDITPAYMENT",
            "APCREDITPAYMENT",
            "AROVERPAYMENTPAYMENT",
            "ARPREPAYMENTPAYMENT",
            "APPREPAYMENTPAYMENT",
            "APOVERPAYMENTPAYMENT",
            "None",
        ]
        if payment_type:
            if payment_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `payment_type` ({0}), must be one of {1}".format(
                        payment_type, allowed_values
                    )
                )
        self._payment_type = payment_type

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        self._payment_id = payment_id

    @property
    def batch_payment_id(self):
        return self._batch_payment_id

    @batch_payment_id.setter
    def batch_payment_id(self, batch_payment_id):
        self._batch_payment_id = batch_payment_id

    @property
    def bank_account_number(self):
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        self._bank_account_number = bank_account_number

    @property
    def particulars(self):
        return self._particulars

    @particulars.setter
    def particulars(self, particulars):
        self._particulars = particulars

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

    @property
    def has_account(self):
        return self._has_account

    @has_account.setter
    def has_account(self, has_account):
        self._has_account = has_account

    @property
    def has_validation_errors(self):
        return self._has_validation_errors

    @has_validation_errors.setter
    def has_validation_errors(self, has_validation_errors):
        self._has_validation_errors = has_validation_errors

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
