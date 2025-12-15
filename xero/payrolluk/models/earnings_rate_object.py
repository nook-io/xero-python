from xero.models import BaseModel


class EarningsRateObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "earnings_rate": "EarningsRate",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "earnings_rate": "earningsRate",
    }

    def __init__(self, pagination=None, problem=None, earnings_rate=None):
        self._pagination = None
        self._problem = None
        self._earnings_rate = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if earnings_rate is not None:
            self.earnings_rate = earnings_rate

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
    def earnings_rate(self):
        return self._earnings_rate

    @earnings_rate.setter
    def earnings_rate(self, earnings_rate):
        self._earnings_rate = earnings_rate
