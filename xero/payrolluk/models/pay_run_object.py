from xero.models import BaseModel


class PayRunObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "pay_run": "PayRun",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_run": "payRun",
    }

    def __init__(self, pagination=None, problem=None, pay_run=None):
        self._pagination = None
        self._problem = None
        self._pay_run = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_run is not None:
            self.pay_run = pay_run

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
    def pay_run(self):
        return self._pay_run

    @pay_run.setter
    def pay_run(self, pay_run):
        self._pay_run = pay_run
