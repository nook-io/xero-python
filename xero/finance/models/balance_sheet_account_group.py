from xero.models import BaseModel


class BalanceSheetAccountGroup(BaseModel):
    openapi_types = {"account_types": "list[BalanceSheetAccountType]", "total": "float"}
    attribute_map = {"account_types": "accountTypes", "total": "total"}

    def __init__(self, account_types=None, total=None):
        self._account_types = None
        self._total = None
        self.discriminator = None
        if account_types is not None:
            self.account_types = account_types
        if total is not None:
            self.total = total

    @property
    def account_types(self):
        return self._account_types

    @account_types.setter
    def account_types(self, account_types):
        self._account_types = account_types

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total
