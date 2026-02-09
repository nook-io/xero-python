from xero.models import BaseModel


class HistoryRecord(BaseModel):
    openapi_types = {
        "details": "str",
        "changes": "str",
        "user": "str",
        "date_utc": "datetime[ms-format]",
    }
    attribute_map = {
        "details": "Details",
        "changes": "Changes",
        "user": "User",
        "date_utc": "DateUTC",
    }

    def __init__(self, details=None, changes=None, user=None, date_utc=None):
        self._details = None
        self._changes = None
        self._user = None
        self._date_utc = None
        self.discriminator = None
        if details is not None:
            self.details = details
        if changes is not None:
            self.changes = changes
        if user is not None:
            self.user = user
        if date_utc is not None:
            self.date_utc = date_utc

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

    @property
    def changes(self):
        return self._changes

    @changes.setter
    def changes(self, changes):
        self._changes = changes

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def date_utc(self):
        return self._date_utc

    @date_utc.setter
    def date_utc(self, date_utc):
        self._date_utc = date_utc
