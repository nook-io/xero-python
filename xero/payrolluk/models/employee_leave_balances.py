from xero.models import BaseModel


class EmployeeLeaveBalances(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "leave_balances": "list[EmployeeLeaveBalance]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "leave_balances": "leaveBalances",
    }

    def __init__(self, pagination=None, problem=None, leave_balances=None):
        self._pagination = None
        self._problem = None
        self._leave_balances = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave_balances is not None:
            self.leave_balances = leave_balances

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
    def leave_balances(self):
        return self._leave_balances

    @leave_balances.setter
    def leave_balances(self, leave_balances):
        self._leave_balances = leave_balances
