from xero.models import BaseModel


class StatementResponse(BaseModel):
    openapi_types = {
        "statement_id": "str",
        "start_date": "date",
        "end_date": "date",
        "imported_date_time_utc": "datetime",
        "import_source": "str",
        "start_balance": "float",
        "end_balance": "float",
        "indicative_start_balance": "float",
        "indicative_end_balance": "float",
        "statement_lines": "list[StatementLineResponse]",
    }
    attribute_map = {
        "statement_id": "statementId",
        "start_date": "startDate",
        "end_date": "endDate",
        "imported_date_time_utc": "importedDateTimeUtc",
        "import_source": "importSource",
        "start_balance": "startBalance",
        "end_balance": "endBalance",
        "indicative_start_balance": "indicativeStartBalance",
        "indicative_end_balance": "indicativeEndBalance",
        "statement_lines": "statementLines",
    }

    def __init__(
        self,
        statement_id=None,
        start_date=None,
        end_date=None,
        imported_date_time_utc=None,
        import_source=None,
        start_balance=None,
        end_balance=None,
        indicative_start_balance=None,
        indicative_end_balance=None,
        statement_lines=None,
    ):
        self._statement_id = None
        self._start_date = None
        self._end_date = None
        self._imported_date_time_utc = None
        self._import_source = None
        self._start_balance = None
        self._end_balance = None
        self._indicative_start_balance = None
        self._indicative_end_balance = None
        self._statement_lines = None
        self.discriminator = None
        if statement_id is not None:
            self.statement_id = statement_id
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if imported_date_time_utc is not None:
            self.imported_date_time_utc = imported_date_time_utc
        if import_source is not None:
            self.import_source = import_source
        if start_balance is not None:
            self.start_balance = start_balance
        if end_balance is not None:
            self.end_balance = end_balance
        if indicative_start_balance is not None:
            self.indicative_start_balance = indicative_start_balance
        if indicative_end_balance is not None:
            self.indicative_end_balance = indicative_end_balance
        if statement_lines is not None:
            self.statement_lines = statement_lines

    @property
    def statement_id(self):
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        self._statement_id = statement_id

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
    def imported_date_time_utc(self):
        return self._imported_date_time_utc

    @imported_date_time_utc.setter
    def imported_date_time_utc(self, imported_date_time_utc):
        self._imported_date_time_utc = imported_date_time_utc

    @property
    def import_source(self):
        return self._import_source

    @import_source.setter
    def import_source(self, import_source):
        self._import_source = import_source

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
    def indicative_start_balance(self):
        return self._indicative_start_balance

    @indicative_start_balance.setter
    def indicative_start_balance(self, indicative_start_balance):
        self._indicative_start_balance = indicative_start_balance

    @property
    def indicative_end_balance(self):
        return self._indicative_end_balance

    @indicative_end_balance.setter
    def indicative_end_balance(self, indicative_end_balance):
        self._indicative_end_balance = indicative_end_balance

    @property
    def statement_lines(self):
        return self._statement_lines

    @statement_lines.setter
    def statement_lines(self, statement_lines):
        self._statement_lines = statement_lines
