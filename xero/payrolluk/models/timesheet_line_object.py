from xero.models import BaseModel


class TimesheetLineObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "timesheet_line": "TimesheetLine",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "timesheet_line": "timesheetLine",
    }

    def __init__(self, pagination=None, problem=None, timesheet_line=None):
        self._pagination = None
        self._problem = None
        self._timesheet_line = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if timesheet_line is not None:
            self.timesheet_line = timesheet_line

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
    def timesheet_line(self):
        return self._timesheet_line

    @timesheet_line.setter
    def timesheet_line(self, timesheet_line):
        self._timesheet_line = timesheet_line
