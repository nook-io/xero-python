from xero.models import BaseModel


class Folder(BaseModel):
    openapi_types = {
        "name": "str",
        "file_count": "int",
        "email": "str",
        "is_inbox": "bool",
        "id": "str",
    }
    attribute_map = {
        "name": "Name",
        "file_count": "FileCount",
        "email": "Email",
        "is_inbox": "IsInbox",
        "id": "Id",
    }

    def __init__(self, name=None, file_count=None, email=None, is_inbox=None, id=None):
        self._name = None
        self._file_count = None
        self._email = None
        self._is_inbox = None
        self._id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if file_count is not None:
            self.file_count = file_count
        if email is not None:
            self.email = email
        if is_inbox is not None:
            self.is_inbox = is_inbox
        if id is not None:
            self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def file_count(self):
        return self._file_count

    @file_count.setter
    def file_count(self, file_count):
        self._file_count = file_count

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def is_inbox(self):
        return self._is_inbox

    @is_inbox.setter
    def is_inbox(self, is_inbox):
        self._is_inbox = is_inbox

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
