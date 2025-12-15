from xero.models import BaseModel


class Quotes(BaseModel):
    openapi_types = {"quotes": "list[Quote]"}
    attribute_map = {"quotes": "Quotes"}

    def __init__(self, quotes=None):
        self._quotes = None
        self.discriminator = None
        if quotes is not None:
            self.quotes = quotes

    @property
    def quotes(self):
        return self._quotes

    @quotes.setter
    def quotes(self, quotes):
        self._quotes = quotes
