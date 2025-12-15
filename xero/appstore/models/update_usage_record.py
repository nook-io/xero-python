from xero.models import BaseModel


class UpdateUsageRecord(BaseModel):
    openapi_types = {"quantity": "int"}
    attribute_map = {"quantity": "quantity"}

    def __init__(self, quantity=None):
        self._quantity = None
        self.discriminator = None
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")
        self._quantity = quantity
