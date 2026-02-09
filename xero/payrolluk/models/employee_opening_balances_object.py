from xero.models import BaseModel


class EmployeeOpeningBalancesObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "opening_balances": "EmployeeOpeningBalances",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "opening_balances": "openingBalances",
    }

    def __init__(self, pagination=None, problem=None, opening_balances=None):
        self._pagination = None
        self._problem = None
        self._opening_balances = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if opening_balances is not None:
            self.opening_balances = opening_balances

    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        self._pagination = pagination

    @property
    def problem(self):
        return self._problem

    @problem.setter
    def problem(self, problem):
        self._problem = problem

    @property
    def opening_balances(self):
        return self._opening_balances

    @opening_balances.setter
    def opening_balances(self, opening_balances):
        self._opening_balances = opening_balances
