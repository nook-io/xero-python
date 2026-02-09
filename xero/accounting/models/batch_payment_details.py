from xero.models import BaseModel


class BatchPaymentDetails(BaseModel):
    openapi_types = {
        "bank_account_number": "str",
        "bank_account_name": "str",
        "details": "str",
        "code": "str",
        "reference": "str",
    }
    attribute_map = {
        "bank_account_number": "BankAccountNumber",
        "bank_account_name": "BankAccountName",
        "details": "Details",
        "code": "Code",
        "reference": "Reference",
    }

    def __init__(
        self,
        bank_account_number=None,
        bank_account_name=None,
        details=None,
        code=None,
        reference=None,
    ):
        self._bank_account_number = None
        self._bank_account_name = None
        self._details = None
        self._code = None
        self._reference = None
        self.discriminator = None
        if bank_account_number is not None:
            self.bank_account_number = bank_account_number
        if bank_account_name is not None:
            self.bank_account_name = bank_account_name
        if details is not None:
            self.details = details
        if code is not None:
            self.code = code
        if reference is not None:
            self.reference = reference

    @property
    def bank_account_number(self):
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        self._bank_account_number = bank_account_number

    @property
    def bank_account_name(self):
        return self._bank_account_name

    @bank_account_name.setter
    def bank_account_name(self, bank_account_name):
        self._bank_account_name = bank_account_name

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

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
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if reference is not None and len(reference) > 12:
            raise ValueError(
                "Invalid value for `reference`, "
                "length must be less than or equal to `12`"
            )
        self._reference = reference
