from xero.models import BaseModel


class Invoices(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "warnings": "list[ValidationError]",
        "invoices": "list[Invoice]",
    }
    attribute_map = {
        "pagination": "pagination",
        "warnings": "Warnings",
        "invoices": "Invoices",
    }

    def __init__(self, pagination=None, warnings=None, invoices=None):
        self._pagination = None
        self._warnings = None
        self._invoices = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if warnings is not None:
            self.warnings = warnings
        if invoices is not None:
            self.invoices = invoices

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
    def invoices(self):
        return self._invoices

    @invoices.setter
    def invoices(self, invoices):
        self._invoices = invoices
