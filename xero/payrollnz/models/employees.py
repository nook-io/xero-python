from xero.models import BaseModel


class Employees(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "employees": "list[Employee]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "employees": "employees",
    }

    def __init__(self, pagination=None, problem=None, employees=None):
        self._pagination = None
        self._problem = None
        self._employees = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if employees is not None:
            self.employees = employees

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
    def employees(self):
        return self._employees

    @employees.setter
    def employees(self, employees):
        self._employees = employees
