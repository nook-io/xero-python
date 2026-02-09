from xero.models import BaseModel


class DeductionObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "deduction": "Deduction",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "deduction": "deduction",
    }

    def __init__(self, pagination=None, problem=None, deduction=None):
        self._pagination = None
        self._problem = None
        self._deduction = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if deduction is not None:
            self.deduction = deduction

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
    def deduction(self):
        return self._deduction

    @deduction.setter
    def deduction(self, deduction):
        self._deduction = deduction
