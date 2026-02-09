from xero.models import BaseModel


class Overpayments(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "warnings": "list[ValidationError]",
        "overpayments": "list[Overpayment]",
    }
    attribute_map = {
        "pagination": "pagination",
        "warnings": "Warnings",
        "overpayments": "Overpayments",
    }

    def __init__(self, pagination=None, warnings=None, overpayments=None):
        self._pagination = None
        self._warnings = None
        self._overpayments = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if warnings is not None:
            self.warnings = warnings
        if overpayments is not None:
            self.overpayments = overpayments

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
    def overpayments(self):
        return self._overpayments

    @overpayments.setter
    def overpayments(self, overpayments):
        self._overpayments = overpayments
