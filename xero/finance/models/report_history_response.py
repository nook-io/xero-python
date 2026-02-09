from xero.models import BaseModel


class ReportHistoryResponse(BaseModel):
    openapi_types = {
        "organisation_id": "str",
        "end_date": "date",
        "reports": "list[ReportHistoryModel]",
    }
    attribute_map = {
        "organisation_id": "organisationId",
        "end_date": "endDate",
        "reports": "reports",
    }

    def __init__(self, organisation_id=None, end_date=None, reports=None):
        self._organisation_id = None
        self._end_date = None
        self._reports = None
        self.discriminator = None
        if organisation_id is not None:
            self.organisation_id = organisation_id
        if end_date is not None:
            self.end_date = end_date
        if reports is not None:
            self.reports = reports

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
    def reports(self):
        return self._reports

    @reports.setter
    def reports(self, reports):
        self._reports = reports
