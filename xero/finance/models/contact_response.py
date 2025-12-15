from xero.models import BaseModel


class ContactResponse(BaseModel):
    openapi_types = {"contact_id": "str", "contact_name": "str"}
    attribute_map = {"contact_id": "contactId", "contact_name": "contactName"}

    def __init__(self, contact_id=None, contact_name=None):
        self._contact_id = None
        self._contact_name = None
        self.discriminator = None
        if contact_id is not None:
            self.contact_id = contact_id
        if contact_name is not None:
            self.contact_name = contact_name

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        self._contact_name = contact_name
