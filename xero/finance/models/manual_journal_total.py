from xero.models import BaseModel


class ManualJournalTotal(BaseModel):
    openapi_types = {"total": "float"}
    attribute_map = {"total": "total"}

    def __init__(self, total=None):
        self._total = None
        self.discriminator = None
        if total is not None:
            self.total = total

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total
