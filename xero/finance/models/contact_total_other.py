from xero.models import BaseModel


class ContactTotalOther(BaseModel):
    openapi_types = {
        "total_outstanding_aged": "float",
        "total_voided": "float",
        "total_credited": "float",
        "transaction_count": "int",
    }
    attribute_map = {
        "total_outstanding_aged": "totalOutstandingAged",
        "total_voided": "totalVoided",
        "total_credited": "totalCredited",
        "transaction_count": "transactionCount",
    }

    def __init__(
        self,
        total_outstanding_aged=None,
        total_voided=None,
        total_credited=None,
        transaction_count=None,
    ):
        self._total_outstanding_aged = None
        self._total_voided = None
        self._total_credited = None
        self._transaction_count = None
        self.discriminator = None
        if total_outstanding_aged is not None:
            self.total_outstanding_aged = total_outstanding_aged
        if total_voided is not None:
            self.total_voided = total_voided
        if total_credited is not None:
            self.total_credited = total_credited
        if transaction_count is not None:
            self.transaction_count = transaction_count

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

    @property
    def transaction_count(self):
        return self._transaction_count

    @transaction_count.setter
    def transaction_count(self, transaction_count):
        self._transaction_count = transaction_count
