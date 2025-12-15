from xero.models import BaseModel


class SalaryAndWageObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "salary_and_wages": "SalaryAndWage",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "salary_and_wages": "salaryAndWages",
    }

    def __init__(self, pagination=None, problem=None, salary_and_wages=None):
        self._pagination = None
        self._problem = None
        self._salary_and_wages = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if salary_and_wages is not None:
            self.salary_and_wages = salary_and_wages

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
    def salary_and_wages(self):
        return self._salary_and_wages

    @salary_and_wages.setter
    def salary_and_wages(self, salary_and_wages):
        self._salary_and_wages = salary_and_wages
