from xero.models import BaseModel


class ProblemDetails(BaseModel):
    openapi_types = {
        "detail": "str",
        "extensions": "object",
        "instance": "str",
        "status": "int",
        "title": "str",
        "type": "str",
    }
    attribute_map = {
        "detail": "detail",
        "extensions": "extensions",
        "instance": "instance",
        "status": "status",
        "title": "title",
        "type": "type",
    }

    def __init__(
        self,
        detail=None,
        extensions=None,
        instance=None,
        status=None,
        title=None,
        type=None,
    ):
        self._detail = None
        self._extensions = None
        self._instance = None
        self._status = None
        self._title = None
        self._type = None
        self.discriminator = None
        if detail is not None:
            self.detail = detail
        if extensions is not None:
            self.extensions = extensions
        if instance is not None:
            self.instance = instance
        if status is not None:
            self.status = status
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, detail):
        self._detail = detail

    @property
    def extensions(self):
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        self._extensions = extensions

    @property
    def instance(self):
        return self._instance

    @instance.setter
    def instance(self, instance):
        self._instance = instance

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type
