from xero.models import BaseModel


class Users(BaseModel):
    openapi_types = {"users": "list[User]"}
    attribute_map = {"users": "Users"}

    def __init__(self, users=None):
        self._users = None
        self.discriminator = None
        if users is not None:
            self.users = users

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, users):
        self._users = users
