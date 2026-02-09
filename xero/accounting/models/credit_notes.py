from xero.models import BaseModel


class CreditNotes(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "warnings": "list[ValidationError]",
        "credit_notes": "list[CreditNote]",
    }
    attribute_map = {
        "pagination": "pagination",
        "warnings": "Warnings",
        "credit_notes": "CreditNotes",
    }

    def __init__(self, pagination=None, warnings=None, credit_notes=None):
        self._pagination = None
        self._warnings = None
        self._credit_notes = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if warnings is not None:
            self.warnings = warnings
        if credit_notes is not None:
            self.credit_notes = credit_notes

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
    def credit_notes(self):
        return self._credit_notes

    @credit_notes.setter
    def credit_notes(self, credit_notes):
        self._credit_notes = credit_notes
