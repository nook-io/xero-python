from xero.models import BaseModel


class ContactGroup(BaseModel):
    openapi_types = {
        "name": "str",
        "status": "str",
        "contact_group_id": "str",
        "contacts": "list[Contact]",
    }
    attribute_map = {
        "name": "Name",
        "status": "Status",
        "contact_group_id": "ContactGroupID",
        "contacts": "Contacts",
    }

    def __init__(self, name=None, status=None, contact_group_id=None, contacts=None):
        self._name = None
        self._status = None
        self._contact_group_id = None
        self._contacts = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if contact_group_id is not None:
            self.contact_group_id = contact_group_id
        if contacts is not None:
            self.contacts = contacts

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["ACTIVE", "DELETED", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def contact_group_id(self):
        return self._contact_group_id

    @contact_group_id.setter
    def contact_group_id(self, contact_group_id):
        self._contact_group_id = contact_group_id

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        self._contacts = contacts
