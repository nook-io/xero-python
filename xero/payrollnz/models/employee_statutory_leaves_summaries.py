from xero.models import BaseModel


class EmployeeStatutoryLeavesSummaries(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "statutory_leaves": "list[EmployeeStatutoryLeaveSummary]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "statutory_leaves": "statutoryLeaves",
    }

    def __init__(self, pagination=None, problem=None, statutory_leaves=None):
        self._pagination = None
        self._problem = None
        self._statutory_leaves = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if statutory_leaves is not None:
            self.statutory_leaves = statutory_leaves

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
    def statutory_leaves(self):
        return self._statutory_leaves

    @statutory_leaves.setter
    def statutory_leaves(self, statutory_leaves):
        self._statutory_leaves = statutory_leaves
