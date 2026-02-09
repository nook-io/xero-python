from xero.models import BaseModel


class Setup(BaseModel):
    openapi_types = {
        "conversion_date": "ConversionDate",
        "conversion_balances": "list[ConversionBalances]",
        "accounts": "list[Account]",
    }
    attribute_map = {
        "conversion_date": "ConversionDate",
        "conversion_balances": "ConversionBalances",
        "accounts": "Accounts",
    }

    def __init__(self, conversion_date=None, conversion_balances=None, accounts=None):
        self._conversion_date = None
        self._conversion_balances = None
        self._accounts = None
        self.discriminator = None
        if conversion_date is not None:
            self.conversion_date = conversion_date
        if conversion_balances is not None:
            self.conversion_balances = conversion_balances
        if accounts is not None:
            self.accounts = accounts

    @property
    def conversion_date(self):
        return self._conversion_date

    @conversion_date.setter
    def conversion_date(self, conversion_date):
        self._conversion_date = conversion_date

    @property
    def conversion_balances(self):
        return self._conversion_balances

    @conversion_balances.setter
    def conversion_balances(self, conversion_balances):
        self._conversion_balances = conversion_balances

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts
