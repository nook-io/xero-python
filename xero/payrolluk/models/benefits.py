from xero.models import BaseModel


class Benefits(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "benefits": "list[Benefit]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "benefits": "benefits",
    }

    def __init__(self, pagination=None, problem=None, benefits=None):
        self._pagination = None
        self._problem = None
        self._benefits = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if benefits is not None:
            self.benefits = benefits

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
    def benefits(self):
        return self._benefits

    @benefits.setter
    def benefits(self, benefits):
        self._benefits = benefits
