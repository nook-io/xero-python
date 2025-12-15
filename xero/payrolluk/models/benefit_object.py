from xero.models import BaseModel


class BenefitObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "benefit": "Benefit",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "benefit": "benefit",
    }

    def __init__(self, pagination=None, problem=None, benefit=None):
        self._pagination = None
        self._problem = None
        self._benefit = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if benefit is not None:
            self.benefit = benefit

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
    def benefit(self):
        return self._benefit

    @benefit.setter
    def benefit(self, benefit):
        self._benefit = benefit
