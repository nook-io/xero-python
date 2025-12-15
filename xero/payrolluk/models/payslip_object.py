from xero.models import BaseModel


class PayslipObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "pay_slip": "Payslip",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_slip": "paySlip",
    }

    def __init__(self, pagination=None, problem=None, pay_slip=None):
        self._pagination = None
        self._problem = None
        self._pay_slip = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_slip is not None:
            self.pay_slip = pay_slip

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
    def pay_slip(self):
        return self._pay_slip

    @pay_slip.setter
    def pay_slip(self, pay_slip):
        self._pay_slip = pay_slip
