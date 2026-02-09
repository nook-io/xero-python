from xero.models import BaseModel


class LockHistoryResponse(BaseModel):
    openapi_types = {
        "organisation_id": "str",
        "end_date": "date",
        "lock_dates": "list[LockHistoryModel]",
    }
    attribute_map = {
        "organisation_id": "organisationId",
        "end_date": "endDate",
        "lock_dates": "lockDates",
    }

    def __init__(self, organisation_id=None, end_date=None, lock_dates=None):
        self._organisation_id = None
        self._end_date = None
        self._lock_dates = None
        self.discriminator = None
        if organisation_id is not None:
            self.organisation_id = organisation_id
        if end_date is not None:
            self.end_date = end_date
        if lock_dates is not None:
            self.lock_dates = lock_dates

    @property
    def organisation_id(self):
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        self._organisation_id = organisation_id

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @property
    def lock_dates(self):
        return self._lock_dates

    @lock_dates.setter
    def lock_dates(self, lock_dates):
        self._lock_dates = lock_dates
