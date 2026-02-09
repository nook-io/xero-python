from xero.models import BaseModel


class EmployeeObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "employee": "Employee",
        "problem": "Problem",
    }
    attribute_map = {
        "pagination": "pagination",
        "employee": "employee",
        "problem": "problem",
    }

    def __init__(self, pagination=None, employee=None, problem=None):
        self._pagination = None
        self._employee = None
        self._problem = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if employee is not None:
            self.employee = employee
        if problem is not None:
            self.problem = problem

    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        self._pagination = pagination

    @property
    def employee(self):
        return self._employee

    @employee.setter
    def employee(self, employee):
        self._employee = employee

    @property
    def problem(self):
        return self._problem

    @problem.setter
    def problem(self, problem):
        self._problem = problem
