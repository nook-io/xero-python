from xero.models import BaseModel


class CreateUsageRecord(BaseModel):
    openapi_types = {"quantity": "int", "timestamp": "datetime"}
    attribute_map = {"quantity": "quantity", "timestamp": "timestamp"}

    def __init__(self, quantity=None, timestamp=None):
        self._quantity = None
        self._timestamp = None
        self.discriminator = None
        self.quantity = quantity
        self.timestamp = timestamp

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")
        self._quantity = quantity

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")
        self._timestamp = timestamp
