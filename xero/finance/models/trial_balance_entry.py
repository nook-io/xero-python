from xero.models import BaseModel


class TrialBalanceEntry(BaseModel):
    openapi_types = {"value": "float", "entry_type": "str"}
    attribute_map = {"value": "value", "entry_type": "entryType"}

    def __init__(self, value=None, entry_type=None):
        self._value = None
        self._entry_type = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if entry_type is not None:
            self.entry_type = entry_type

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def entry_type(self):
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        self._entry_type = entry_type
