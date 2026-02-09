from xero.models import BaseModel


class TotalOther(BaseModel):
    openapi_types = {
        "total_outstanding_aged": "float",
        "total_voided": "float",
        "total_credited": "float",
    }
    attribute_map = {
        "total_outstanding_aged": "totalOutstandingAged",
        "total_voided": "totalVoided",
        "total_credited": "totalCredited",
    }

    def __init__(
        self, total_outstanding_aged=None, total_voided=None, total_credited=None
    ):
        self._total_outstanding_aged = None
        self._total_voided = None
        self._total_credited = None
        self.discriminator = None
        if total_outstanding_aged is not None:
            self.total_outstanding_aged = total_outstanding_aged
        if total_voided is not None:
            self.total_voided = total_voided
        if total_credited is not None:
            self.total_credited = total_credited

    @property
    def total_outstanding_aged(self):
        return self._total_outstanding_aged

    @total_outstanding_aged.setter
    def total_outstanding_aged(self, total_outstanding_aged):
        self._total_outstanding_aged = total_outstanding_aged

    @property
    def total_voided(self):
        return self._total_voided

    @total_voided.setter
    def total_voided(self, total_voided):
        self._total_voided = total_voided

    @property
    def total_credited(self):
        return self._total_credited

    @total_credited.setter
    def total_credited(self, total_credited):
        self._total_credited = total_credited
