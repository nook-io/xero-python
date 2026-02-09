from xero.models import BaseModel


class Reimbursements(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "reimbursements": "list[Reimbursement]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "reimbursements": "reimbursements",
    }

    def __init__(self, pagination=None, problem=None, reimbursements=None):
        self._pagination = None
        self._problem = None
        self._reimbursements = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if reimbursements is not None:
            self.reimbursements = reimbursements

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
    def reimbursements(self):
        return self._reimbursements

    @reimbursements.setter
    def reimbursements(self, reimbursements):
        self._reimbursements = reimbursements
