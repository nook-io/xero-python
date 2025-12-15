from xero.models import BaseModel


class Timesheets(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "timesheets": "list[Timesheet]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "timesheets": "timesheets",
    }

    def __init__(self, pagination=None, problem=None, timesheets=None):
        self._pagination = None
        self._problem = None
        self._timesheets = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if timesheets is not None:
            self.timesheets = timesheets

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
    def timesheets(self):
        return self._timesheets

    @timesheets.setter
    def timesheets(self, timesheets):
        self._timesheets = timesheets
