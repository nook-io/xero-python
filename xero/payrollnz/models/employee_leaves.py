from xero.models import BaseModel


class EmployeeLeaves(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "leave": "list[EmployeeLeave]",
    }
    attribute_map = {"pagination": "pagination", "problem": "problem", "leave": "leave"}

    def __init__(self, pagination=None, problem=None, leave=None):
        self._pagination = None
        self._problem = None
        self._leave = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave is not None:
            self.leave = leave

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
    def leave(self):
        return self._leave

    @leave.setter
    def leave(self, leave):
        self._leave = leave
