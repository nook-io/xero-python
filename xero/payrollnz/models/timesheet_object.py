from xero.models import BaseModel


class TimesheetObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "timesheet": "Timesheet",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "timesheet": "timesheet",
    }

    def __init__(self, pagination=None, problem=None, timesheet=None):
        self._pagination = None
        self._problem = None
        self._timesheet = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if timesheet is not None:
            self.timesheet = timesheet

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
    def timesheet(self):
        return self._timesheet

    @timesheet.setter
    def timesheet(self, timesheet):
        self._timesheet = timesheet
