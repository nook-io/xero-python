from xero.models import BaseModel


class BalanceDetails(BaseModel):
    openapi_types = {
        "balance": "float",
        "currency_code": "str",
        "currency_rate": "float",
    }
    attribute_map = {
        "balance": "Balance",
        "currency_code": "CurrencyCode",
        "currency_rate": "CurrencyRate",
    }

    def __init__(self, balance=None, currency_code=None, currency_rate=None):
        self._balance = None
        self._currency_code = None
        self._currency_rate = None
        self.discriminator = None
        if balance is not None:
            self.balance = balance
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_rate is not None:
            self.currency_rate = currency_rate

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

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
