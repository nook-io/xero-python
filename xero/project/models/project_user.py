from xero.models import BaseModel


class ProjectUser(BaseModel):
    openapi_types = {"user_id": "str", "name": "str", "email": "str"}
    attribute_map = {"user_id": "userId", "name": "name", "email": "email"}

    def __init__(self, user_id=None, name=None, email=None):
        self._user_id = None
        self._name = None
        self._email = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
