from xero.models import BaseModel


class Report(BaseModel):
    openapi_types = {
        "report_name": "str",
        "report_type": "str",
        "report_title": "str",
        "report_date": "str",
        "updated_date_utc": "datetime[ms-format]",
        "contacts": "list[TenNinetyNineContact]",
    }
    attribute_map = {
        "report_name": "ReportName",
        "report_type": "ReportType",
        "report_title": "ReportTitle",
        "report_date": "ReportDate",
        "updated_date_utc": "UpdatedDateUTC",
        "contacts": "Contacts",
    }

    def __init__(
        self,
        report_name=None,
        report_type=None,
        report_title=None,
        report_date=None,
        updated_date_utc=None,
        contacts=None,
    ):
        self._report_name = None
        self._report_type = None
        self._report_title = None
        self._report_date = None
        self._updated_date_utc = None
        self._contacts = None
        self.discriminator = None
        if report_name is not None:
            self.report_name = report_name
        if report_type is not None:
            self.report_type = report_type
        if report_title is not None:
            self.report_title = report_title
        if report_date is not None:
            self.report_date = report_date
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if contacts is not None:
            self.contacts = contacts

    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        self._report_name = report_name

    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        allowed_values = ["AgedPayablesByContact", "None"]
        if report_type:
            if report_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `report_type` ({0}), must be one of {1}".format(
                        report_type, allowed_values
                    )
                )
        self._report_type = report_type

    @property
    def report_title(self):
        return self._report_title

    @report_title.setter
    def report_title(self, report_title):
        self._report_title = report_title

    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, report_date):
        self._report_date = report_date

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        self._contacts = contacts
