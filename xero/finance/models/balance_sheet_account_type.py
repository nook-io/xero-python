from xero.models import BaseModel


class BalanceSheetAccountType(BaseModel):
    openapi_types = {
        "account_type": "str",
        "accounts": "list[BalanceSheetAccountDetail]",
        "total": "float",
    }
    attribute_map = {
        "account_type": "accountType",
        "accounts": "accounts",
        "total": "total",
    }

    def __init__(self, account_type=None, accounts=None, total=None):
        self._account_type = None
        self._accounts = None
        self._total = None
        self.discriminator = None
        if account_type is not None:
            self.account_type = account_type
        if accounts is not None:
            self.accounts = accounts
        if total is not None:
            self.total = total

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        self._account_type = account_type

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total
