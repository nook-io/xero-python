from xero.models import BaseModel


class InvalidField(BaseModel):
    openapi_types = {"name": "str", "reason": "str"}
    attribute_map = {"name": "name", "reason": "reason"}

    def __init__(self, name=None, reason=None):
        self._name = None
        self._reason = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if reason is not None:
            self.reason = reason

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, reason):
        self._reason = reason
