from xero.models import BaseModel


class FieldValidationErrorsElement(BaseModel):
    openapi_types = {
        "field_name": "str",
        "value_provided": "str",
        "localised_message": "str",
        "type": "str",
        "title": "str",
        "detail": "str",
    }
    attribute_map = {
        "field_name": "fieldName",
        "value_provided": "valueProvided",
        "localised_message": "localisedMessage",
        "type": "type",
        "title": "title",
        "detail": "detail",
    }

    def __init__(
        self,
        field_name=None,
        value_provided=None,
        localised_message=None,
        type=None,
        title=None,
        detail=None,
    ):
        self._field_name = None
        self._value_provided = None
        self._localised_message = None
        self._type = None
        self._title = None
        self._detail = None
        self.discriminator = None
        if field_name is not None:
            self.field_name = field_name
        if value_provided is not None:
            self.value_provided = value_provided
        if localised_message is not None:
            self.localised_message = localised_message
        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if detail is not None:
            self.detail = detail

    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        self._field_name = field_name

    @property
    def value_provided(self):
        return self._value_provided

    @value_provided.setter
    def value_provided(self, value_provided):
        self._value_provided = value_provided

    @property
    def localised_message(self):
        return self._localised_message

    @localised_message.setter
    def localised_message(self, localised_message):
        self._localised_message = localised_message

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, detail):
        self._detail = detail
