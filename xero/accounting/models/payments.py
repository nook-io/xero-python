from xero.models import BaseModel


class Payments(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "warnings": "list[ValidationError]",
        "payments": "list[Payment]",
    }
    attribute_map = {
        "pagination": "pagination",
        "warnings": "Warnings",
        "payments": "Payments",
    }

    def __init__(self, pagination=None, warnings=None, payments=None):
        self._pagination = None
        self._warnings = None
        self._payments = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if warnings is not None:
            self.warnings = warnings
        if payments is not None:
            self.payments = payments

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
    def payments(self):
        return self._payments

    @payments.setter
    def payments(self, payments):
        self._payments = payments
