from xero.models import BaseModel


class EmployeeStatutoryLeaveBalanceObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "leave_balance": "EmployeeStatutoryLeaveBalance",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "leave_balance": "leaveBalance",
    }

    def __init__(self, pagination=None, problem=None, leave_balance=None):
        self._pagination = None
        self._problem = None
        self._leave_balance = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave_balance is not None:
            self.leave_balance = leave_balance

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
    def leave_balance(self):
        return self._leave_balance

    @leave_balance.setter
    def leave_balance(self, leave_balance):
        self._leave_balance = leave_balance
