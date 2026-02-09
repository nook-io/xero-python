from xero.models import BaseModel


class ManualJournals(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "warnings": "list[ValidationError]",
        "manual_journals": "list[ManualJournal]",
    }
    attribute_map = {
        "pagination": "pagination",
        "warnings": "Warnings",
        "manual_journals": "ManualJournals",
    }

    def __init__(self, pagination=None, warnings=None, manual_journals=None):
        self._pagination = None
        self._warnings = None
        self._manual_journals = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if warnings is not None:
            self.warnings = warnings
        if manual_journals is not None:
            self.manual_journals = manual_journals

    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        self._pagination = pagination

    @property
    def warnings(self):
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        self._warnings = warnings

    @property
    def manual_journals(self):
        return self._manual_journals

    @manual_journals.setter
    def manual_journals(self, manual_journals):
        self._manual_journals = manual_journals
