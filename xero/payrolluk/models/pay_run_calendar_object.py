from xero.models import BaseModel


class PayRunCalendarObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "pay_run_calendar": "PayRunCalendar",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_run_calendar": "payRunCalendar",
    }

    def __init__(self, pagination=None, problem=None, pay_run_calendar=None):
        self._pagination = None
        self._problem = None
        self._pay_run_calendar = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_run_calendar is not None:
            self.pay_run_calendar = pay_run_calendar

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
    def pay_run_calendar(self):
        return self._pay_run_calendar

    @pay_run_calendar.setter
    def pay_run_calendar(self, pay_run_calendar):
        self._pay_run_calendar = pay_run_calendar
