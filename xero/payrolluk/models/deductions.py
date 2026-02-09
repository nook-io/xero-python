from xero.models import BaseModel


class Deductions(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "deductions": "list[Deduction]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "deductions": "deductions",
    }

    def __init__(self, pagination=None, problem=None, deductions=None):
        self._pagination = None
        self._problem = None
        self._deductions = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if deductions is not None:
            self.deductions = deductions

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
    def deductions(self):
        return self._deductions

    @deductions.setter
    def deductions(self, deductions):
        self._deductions = deductions
