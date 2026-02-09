from xero.models import BaseModel


class Receipts(BaseModel):
    openapi_types = {"receipts": "list[Receipt]"}
    attribute_map = {"receipts": "Receipts"}

    def __init__(self, receipts=None):
        self._receipts = None
        self.discriminator = None
        if receipts is not None:
            self.receipts = receipts

    @property
    def receipts(self):
        return self._receipts

    @receipts.setter
    def receipts(self, receipts):
        self._receipts = receipts
