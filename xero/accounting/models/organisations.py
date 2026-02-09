from xero.models import BaseModel


class Organisations(BaseModel):
    openapi_types = {"organisations": "list[Organisation]"}
    attribute_map = {"organisations": "Organisations"}

    def __init__(self, organisations=None):
        self._organisations = None
        self.discriminator = None
        if organisations is not None:
            self.organisations = organisations

    @property
    def organisations(self):
        return self._organisations

    @organisations.setter
    def organisations(self, organisations):
        self._organisations = organisations
