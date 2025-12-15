from xero.models import BaseModel


class CurrentStatementResponse(BaseModel):
    openapi_types = {
        "start_date": "date",
        "end_date": "date",
        "start_balance": "float",
        "end_balance": "float",
        "imported_date_time_utc": "datetime",
        "import_source_type": "str",
    }
    attribute_map = {
        "start_date": "startDate",
        "end_date": "endDate",
        "start_balance": "startBalance",
        "end_balance": "endBalance",
        "imported_date_time_utc": "importedDateTimeUtc",
        "import_source_type": "importSourceType",
    }

    def __init__(
        self,
        start_date=None,
        end_date=None,
        start_balance=None,
        end_balance=None,
        imported_date_time_utc=None,
        import_source_type=None,
    ):
        self._start_date = None
        self._end_date = None
        self._start_balance = None
        self._end_balance = None
        self._imported_date_time_utc = None
        self._import_source_type = None
        self.discriminator = None
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if start_balance is not None:
            self.start_balance = start_balance
        if end_balance is not None:
            self.end_balance = end_balance
        if imported_date_time_utc is not None:
            self.imported_date_time_utc = imported_date_time_utc
        if import_source_type is not None:
            self.import_source_type = import_source_type

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @property
    def start_balance(self):
        return self._start_balance

    @start_balance.setter
    def start_balance(self, start_balance):
        self._start_balance = start_balance

    @property
    def end_balance(self):
        return self._end_balance

    @end_balance.setter
    def end_balance(self, end_balance):
        self._end_balance = end_balance

    @property
    def imported_date_time_utc(self):
        return self._imported_date_time_utc

    @imported_date_time_utc.setter
    def imported_date_time_utc(self, imported_date_time_utc):
        self._imported_date_time_utc = imported_date_time_utc

    @property
    def import_source_type(self):
        return self._import_source_type

    @import_source_type.setter
    def import_source_type(self, import_source_type):
        self._import_source_type = import_source_type
