from xero.models import BaseModel


class EmployeeLeaveSetupObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "leave_setup": "EmployeeLeaveSetup",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "leave_setup": "leaveSetup",
    }

    def __init__(self, pagination=None, problem=None, leave_setup=None):
        self._pagination = None
        self._problem = None
        self._leave_setup = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave_setup is not None:
            self.leave_setup = leave_setup

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
    def leave_setup(self):
        return self._leave_setup

    @leave_setup.setter
    def leave_setup(self, leave_setup):
        self._leave_setup = leave_setup
