from xero.models import BaseModel


class LeavePeriods(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "periods": "list[LeavePeriod]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "periods": "periods",
    }

    def __init__(self, pagination=None, problem=None, periods=None):
        self._pagination = None
        self._problem = None
        self._periods = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if periods is not None:
            self.periods = periods

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
    def periods(self):
        return self._periods

    @periods.setter
    def periods(self, periods):
        self._periods = periods
