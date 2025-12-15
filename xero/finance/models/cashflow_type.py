from xero.models import BaseModel


class CashflowType(BaseModel):
    openapi_types = {
        "name": "str",
        "total": "float",
        "accounts": "list[CashflowAccount]",
    }
    attribute_map = {"name": "name", "total": "total", "accounts": "accounts"}

    def __init__(self, name=None, total=None, accounts=None):
        self._name = None
        self._total = None
        self._accounts = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if total is not None:
            self.total = total
        if accounts is not None:
            self.accounts = accounts

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts
