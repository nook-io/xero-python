from xero.models import BaseModel


class EarningsOrders(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "statutory_deductions": "list[EarningsOrder]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "statutory_deductions": "statutoryDeductions",
    }

    def __init__(self, pagination=None, problem=None, statutory_deductions=None):
        self._pagination = None
        self._problem = None
        self._statutory_deductions = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if statutory_deductions is not None:
            self.statutory_deductions = statutory_deductions

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
    def statutory_deductions(self):
        return self._statutory_deductions

    @statutory_deductions.setter
    def statutory_deductions(self, statutory_deductions):
        self._statutory_deductions = statutory_deductions
