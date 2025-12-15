from xero.models import BaseModel


class Bill(BaseModel):
    openapi_types = {"day": "int", "type": "PaymentTermType"}
    attribute_map = {"day": "Day", "type": "Type"}

    def __init__(self, day=None, type=None):
        self._day = None
        self._type = None
        self.discriminator = None
        if day is not None:
            self.day = day
        if type is not None:
            self.type = type

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        self._day = day

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type
