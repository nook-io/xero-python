from xero.models import BaseModel


class EmployeePayTemplates(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "pay_template": "EmployeePayTemplate",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_template": "payTemplate",
    }

    def __init__(self, pagination=None, problem=None, pay_template=None):
        self._pagination = None
        self._problem = None
        self._pay_template = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_template is not None:
            self.pay_template = pay_template

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
    def pay_template(self):
        return self._pay_template

    @pay_template.setter
    def pay_template(self, pay_template):
        self._pay_template = pay_template
