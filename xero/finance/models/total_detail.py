from xero.models import BaseModel


class TotalDetail(BaseModel):
    openapi_types = {
        "total_paid": "float",
        "total_outstanding": "float",
        "total_credited_un_applied": "float",
    }
    attribute_map = {
        "total_paid": "totalPaid",
        "total_outstanding": "totalOutstanding",
        "total_credited_un_applied": "totalCreditedUnApplied",
    }

    def __init__(
        self, total_paid=None, total_outstanding=None, total_credited_un_applied=None
    ):
        self._total_paid = None
        self._total_outstanding = None
        self._total_credited_un_applied = None
        self.discriminator = None
        if total_paid is not None:
            self.total_paid = total_paid
        if total_outstanding is not None:
            self.total_outstanding = total_outstanding
        if total_credited_un_applied is not None:
            self.total_credited_un_applied = total_credited_un_applied

    @property
    def total_paid(self):
        return self._total_paid

    @total_paid.setter
    def total_paid(self, total_paid):
        self._total_paid = total_paid

    @property
    def total_outstanding(self):
        return self._total_outstanding

    @total_outstanding.setter
    def total_outstanding(self, total_outstanding):
        self._total_outstanding = total_outstanding

    @property
    def total_credited_un_applied(self):
        return self._total_credited_un_applied

    @total_credited_un_applied.setter
    def total_credited_un_applied(self, total_credited_un_applied):
        self._total_credited_un_applied = total_credited_un_applied
