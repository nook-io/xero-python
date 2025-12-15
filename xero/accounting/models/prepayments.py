from xero.models import BaseModel


class Prepayments(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "warnings": "list[ValidationError]",
        "prepayments": "list[Prepayment]",
    }
    attribute_map = {
        "pagination": "pagination",
        "warnings": "Warnings",
        "prepayments": "Prepayments",
    }

    def __init__(self, pagination=None, warnings=None, prepayments=None):
        self._pagination = None
        self._warnings = None
        self._prepayments = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if warnings is not None:
            self.warnings = warnings
        if prepayments is not None:
            self.prepayments = prepayments

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
    def prepayments(self):
        return self._prepayments

    @prepayments.setter
    def prepayments(self, prepayments):
        self._prepayments = prepayments
