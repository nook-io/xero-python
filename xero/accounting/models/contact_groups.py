from xero.models import BaseModel


class ContactGroups(BaseModel):
    openapi_types = {"contact_groups": "list[ContactGroup]"}
    attribute_map = {"contact_groups": "ContactGroups"}

    def __init__(self, contact_groups=None):
        self._contact_groups = None
        self.discriminator = None
        if contact_groups is not None:
            self.contact_groups = contact_groups

    @property
    def contact_groups(self):
        return self._contact_groups

    @contact_groups.setter
    def contact_groups(self, contact_groups):
        self._contact_groups = contact_groups
