from xero.models import BaseModel


class Payslips(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "pay_slips": "list[Payslip]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_slips": "paySlips",
    }

    def __init__(self, pagination=None, problem=None, pay_slips=None):
        self._pagination = None
        self._problem = None
        self._pay_slips = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_slips is not None:
            self.pay_slips = pay_slips

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
    def pay_slips(self):
        return self._pay_slips

    @pay_slips.setter
    def pay_slips(self, pay_slips):
        self._pay_slips = pay_slips
