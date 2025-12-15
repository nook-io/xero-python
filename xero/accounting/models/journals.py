from xero.models import BaseModel


class Journals(BaseModel):
    openapi_types = {"warnings": "list[ValidationError]", "journals": "list[Journal]"}
    attribute_map = {"warnings": "Warnings", "journals": "Journals"}

    def __init__(self, warnings=None, journals=None):
        self._warnings = None
        self._journals = None
        self.discriminator = None
        if warnings is not None:
            self.warnings = warnings
        if journals is not None:
            self.journals = journals

    @property
    def warnings(self):
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        self._warnings = warnings

    @property
    def journals(self):
        return self._journals

    @journals.setter
    def journals(self, journals):
        self._journals = journals
