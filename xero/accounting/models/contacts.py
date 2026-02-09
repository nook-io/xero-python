from xero.models import BaseModel


class Contacts(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "warnings": "list[ValidationError]",
        "contacts": "list[Contact]",
    }
    attribute_map = {
        "pagination": "pagination",
        "warnings": "Warnings",
        "contacts": "Contacts",
    }

    def __init__(self, pagination=None, warnings=None, contacts=None):
        self._pagination = None
        self._warnings = None
        self._contacts = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if warnings is not None:
            self.warnings = warnings
        if contacts is not None:
            self.contacts = contacts

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
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        self._contacts = contacts
