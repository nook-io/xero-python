from xero.models import BaseModel


class BankTransfer(BaseModel):
    openapi_types = {
        "from_bank_account": "Account",
        "to_bank_account": "Account",
        "amount": "float",
        "date": "date[ms-format]",
        "bank_transfer_id": "str",
        "currency_rate": "float",
        "from_bank_transaction_id": "str",
        "to_bank_transaction_id": "str",
        "from_is_reconciled": "bool",
        "to_is_reconciled": "bool",
        "reference": "str",
        "has_attachments": "bool",
        "created_date_utc": "datetime[ms-format]",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "from_bank_account": "FromBankAccount",
        "to_bank_account": "ToBankAccount",
        "amount": "Amount",
        "date": "Date",
        "bank_transfer_id": "BankTransferID",
        "currency_rate": "CurrencyRate",
        "from_bank_transaction_id": "FromBankTransactionID",
        "to_bank_transaction_id": "ToBankTransactionID",
        "from_is_reconciled": "FromIsReconciled",
        "to_is_reconciled": "ToIsReconciled",
        "reference": "Reference",
        "has_attachments": "HasAttachments",
        "created_date_utc": "CreatedDateUTC",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        from_bank_account=None,
        to_bank_account=None,
        amount=None,
        date=None,
        bank_transfer_id=None,
        currency_rate=None,
        from_bank_transaction_id=None,
        to_bank_transaction_id=None,
        from_is_reconciled=False,
        to_is_reconciled=False,
        reference=None,
        has_attachments=False,
        created_date_utc=None,
        validation_errors=None,
    ):
        self._from_bank_account = None
        self._to_bank_account = None
        self._amount = None
        self._date = None
        self._bank_transfer_id = None
        self._currency_rate = None
        self._from_bank_transaction_id = None
        self._to_bank_transaction_id = None
        self._from_is_reconciled = None
        self._to_is_reconciled = None
        self._reference = None
        self._has_attachments = None
        self._created_date_utc = None
        self._validation_errors = None
        self.discriminator = None
        self.from_bank_account = from_bank_account
        self.to_bank_account = to_bank_account
        self.amount = amount
        if date is not None:
            self.date = date
        if bank_transfer_id is not None:
            self.bank_transfer_id = bank_transfer_id
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if from_bank_transaction_id is not None:
            self.from_bank_transaction_id = from_bank_transaction_id
        if to_bank_transaction_id is not None:
            self.to_bank_transaction_id = to_bank_transaction_id
        if from_is_reconciled is not None:
            self.from_is_reconciled = from_is_reconciled
        if to_is_reconciled is not None:
            self.to_is_reconciled = to_is_reconciled
        if reference is not None:
            self.reference = reference
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def from_bank_account(self):
        return self._from_bank_account

    @from_bank_account.setter
    def from_bank_account(self, from_bank_account):
        if from_bank_account is None:
            raise ValueError(
                "Invalid value for `from_bank_account`, must not be `None`"
            )
        self._from_bank_account = from_bank_account

    @property
    def to_bank_account(self):
        return self._to_bank_account

    @to_bank_account.setter
    def to_bank_account(self, to_bank_account):
        if to_bank_account is None:
            raise ValueError("Invalid value for `to_bank_account`, must not be `None`")
        self._to_bank_account = to_bank_account

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")
        self._amount = amount

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def bank_transfer_id(self):
        return self._bank_transfer_id

    @bank_transfer_id.setter
    def bank_transfer_id(self, bank_transfer_id):
        self._bank_transfer_id = bank_transfer_id

    @property
    def currency_rate(self):
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        self._currency_rate = currency_rate

    @property
    def from_bank_transaction_id(self):
        return self._from_bank_transaction_id

    @from_bank_transaction_id.setter
    def from_bank_transaction_id(self, from_bank_transaction_id):
        self._from_bank_transaction_id = from_bank_transaction_id

    @property
    def to_bank_transaction_id(self):
        return self._to_bank_transaction_id

    @to_bank_transaction_id.setter
    def to_bank_transaction_id(self, to_bank_transaction_id):
        self._to_bank_transaction_id = to_bank_transaction_id

    @property
    def from_is_reconciled(self):
        return self._from_is_reconciled

    @from_is_reconciled.setter
    def from_is_reconciled(self, from_is_reconciled):
        self._from_is_reconciled = from_is_reconciled

    @property
    def to_is_reconciled(self):
        return self._to_is_reconciled

    @to_is_reconciled.setter
    def to_is_reconciled(self, to_is_reconciled):
        self._to_is_reconciled = to_is_reconciled

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def has_attachments(self):
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        self._has_attachments = has_attachments

    @property
    def created_date_utc(self):
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        self._created_date_utc = created_date_utc

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
