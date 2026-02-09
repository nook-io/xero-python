from xero.models import BaseModel


class BankAccount(BaseModel):
    openapi_types = {
        "statement_text": "str",
        "account_name": "str",
        "bsb": "str",
        "account_number": "str",
        "remainder": "bool",
        "amount": "float",
    }
    attribute_map = {
        "statement_text": "StatementText",
        "account_name": "AccountName",
        "bsb": "BSB",
        "account_number": "AccountNumber",
        "remainder": "Remainder",
        "amount": "Amount",
    }

    def __init__(
        self,
        statement_text=None,
        account_name=None,
        bsb=None,
        account_number=None,
        remainder=None,
        amount=None,
    ):
        self._statement_text = None
        self._account_name = None
        self._bsb = None
        self._account_number = None
        self._remainder = None
        self._amount = None
        self.discriminator = None
        if statement_text is not None:
            self.statement_text = statement_text
        if account_name is not None:
            self.account_name = account_name
        if bsb is not None:
            self.bsb = bsb
        if account_number is not None:
            self.account_number = account_number
        if remainder is not None:
            self.remainder = remainder
        if amount is not None:
            self.amount = amount

    @property
    def statement_text(self):
        return self._statement_text

    @statement_text.setter
    def statement_text(self, statement_text):
        self._statement_text = statement_text

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        self._account_name = account_name

    @property
    def bsb(self):
        return self._bsb

    @bsb.setter
    def bsb(self, bsb):
        self._bsb = bsb

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        self._account_number = account_number

    @property
    def remainder(self):
        return self._remainder

    @remainder.setter
    def remainder(self, remainder):
        self._remainder = remainder

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount
