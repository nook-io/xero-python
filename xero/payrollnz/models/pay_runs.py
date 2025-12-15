from xero.models import BaseModel


class PayRuns(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "pay_runs": "list[PayRun]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_runs": "payRuns",
    }

    def __init__(self, pagination=None, problem=None, pay_runs=None):
        self._pagination = None
        self._problem = None
        self._pay_runs = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_runs is not None:
            self.pay_runs = pay_runs

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
    def pay_runs(self):
        return self._pay_runs

    @pay_runs.setter
    def pay_runs(self, pay_runs):
        self._pay_runs = pay_runs
