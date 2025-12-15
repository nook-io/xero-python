from xero.models import BaseModel


class BalanceSheetResponse(BaseModel):
    openapi_types = {
        "balance_date": "date",
        "asset": "BalanceSheetAccountGroup",
        "liability": "BalanceSheetAccountGroup",
        "equity": "BalanceSheetAccountGroup",
    }
    attribute_map = {
        "balance_date": "balanceDate",
        "asset": "asset",
        "liability": "liability",
        "equity": "equity",
    }

    def __init__(self, balance_date=None, asset=None, liability=None, equity=None):
        self._balance_date = None
        self._asset = None
        self._liability = None
        self._equity = None
        self.discriminator = None
        if balance_date is not None:
            self.balance_date = balance_date
        if asset is not None:
            self.asset = asset
        if liability is not None:
            self.liability = liability
        if equity is not None:
            self.equity = equity

    @property
    def balance_date(self):
        return self._balance_date

    @balance_date.setter
    def balance_date(self, balance_date):
        self._balance_date = balance_date

    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self, asset):
        self._asset = asset

    @property
    def liability(self):
        return self._liability

    @liability.setter
    def liability(self, liability):
        self._liability = liability

    @property
    def equity(self):
        return self._equity

    @equity.setter
    def equity(self, equity):
        self._equity = equity
