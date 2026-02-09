from xero.models import BaseModel


class PageInfo(BaseModel):
    openapi_types = {
        "page": "int",
        "page_size": "int",
        "total_pages": "int",
        "total_rows": "int",
    }
    attribute_map = {
        "page": "Page",
        "page_size": "PageSize",
        "total_pages": "TotalPages",
        "total_rows": "TotalRows",
    }

    def __init__(self, page=None, page_size=None, total_pages=None, total_rows=None):
        self._page = None
        self._page_size = None
        self._total_pages = None
        self._total_rows = None
        self.discriminator = None
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total_pages is not None:
            self.total_pages = total_pages
        if total_rows is not None:
            self.total_rows = total_rows

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
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        self._total_pages = total_pages

    @property
    def total_rows(self):
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        self._total_rows = total_rows
