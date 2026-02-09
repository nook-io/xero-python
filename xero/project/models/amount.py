from xero.models import BaseModel


class Amount(BaseModel):
    openapi_types = {"currency": "CurrencyCode", "value": "float"}
    attribute_map = {"currency": "currency", "value": "value"}

    def __init__(self, currency=None, value=None):
        self._currency = None
        self._value = None
        self.discriminator = None
        if currency is not None:
            self.currency = currency
        if value is not None:
            self.value = value

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
