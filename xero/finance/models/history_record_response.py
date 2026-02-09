from xero.models import BaseModel


class HistoryRecordResponse(BaseModel):
    openapi_types = {
        "changes": "str",
        "date_utc_string": "str",
        "date_utc": "datetime",
        "user": "str",
        "details": "str",
    }
    attribute_map = {
        "changes": "changes",
        "date_utc_string": "dateUTCString",
        "date_utc": "dateUTC",
        "user": "user",
        "details": "details",
    }

    def __init__(
        self, changes=None, date_utc_string=None, date_utc=None, user=None, details=None
    ):
        self._changes = None
        self._date_utc_string = None
        self._date_utc = None
        self._user = None
        self._details = None
        self.discriminator = None
        if changes is not None:
            self.changes = changes
        if date_utc_string is not None:
            self.date_utc_string = date_utc_string
        if date_utc is not None:
            self.date_utc = date_utc
        if user is not None:
            self.user = user
        if details is not None:
            self.details = details

    @property
    def changes(self):
        return self._changes

    @changes.setter
    def changes(self, changes):
        self._changes = changes

    @property
    def date_utc_string(self):
        return self._date_utc_string

    @date_utc_string.setter
    def date_utc_string(self, date_utc_string):
        self._date_utc_string = date_utc_string

    @property
    def date_utc(self):
        return self._date_utc

    @date_utc.setter
    def date_utc(self, date_utc):
        self._date_utc = date_utc

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details
