from xero.models import BaseModel


class Price(BaseModel):
    openapi_types = {"amount": "float", "currency": "str", "id": "str"}
    attribute_map = {"amount": "amount", "currency": "currency", "id": "id"}

    def __init__(self, amount=None, currency=None, id=None):
        self._amount = None
        self._currency = None
        self._id = None
        self.discriminator = None
        self.amount = amount
        self.currency = currency
        self.id = id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")
        self._amount = amount

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")
        self._currency = currency

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        self._id = id
