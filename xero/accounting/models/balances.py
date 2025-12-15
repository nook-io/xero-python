from xero.models import BaseModel


class Balances(BaseModel):
    openapi_types = {
        "accounts_receivable": "AccountsReceivable",
        "accounts_payable": "AccountsPayable",
    }
    attribute_map = {
        "accounts_receivable": "AccountsReceivable",
        "accounts_payable": "AccountsPayable",
    }

    def __init__(self, accounts_receivable=None, accounts_payable=None):
        self._accounts_receivable = None
        self._accounts_payable = None
        self.discriminator = None
        if accounts_receivable is not None:
            self.accounts_receivable = accounts_receivable
        if accounts_payable is not None:
            self.accounts_payable = accounts_payable

    @property
    def accounts_receivable(self):
        return self._accounts_receivable

    @accounts_receivable.setter
    def accounts_receivable(self, accounts_receivable):
        self._accounts_receivable = accounts_receivable

    @property
    def accounts_payable(self):
        return self._accounts_payable

    @accounts_payable.setter
    def accounts_payable(self, accounts_payable):
        self._accounts_payable = accounts_payable
