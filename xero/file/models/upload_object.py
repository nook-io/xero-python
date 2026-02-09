from xero.models import BaseModel


class UploadObject(BaseModel):
    openapi_types = {
        "body": "str",
        "name": "str",
        "filename": "str",
        "mime_type": "str",
    }
    attribute_map = {
        "body": "body",
        "name": "name",
        "filename": "filename",
        "mime_type": "mimeType",
    }

    def __init__(self, body=None, name=None, filename=None, mime_type=None):
        self._body = None
        self._name = None
        self._filename = None
        self._mime_type = None
        self.discriminator = None
        self.body = body
        self.name = name
        self.filename = filename
        if mime_type is not None:
            self.mime_type = mime_type

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")
        self._body = body

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")
        self._filename = filename

    @property
    def mime_type(self):
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        self._mime_type = mime_type
