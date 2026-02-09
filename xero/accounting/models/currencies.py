from xero.models import BaseModel


class Currencies(BaseModel):
    openapi_types = {"currencies": "list[Currency]"}
    attribute_map = {"currencies": "Currencies"}

    def __init__(self, currencies=None):
        self._currencies = None
        self.discriminator = None
        if currencies is not None:
            self.currencies = currencies

    @property
    def currencies(self):
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        self._currencies = currencies
