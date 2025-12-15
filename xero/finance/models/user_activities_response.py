from xero.models import BaseModel


class UserActivitiesResponse(BaseModel):
    openapi_types = {
        "organisation_id": "str",
        "data_month": "str",
        "users": "list[UserResponse]",
    }
    attribute_map = {
        "organisation_id": "organisationId",
        "data_month": "dataMonth",
        "users": "users",
    }

    def __init__(self, organisation_id=None, data_month=None, users=None):
        self._organisation_id = None
        self._data_month = None
        self._users = None
        self.discriminator = None
        if organisation_id is not None:
            self.organisation_id = organisation_id
        if data_month is not None:
            self.data_month = data_month
        if users is not None:
            self.users = users

    @property
    def organisation_id(self):
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        self._organisation_id = organisation_id

    @property
    def data_month(self):
        return self._data_month

    @data_month.setter
    def data_month(self, data_month):
        self._data_month = data_month

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, users):
        self._users = users
