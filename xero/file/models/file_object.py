from xero.models import BaseModel


class FileObject(BaseModel):
    openapi_types = {
        "name": "str",
        "mime_type": "str",
        "size": "int",
        "created_date_utc": "str",
        "updated_date_utc": "str",
        "user": "User",
        "id": "str",
        "folder_id": "str",
    }
    attribute_map = {
        "name": "Name",
        "mime_type": "MimeType",
        "size": "Size",
        "created_date_utc": "CreatedDateUtc",
        "updated_date_utc": "UpdatedDateUtc",
        "user": "User",
        "id": "Id",
        "folder_id": "FolderId",
    }

    def __init__(
        self,
        name=None,
        mime_type=None,
        size=None,
        created_date_utc=None,
        updated_date_utc=None,
        user=None,
        id=None,
        folder_id=None,
    ):
        self._name = None
        self._mime_type = None
        self._size = None
        self._created_date_utc = None
        self._updated_date_utc = None
        self._user = None
        self._id = None
        self._folder_id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if mime_type is not None:
            self.mime_type = mime_type
        if size is not None:
            self.size = size
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if user is not None:
            self.user = user
        if id is not None:
            self.id = id
        if folder_id is not None:
            self.folder_id = folder_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def mime_type(self):
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        self._mime_type = mime_type

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def created_date_utc(self):
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        self._created_date_utc = created_date_utc

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def folder_id(self):
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        self._folder_id = folder_id
