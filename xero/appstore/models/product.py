from xero.models import BaseModel


class Product(BaseModel):
    openapi_types = {
        "id": "str",
        "name": "str",
        "seat_unit": "str",
        "type": "str",
        "usage_unit": "str",
    }
    attribute_map = {
        "id": "id",
        "name": "name",
        "seat_unit": "seatUnit",
        "type": "type",
        "usage_unit": "usageUnit",
    }

    def __init__(self, id=None, name=None, seat_unit=None, type=None, usage_unit=None):
        self._id = None
        self._name = None
        self._seat_unit = None
        self._type = None
        self._usage_unit = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if seat_unit is not None:
            self.seat_unit = seat_unit
        if type is not None:
            self.type = type
        if usage_unit is not None:
            self.usage_unit = usage_unit

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def seat_unit(self):
        return self._seat_unit

    @seat_unit.setter
    def seat_unit(self, seat_unit):
        self._seat_unit = seat_unit

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_values = ["FIXED", "PER_SEAT", "METERED", "None"]
        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(
                        type, allowed_values
                    )
                )
        self._type = type

    @property
    def usage_unit(self):
        return self._usage_unit

    @usage_unit.setter
    def usage_unit(self, usage_unit):
        self._usage_unit = usage_unit
