from xero.models import BaseModel


class StatementBalanceResponse(BaseModel):
    openapi_types = {"value": "float", "type": "str"}
    attribute_map = {"value": "value", "type": "type"}

    def __init__(self, value=None, type=None):
        self._value = None
        self._type = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type
