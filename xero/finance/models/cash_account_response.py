from xero.models import BaseModel


class CashAccountResponse(BaseModel):
    openapi_types = {
        "unreconciled_amount_pos": "float",
        "unreconciled_amount_neg": "float",
        "starting_balance": "float",
        "account_balance": "float",
        "balance_currency": "str",
    }
    attribute_map = {
        "unreconciled_amount_pos": "unreconciledAmountPos",
        "unreconciled_amount_neg": "unreconciledAmountNeg",
        "starting_balance": "startingBalance",
        "account_balance": "accountBalance",
        "balance_currency": "balanceCurrency",
    }

    def __init__(
        self,
        unreconciled_amount_pos=None,
        unreconciled_amount_neg=None,
        starting_balance=None,
        account_balance=None,
        balance_currency=None,
    ):
        self._unreconciled_amount_pos = None
        self._unreconciled_amount_neg = None
        self._starting_balance = None
        self._account_balance = None
        self._balance_currency = None
        self.discriminator = None
        if unreconciled_amount_pos is not None:
            self.unreconciled_amount_pos = unreconciled_amount_pos
        if unreconciled_amount_neg is not None:
            self.unreconciled_amount_neg = unreconciled_amount_neg
        if starting_balance is not None:
            self.starting_balance = starting_balance
        if account_balance is not None:
            self.account_balance = account_balance
        if balance_currency is not None:
            self.balance_currency = balance_currency

    @property
    def unreconciled_amount_pos(self):
        return self._unreconciled_amount_pos

    @unreconciled_amount_pos.setter
    def unreconciled_amount_pos(self, unreconciled_amount_pos):
        self._unreconciled_amount_pos = unreconciled_amount_pos

    @property
    def unreconciled_amount_neg(self):
        return self._unreconciled_amount_neg

    @unreconciled_amount_neg.setter
    def unreconciled_amount_neg(self, unreconciled_amount_neg):
        self._unreconciled_amount_neg = unreconciled_amount_neg

    @property
    def starting_balance(self):
        return self._starting_balance

    @starting_balance.setter
    def starting_balance(self, starting_balance):
        self._starting_balance = starting_balance

    @property
    def account_balance(self):
        return self._account_balance

    @account_balance.setter
    def account_balance(self, account_balance):
        self._account_balance = account_balance

    @property
    def balance_currency(self):
        return self._balance_currency

    @balance_currency.setter
    def balance_currency(self, balance_currency):
        self._balance_currency = balance_currency
