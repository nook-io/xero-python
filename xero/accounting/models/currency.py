from xero.models import BaseModel


class Currency(BaseModel):
    openapi_types = {"code": "CurrencyCode", "description": "str"}
    attribute_map = {"code": "Code", "description": "Description"}

    def __init__(self, code=None, description=None):
        self._code = None
        self._description = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if description is not None:
            self.description = description

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description
