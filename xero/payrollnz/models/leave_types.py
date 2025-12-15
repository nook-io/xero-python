from xero.models import BaseModel


class LeaveTypes(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "leave_types": "list[LeaveType]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "leave_types": "leaveTypes",
    }

    def __init__(self, pagination=None, problem=None, leave_types=None):
        self._pagination = None
        self._problem = None
        self._leave_types = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave_types is not None:
            self.leave_types = leave_types

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
    def leave_types(self):
        return self._leave_types

    @leave_types.setter
    def leave_types(self, leave_types):
        self._leave_types = leave_types
