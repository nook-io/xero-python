from xero.models import BaseModel


class Files(BaseModel):
    openapi_types = {
        "total_count": "int",
        "page": "int",
        "per_page": "int",
        "items": "list[FileObject]",
    }
    attribute_map = {
        "total_count": "TotalCount",
        "page": "Page",
        "per_page": "PerPage",
        "items": "Items",
    }

    def __init__(self, total_count=None, page=None, per_page=None, items=None):
        self._total_count = None
        self._page = None
        self._per_page = None
        self._items = None
        self.discriminator = None
        if total_count is not None:
            self.total_count = total_count
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page
        if items is not None:
            self.items = items

    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        self._total_count = total_count

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, page):
        self._page = page

    @property
    def per_page(self):
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        self._per_page = per_page

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items
