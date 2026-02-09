from xero.models import BaseModel


class User(BaseModel):
    openapi_types = {
        "id": "str",
        "name": "str",
        "first_name": "str",
        "last_name": "str",
        "full_name": "str",
    }
    attribute_map = {
        "id": "Id",
        "name": "Name",
        "first_name": "FirstName",
        "last_name": "LastName",
        "full_name": "FullName",
    }

    def __init__(
        self, id=None, name=None, first_name=None, last_name=None, full_name=None
    ):
        self._id = None
        self._name = None
        self._first_name = None
        self._last_name = None
        self._full_name = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if full_name is not None:
            self.full_name = full_name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        self._full_name = full_name
