from xero.models import BaseModel


class Assets(BaseModel):
    openapi_types = {"pagination": "Pagination", "items": "list[Asset]"}
    attribute_map = {"pagination": "pagination", "items": "items"}

    def __init__(self, pagination=None, items=None):
        self._pagination = None
        self._items = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if items is not None:
            self.items = items

    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        self._pagination = pagination

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items
