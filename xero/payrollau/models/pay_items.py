from xero.models import BaseModel


class PayItems(BaseModel):
    openapi_types = {"pay_items": "PayItem"}
    attribute_map = {"pay_items": "PayItems"}

    def __init__(self, pay_items=None):
        self._pay_items = None
        self.discriminator = None
        if pay_items is not None:
            self.pay_items = pay_items

    @property
    def pay_items(self):
        return self._pay_items

    @pay_items.setter
    def pay_items(self, pay_items):
        self._pay_items = pay_items
