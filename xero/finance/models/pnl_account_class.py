from xero.models import BaseModel


class PnlAccountClass(BaseModel):
    openapi_types = {"total": "float", "account_types": "list[PnlAccountType]"}
    attribute_map = {"total": "total", "account_types": "accountTypes"}

    def __init__(self, total=None, account_types=None):
        self._total = None
        self._account_types = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if account_types is not None:
            self.account_types = account_types

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def account_types(self):
        return self._account_types

    @account_types.setter
    def account_types(self, account_types):
        self._account_types = account_types
