from xero.models import BaseModel


class EmploymentObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "employment": "Employment",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "employment": "employment",
    }

    def __init__(self, pagination=None, problem=None, employment=None):
        self._pagination = None
        self._problem = None
        self._employment = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if employment is not None:
            self.employment = employment

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
    def employment(self):
        return self._employment

    @employment.setter
    def employment(self, employment):
        self._employment = employment
