from xero.models import BaseModel


class PayRunCalendars(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "pay_run_calendars": "list[PayRunCalendar]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_run_calendars": "payRunCalendars",
    }

    def __init__(self, pagination=None, problem=None, pay_run_calendars=None):
        self._pagination = None
        self._problem = None
        self._pay_run_calendars = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_run_calendars is not None:
            self.pay_run_calendars = pay_run_calendars

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
    def pay_run_calendars(self):
        return self._pay_run_calendars

    @pay_run_calendars.setter
    def pay_run_calendars(self, pay_run_calendars):
        self._pay_run_calendars = pay_run_calendars
