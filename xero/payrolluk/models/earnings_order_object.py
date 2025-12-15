from xero.models import BaseModel


class EarningsOrderObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "statutory_deduction": "EarningsOrder",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "statutory_deduction": "statutoryDeduction",
    }

    def __init__(self, pagination=None, problem=None, statutory_deduction=None):
        self._pagination = None
        self._problem = None
        self._statutory_deduction = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if statutory_deduction is not None:
            self.statutory_deduction = statutory_deduction

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
    def statutory_deduction(self):
        return self._statutory_deduction

    @statutory_deduction.setter
    def statutory_deduction(self, statutory_deduction):
        self._statutory_deduction = statutory_deduction
