from xero.models import BaseModel


class BudgetLine(BaseModel):
    openapi_types = {
        "account_id": "str",
        "account_code": "str",
        "budget_balances": "list[BudgetBalance]",
    }
    attribute_map = {
        "account_id": "AccountID",
        "account_code": "AccountCode",
        "budget_balances": "BudgetBalances",
    }

    def __init__(self, account_id=None, account_code=None, budget_balances=None):
        self._account_id = None
        self._account_code = None
        self._budget_balances = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if account_code is not None:
            self.account_code = account_code
        if budget_balances is not None:
            self.budget_balances = budget_balances

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def account_code(self):
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        self._account_code = account_code

    @property
    def budget_balances(self):
        return self._budget_balances

    @budget_balances.setter
    def budget_balances(self, budget_balances):
        self._budget_balances = budget_balances
