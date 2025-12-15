from xero.models import BaseModel


class Problem(BaseModel):
    openapi_types = {
        "type": "ProblemType",
        "title": "str",
        "status": "int",
        "detail": "str",
    }
    attribute_map = {
        "type": "type",
        "title": "title",
        "status": "status",
        "detail": "detail",
    }

    def __init__(self, type=None, title=None, status=None, detail=None):
        self._type = None
        self._title = None
        self._status = None
        self._detail = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail

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
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, detail):
        self._detail = detail
