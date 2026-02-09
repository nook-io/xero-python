from xero.models import BaseModel


class ReportAttribute(BaseModel):
    openapi_types = {"id": "str", "value": "str"}
    attribute_map = {"id": "Id", "value": "Value"}

    def __init__(self, id=None, value=None):
        self._id = None
        self._value = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if value is not None:
            self.value = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
