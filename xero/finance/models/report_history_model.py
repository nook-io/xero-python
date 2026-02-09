from xero.models import BaseModel


class ReportHistoryModel(BaseModel):
    openapi_types = {
        "report_name": "str",
        "report_date_text": "str",
        "published_date_utc": "datetime",
    }
    attribute_map = {
        "report_name": "reportName",
        "report_date_text": "reportDateText",
        "published_date_utc": "publishedDateUtc",
    }

    def __init__(
        self, report_name=None, report_date_text=None, published_date_utc=None
    ):
        self._report_name = None
        self._report_date_text = None
        self._published_date_utc = None
        self.discriminator = None
        if report_name is not None:
            self.report_name = report_name
        if report_date_text is not None:
            self.report_date_text = report_date_text
        if published_date_utc is not None:
            self.published_date_utc = published_date_utc

    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        self._report_name = report_name

    @property
    def report_date_text(self):
        return self._report_date_text

    @report_date_text.setter
    def report_date_text(self, report_date_text):
        self._report_date_text = report_date_text

    @property
    def published_date_utc(self):
        return self._published_date_utc

    @published_date_utc.setter
    def published_date_utc(self, published_date_utc):
        self._published_date_utc = published_date_utc
