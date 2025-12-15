from xero.models import BaseModel


class LockHistoryModel(BaseModel):
    openapi_types = {
        "hard_lock_date": "date",
        "soft_lock_date": "date",
        "updated_date_utc": "datetime",
    }
    attribute_map = {
        "hard_lock_date": "hardLockDate",
        "soft_lock_date": "softLockDate",
        "updated_date_utc": "updatedDateUtc",
    }

    def __init__(self, hard_lock_date=None, soft_lock_date=None, updated_date_utc=None):
        self._hard_lock_date = None
        self._soft_lock_date = None
        self._updated_date_utc = None
        self.discriminator = None
        if hard_lock_date is not None:
            self.hard_lock_date = hard_lock_date
        if soft_lock_date is not None:
            self.soft_lock_date = soft_lock_date
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def hard_lock_date(self):
        return self._hard_lock_date

    @hard_lock_date.setter
    def hard_lock_date(self, hard_lock_date):
        self._hard_lock_date = hard_lock_date

    @property
    def soft_lock_date(self):
        return self._soft_lock_date

    @soft_lock_date.setter
    def soft_lock_date(self, soft_lock_date):
        self._soft_lock_date = soft_lock_date

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc
