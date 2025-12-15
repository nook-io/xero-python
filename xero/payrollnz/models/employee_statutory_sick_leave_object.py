from xero.models import BaseModel


class EmployeeStatutorySickLeaveObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "statutory_sick_leave": "EmployeeStatutorySickLeave",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "statutory_sick_leave": "statutorySickLeave",
    }

    def __init__(self, pagination=None, problem=None, statutory_sick_leave=None):
        self._pagination = None
        self._problem = None
        self._statutory_sick_leave = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if statutory_sick_leave is not None:
            self.statutory_sick_leave = statutory_sick_leave

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
    def statutory_sick_leave(self):
        return self._statutory_sick_leave

    @statutory_sick_leave.setter
    def statutory_sick_leave(self, statutory_sick_leave):
        self._statutory_sick_leave = statutory_sick_leave
