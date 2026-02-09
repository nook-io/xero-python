from xero.models import BaseModel


class Attachment(BaseModel):
    openapi_types = {
        "attachment_id": "str",
        "file_name": "str",
        "url": "str",
        "mime_type": "str",
        "content_length": "int",
        "include_online": "bool",
    }
    attribute_map = {
        "attachment_id": "AttachmentID",
        "file_name": "FileName",
        "url": "Url",
        "mime_type": "MimeType",
        "content_length": "ContentLength",
        "include_online": "IncludeOnline",
    }

    def __init__(
        self,
        attachment_id=None,
        file_name=None,
        url=None,
        mime_type=None,
        content_length=None,
        include_online=None,
    ):
        self._attachment_id = None
        self._file_name = None
        self._url = None
        self._mime_type = None
        self._content_length = None
        self._include_online = None
        self.discriminator = None
        if attachment_id is not None:
            self.attachment_id = attachment_id
        if file_name is not None:
            self.file_name = file_name
        if url is not None:
            self.url = url
        if mime_type is not None:
            self.mime_type = mime_type
        if content_length is not None:
            self.content_length = content_length
        if include_online is not None:
            self.include_online = include_online

    @property
    def attachment_id(self):
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        self._attachment_id = attachment_id

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        self._file_name = file_name

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def mime_type(self):
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        self._mime_type = mime_type

    @property
    def content_length(self):
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        self._content_length = content_length

    @property
    def include_online(self):
        return self._include_online

    @include_online.setter
    def include_online(self, include_online):
        self._include_online = include_online
