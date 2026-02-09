from xero.models import BaseModel


class ReportWithRow(BaseModel):
    openapi_types = {
        "report_id": "str",
        "report_name": "str",
        "report_title": "str",
        "report_type": "str",
        "report_titles": "list[str]",
        "report_date": "str",
        "rows": "list[ReportRows]",
        "updated_date_utc": "datetime[ms-format]",
        "fields": "list[ReportFields]",
    }
    attribute_map = {
        "report_id": "ReportID",
        "report_name": "ReportName",
        "report_title": "ReportTitle",
        "report_type": "ReportType",
        "report_titles": "ReportTitles",
        "report_date": "ReportDate",
        "rows": "Rows",
        "updated_date_utc": "UpdatedDateUTC",
        "fields": "Fields",
    }

    def __init__(
        self,
        report_id=None,
        report_name=None,
        report_title=None,
        report_type=None,
        report_titles=None,
        report_date=None,
        rows=None,
        updated_date_utc=None,
        fields=None,
    ):
        self._report_id = None
        self._report_name = None
        self._report_title = None
        self._report_type = None
        self._report_titles = None
        self._report_date = None
        self._rows = None
        self._updated_date_utc = None
        self._fields = None
        self.discriminator = None
        if report_id is not None:
            self.report_id = report_id
        if report_name is not None:
            self.report_name = report_name
        if report_title is not None:
            self.report_title = report_title
        if report_type is not None:
            self.report_type = report_type
        if report_titles is not None:
            self.report_titles = report_titles
        if report_date is not None:
            self.report_date = report_date
        if rows is not None:
            self.rows = rows
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if fields is not None:
            self.fields = fields

    @property
    def report_id(self):
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        self._report_id = report_id

    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        self._report_name = report_name

    @property
    def report_title(self):
        return self._report_title

    @report_title.setter
    def report_title(self, report_title):
        self._report_title = report_title

    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        self._report_type = report_type

    @property
    def report_titles(self):
        return self._report_titles

    @report_titles.setter
    def report_titles(self, report_titles):
        self._report_titles = report_titles

    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, report_date):
        self._report_date = report_date

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, rows):
        self._rows = rows

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        self._fields = fields
