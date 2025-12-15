from xero.models import BaseModel


class EmployeeWorkingPatternWithWorkingWeeksObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "payee_working_pattern": "EmployeeWorkingPatternWithWorkingWeeks",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "payee_working_pattern": "payeeWorkingPattern",
    }

    def __init__(self, pagination=None, problem=None, payee_working_pattern=None):
        self._pagination = None
        self._problem = None
        self._payee_working_pattern = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if payee_working_pattern is not None:
            self.payee_working_pattern = payee_working_pattern

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
    def payee_working_pattern(self):
        return self._payee_working_pattern

    @payee_working_pattern.setter
    def payee_working_pattern(self, payee_working_pattern):
        self._payee_working_pattern = payee_working_pattern
