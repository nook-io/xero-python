from xero.models import BaseModel


class Error(BaseModel):
    openapi_types = {
        "resource_validation_errors": "list[ResourceValidationErrorsElement]",
        "field_validation_errors": "list[FieldValidationErrorsElement]",
        "type": "str",
        "title": "str",
        "detail": "str",
    }
    attribute_map = {
        "resource_validation_errors": "resourceValidationErrors",
        "field_validation_errors": "fieldValidationErrors",
        "type": "type",
        "title": "title",
        "detail": "detail",
    }

    def __init__(
        self,
        resource_validation_errors=None,
        field_validation_errors=None,
        type=None,
        title=None,
        detail=None,
    ):
        self._resource_validation_errors = None
        self._field_validation_errors = None
        self._type = None
        self._title = None
        self._detail = None
        self.discriminator = None
        if resource_validation_errors is not None:
            self.resource_validation_errors = resource_validation_errors
        if field_validation_errors is not None:
            self.field_validation_errors = field_validation_errors
        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if detail is not None:
            self.detail = detail

    @property
    def resource_validation_errors(self):
        return self._resource_validation_errors

    @resource_validation_errors.setter
    def resource_validation_errors(self, resource_validation_errors):
        self._resource_validation_errors = resource_validation_errors

    @property
    def field_validation_errors(self):
        return self._field_validation_errors

    @field_validation_errors.setter
    def field_validation_errors(self, field_validation_errors):
        self._field_validation_errors = field_validation_errors

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
