from xero.models import BaseModel


class PnlAccountType(BaseModel):
    openapi_types = {"total": "float", "title": "str", "accounts": "list[PnlAccount]"}
    attribute_map = {"total": "total", "title": "title", "accounts": "accounts"}

    def __init__(self, total=None, title=None, accounts=None):
        self._total = None
        self._title = None
        self._accounts = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if title is not None:
            self.title = title
        if accounts is not None:
            self.accounts = accounts

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts
