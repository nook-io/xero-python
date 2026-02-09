from xero.models import BaseModel


class EmployeeTaxObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "employee_tax": "EmployeeTax",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "employee_tax": "employeeTax",
    }

    def __init__(self, pagination=None, problem=None, employee_tax=None):
        self._pagination = None
        self._problem = None
        self._employee_tax = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if employee_tax is not None:
            self.employee_tax = employee_tax

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
    def employee_tax(self):
        return self._employee_tax

    @employee_tax.setter
    def employee_tax(self, employee_tax):
        self._employee_tax = employee_tax
