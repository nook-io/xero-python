from xero.models import BaseModel


class User(BaseModel):
    openapi_types = {
        "user_id": "str",
        "email_address": "str",
        "first_name": "str",
        "last_name": "str",
        "updated_date_utc": "datetime[ms-format]",
        "is_subscriber": "bool",
        "organisation_role": "str",
    }
    attribute_map = {
        "user_id": "UserID",
        "email_address": "EmailAddress",
        "first_name": "FirstName",
        "last_name": "LastName",
        "updated_date_utc": "UpdatedDateUTC",
        "is_subscriber": "IsSubscriber",
        "organisation_role": "OrganisationRole",
    }

    def __init__(
        self,
        user_id=None,
        email_address=None,
        first_name=None,
        last_name=None,
        updated_date_utc=None,
        is_subscriber=None,
        organisation_role=None,
    ):
        self._user_id = None
        self._email_address = None
        self._first_name = None
        self._last_name = None
        self._updated_date_utc = None
        self._is_subscriber = None
        self._organisation_role = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if email_address is not None:
            self.email_address = email_address
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if is_subscriber is not None:
            self.is_subscriber = is_subscriber
        if organisation_role is not None:
            self.organisation_role = organisation_role

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        self._email_address = email_address

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
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def is_subscriber(self):
        return self._is_subscriber

    @is_subscriber.setter
    def is_subscriber(self, is_subscriber):
        self._is_subscriber = is_subscriber

    @property
    def organisation_role(self):
        return self._organisation_role

    @organisation_role.setter
    def organisation_role(self, organisation_role):
        allowed_values = [
            "READONLY",
            "INVOICEONLY",
            "STANDARD",
            "FINANCIALADVISER",
            "MANAGEDCLIENT",
            "CASHBOOKCLIENT",
            "UNKNOWN",
            "None",
        ]
        if organisation_role:
            if organisation_role not in allowed_values:
                raise ValueError(
                    "Invalid value for `organisation_role` ({0}), must be one of {1}".format(
                        organisation_role, allowed_values
                    )
                )
        self._organisation_role = organisation_role
