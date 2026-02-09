from xero.models import BaseModel


class CashBalance(BaseModel):
    openapi_types = {
        "opening_cash_balance": "float",
        "closing_cash_balance": "float",
        "net_cash_movement": "float",
    }
    attribute_map = {
        "opening_cash_balance": "openingCashBalance",
        "closing_cash_balance": "closingCashBalance",
        "net_cash_movement": "netCashMovement",
    }

    def __init__(
        self,
        opening_cash_balance=None,
        closing_cash_balance=None,
        net_cash_movement=None,
    ):
        self._opening_cash_balance = None
        self._closing_cash_balance = None
        self._net_cash_movement = None
        self.discriminator = None
        if opening_cash_balance is not None:
            self.opening_cash_balance = opening_cash_balance
        if closing_cash_balance is not None:
            self.closing_cash_balance = closing_cash_balance
        if net_cash_movement is not None:
            self.net_cash_movement = net_cash_movement

    @property
    def opening_cash_balance(self):
        return self._opening_cash_balance

    @opening_cash_balance.setter
    def opening_cash_balance(self, opening_cash_balance):
        self._opening_cash_balance = opening_cash_balance

    @property
    def closing_cash_balance(self):
        return self._closing_cash_balance

    @closing_cash_balance.setter
    def closing_cash_balance(self, closing_cash_balance):
        self._closing_cash_balance = closing_cash_balance

    @property
    def net_cash_movement(self):
        return self._net_cash_movement

    @net_cash_movement.setter
    def net_cash_movement(self, net_cash_movement):
        self._net_cash_movement = net_cash_movement
