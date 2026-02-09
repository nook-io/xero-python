from xero.models import BaseModel


class Accounts(BaseModel):
    openapi_types = {"accounts": "list[Account]"}
    attribute_map = {"accounts": "accounts"}

    def __init__(self, accounts=None):
        self._accounts = None
        self.discriminator = None
        if accounts is not None:
            self.accounts = accounts

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts
