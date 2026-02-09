from xero.models import BaseModel


class Association(BaseModel):
    openapi_types = {
        "send_with_object": "bool",
        "name": "str",
        "size": "int",
        "file_id": "str",
        "object_id": "str",
        "object_group": "ObjectGroup",
        "object_type": "ObjectType",
    }
    attribute_map = {
        "send_with_object": "SendWithObject",
        "name": "Name",
        "size": "Size",
        "file_id": "FileId",
        "object_id": "ObjectId",
        "object_group": "ObjectGroup",
        "object_type": "ObjectType",
    }

    def __init__(
        self,
        send_with_object=None,
        name=None,
        size=None,
        file_id=None,
        object_id=None,
        object_group=None,
        object_type=None,
    ):
        self._send_with_object = None
        self._name = None
        self._size = None
        self._file_id = None
        self._object_id = None
        self._object_group = None
        self._object_type = None
        self.discriminator = None
        if send_with_object is not None:
            self.send_with_object = send_with_object
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if file_id is not None:
            self.file_id = file_id
        if object_id is not None:
            self.object_id = object_id
        if object_group is not None:
            self.object_group = object_group
        if object_type is not None:
            self.object_type = object_type

    @property
    def send_with_object(self):
        return self._send_with_object

    @send_with_object.setter
    def send_with_object(self, send_with_object):
        self._send_with_object = send_with_object

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        self._file_id = file_id

    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        self._object_id = object_id

    @property
    def object_group(self):
        return self._object_group

    @object_group.setter
    def object_group(self, object_group):
        self._object_group = object_group

    @property
    def object_type(self):
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        self._object_type = object_type
