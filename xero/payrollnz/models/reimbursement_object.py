from xero.models import BaseModel


class ReimbursementObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "reimbursement": "Reimbursement",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "reimbursement": "reimbursement",
    }

    def __init__(self, pagination=None, problem=None, reimbursement=None):
        self._pagination = None
        self._problem = None
        self._reimbursement = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if reimbursement is not None:
            self.reimbursement = reimbursement

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
    def reimbursement(self):
        return self._reimbursement

    @reimbursement.setter
    def reimbursement(self, reimbursement):
        self._reimbursement = reimbursement
