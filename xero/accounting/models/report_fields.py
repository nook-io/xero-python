from xero.models import BaseModel


class ReportFields(BaseModel):
    openapi_types = {"field_id": "str", "description": "str", "value": "str"}
    attribute_map = {
        "field_id": "FieldID",
        "description": "Description",
        "value": "Value",
    }

    def __init__(self, field_id=None, description=None, value=None):
        self._field_id = None
        self._description = None
        self._value = None
        self.discriminator = None
        if field_id is not None:
            self.field_id = field_id
        if description is not None:
            self.description = description
        if value is not None:
            self.value = value

    @property
    def field_id(self):
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        self._field_id = field_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
