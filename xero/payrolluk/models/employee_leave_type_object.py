from xero.models import BaseModel


class EmployeeLeaveTypeObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "leave_type": "EmployeeLeaveType",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "leave_type": "leaveType",
    }

    def __init__(self, pagination=None, problem=None, leave_type=None):
        self._pagination = None
        self._problem = None
        self._leave_type = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave_type is not None:
            self.leave_type = leave_type

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
    def leave_type(self):
        return self._leave_type

    @leave_type.setter
    def leave_type(self, leave_type):
        self._leave_type = leave_type
