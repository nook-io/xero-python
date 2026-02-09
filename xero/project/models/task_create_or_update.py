from xero.models import BaseModel


class TaskCreateOrUpdate(BaseModel):
    openapi_types = {
        "name": "str",
        "rate": "Amount",
        "charge_type": "ChargeType",
        "estimate_minutes": "int",
    }
    attribute_map = {
        "name": "name",
        "rate": "rate",
        "charge_type": "chargeType",
        "estimate_minutes": "estimateMinutes",
    }

    def __init__(self, name=None, rate=None, charge_type=None, estimate_minutes=None):
        self._name = None
        self._rate = None
        self._charge_type = None
        self._estimate_minutes = None
        self.discriminator = None
        self.name = name
        self.rate = rate
        self.charge_type = charge_type
        if estimate_minutes is not None:
            self.estimate_minutes = estimate_minutes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")
        self._rate = rate

    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        if charge_type is None:
            raise ValueError("Invalid value for `charge_type`, must not be `None`")
        self._charge_type = charge_type

    @property
    def estimate_minutes(self):
        return self._estimate_minutes

    @estimate_minutes.setter
    def estimate_minutes(self, estimate_minutes):
        self._estimate_minutes = estimate_minutes
