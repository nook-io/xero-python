from xero.models import BaseModel


class EarningsRates(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "earnings_rates": "list[EarningsRate]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "earnings_rates": "earningsRates",
    }

    def __init__(self, pagination=None, problem=None, earnings_rates=None):
        self._pagination = None
        self._problem = None
        self._earnings_rates = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if earnings_rates is not None:
            self.earnings_rates = earnings_rates

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
    def earnings_rates(self):
        return self._earnings_rates

    @earnings_rates.setter
    def earnings_rates(self, earnings_rates):
        self._earnings_rates = earnings_rates
