from xero.models import BaseModel


class ContactPerson(BaseModel):
    openapi_types = {
        "first_name": "str",
        "last_name": "str",
        "email_address": "str",
        "include_in_emails": "bool",
    }
    attribute_map = {
        "first_name": "FirstName",
        "last_name": "LastName",
        "email_address": "EmailAddress",
        "include_in_emails": "IncludeInEmails",
    }

    def __init__(
        self,
        first_name=None,
        last_name=None,
        email_address=None,
        include_in_emails=None,
    ):
        self._first_name = None
        self._last_name = None
        self._email_address = None
        self._include_in_emails = None
        self.discriminator = None
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email_address is not None:
            self.email_address = email_address
        if include_in_emails is not None:
            self.include_in_emails = include_in_emails

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
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        self._email_address = email_address

    @property
    def include_in_emails(self):
        return self._include_in_emails

    @include_in_emails.setter
    def include_in_emails(self, include_in_emails):
        self._include_in_emails = include_in_emails
