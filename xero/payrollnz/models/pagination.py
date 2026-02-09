from xero.models import BaseModel


class Pagination(BaseModel):
    openapi_types = {
        "page": "int",
        "page_size": "int",
        "page_count": "int",
        "item_count": "int",
    }
    attribute_map = {
        "page": "page",
        "page_size": "pageSize",
        "page_count": "pageCount",
        "item_count": "itemCount",
    }

    def __init__(self, page=None, page_size=None, page_count=None, item_count=None):
        self._page = None
        self._page_size = None
        self._page_count = None
        self._item_count = None
        self.discriminator = None
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if page_count is not None:
            self.page_count = page_count
        if item_count is not None:
            self.item_count = item_count

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, page):
        self._page = page

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        self._page_size = page_size

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        self._page_count = page_count

    @property
    def item_count(self):
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        self._item_count = item_count
