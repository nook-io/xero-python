from xero.models import BaseModel


class TaxComponent(BaseModel):
    openapi_types = {
        "name": "str",
        "rate": "float",
        "is_compound": "bool",
        "is_non_recoverable": "bool",
    }
    attribute_map = {
        "name": "Name",
        "rate": "Rate",
        "is_compound": "IsCompound",
        "is_non_recoverable": "IsNonRecoverable",
    }

    def __init__(self, name=None, rate=None, is_compound=None, is_non_recoverable=None):
        self._name = None
        self._rate = None
        self._is_compound = None
        self._is_non_recoverable = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if rate is not None:
            self.rate = rate
        if is_compound is not None:
            self.is_compound = is_compound
        if is_non_recoverable is not None:
            self.is_non_recoverable = is_non_recoverable

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        self._rate = rate

    @property
    def is_compound(self):
        return self._is_compound

    @is_compound.setter
    def is_compound(self, is_compound):
        self._is_compound = is_compound

    @property
    def is_non_recoverable(self):
        return self._is_non_recoverable

    @is_non_recoverable.setter
    def is_non_recoverable(self, is_non_recoverable):
        self._is_non_recoverable = is_non_recoverable
