from xero.models import BaseModel


class Reports(BaseModel):
    openapi_types = {"reports": "list[Report]"}
    attribute_map = {"reports": "Reports"}

    def __init__(self, reports=None):
        self._reports = None
        self.discriminator = None
        if reports is not None:
            self.reports = reports

    @property
    def reports(self):
        return self._reports

    @reports.setter
    def reports(self, reports):
        self._reports = reports
