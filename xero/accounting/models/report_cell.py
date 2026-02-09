from xero.models import BaseModel


class ReportCell(BaseModel):
    openapi_types = {"value": "str", "attributes": "list[ReportAttribute]"}
    attribute_map = {"value": "Value", "attributes": "Attributes"}

    def __init__(self, value=None, attributes=None):
        self._value = None
        self._attributes = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if attributes is not None:
            self.attributes = attributes

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        self._attributes = attributes
