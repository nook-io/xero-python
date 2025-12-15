from xero.models import BaseModel


class ResourceValidationErrorsElement(BaseModel):
    openapi_types = {
        "resource_name": "str",
        "localised_message": "str",
        "type": "str",
        "title": "str",
        "detail": "str",
    }
    attribute_map = {
        "resource_name": "resourceName",
        "localised_message": "localisedMessage",
        "type": "type",
        "title": "title",
        "detail": "detail",
    }

    def __init__(
        self,
        resource_name=None,
        localised_message=None,
        type=None,
        title=None,
        detail=None,
    ):
        self._resource_name = None
        self._localised_message = None
        self._type = None
        self._title = None
        self._detail = None
        self.discriminator = None
        if resource_name is not None:
            self.resource_name = resource_name
        if localised_message is not None:
            self.localised_message = localised_message
        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if detail is not None:
            self.detail = detail

    @property
    def resource_name(self):
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        self._resource_name = resource_name

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
