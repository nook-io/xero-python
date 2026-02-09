from xero.models import BaseModel


class ConversionBalances(BaseModel):
    openapi_types = {
        "account_code": "str",
        "balance": "float",
        "balance_details": "list[BalanceDetails]",
    }
    attribute_map = {
        "account_code": "AccountCode",
        "balance": "Balance",
        "balance_details": "BalanceDetails",
    }

    def __init__(self, account_code=None, balance=None, balance_details=None):
        self._account_code = None
        self._balance = None
        self._balance_details = None
        self.discriminator = None
        if account_code is not None:
            self.account_code = account_code
        if balance is not None:
            self.balance = balance
        if balance_details is not None:
            self.balance_details = balance_details

    @property
    def account_code(self):
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        self._account_code = account_code

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def balance_details(self):
        return self._balance_details

    @balance_details.setter
    def balance_details(self, balance_details):
        self._balance_details = balance_details
