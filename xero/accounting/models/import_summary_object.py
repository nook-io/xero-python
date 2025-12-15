from xero.models import BaseModel


class ImportSummaryObject(BaseModel):
    openapi_types = {"import_summary": "ImportSummary"}
    attribute_map = {"import_summary": "ImportSummary"}

    def __init__(self, import_summary=None):
        self._import_summary = None
        self.discriminator = None
        if import_summary is not None:
            self.import_summary = import_summary

    @property
    def import_summary(self):
        return self._import_summary

    @import_summary.setter
    def import_summary(self, import_summary):
        self._import_summary = import_summary
