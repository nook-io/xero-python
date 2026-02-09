from xero.models import BaseModel


class Items(BaseModel):
    openapi_types = {"items": "list[Item]"}
    attribute_map = {"items": "Items"}

    def __init__(self, items=None):
        self._items = None
        self.discriminator = None
        if items is not None:
            self.items = items

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items
