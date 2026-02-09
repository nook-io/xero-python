from xero.models import BaseModel


class EmployeeWorkingPatternsObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "payee_working_patterns": "list[EmployeeWorkingPattern]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "payee_working_patterns": "payeeWorkingPatterns",
    }

    def __init__(self, pagination=None, problem=None, payee_working_patterns=None):
        self._pagination = None
        self._problem = None
        self._payee_working_patterns = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if payee_working_patterns is not None:
            self.payee_working_patterns = payee_working_patterns

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
    def payee_working_patterns(self):
        return self._payee_working_patterns

    @payee_working_patterns.setter
    def payee_working_patterns(self, payee_working_patterns):
        self._payee_working_patterns = payee_working_patterns
