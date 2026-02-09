from xero.models import BaseModel


class EmployeeEarningsTemplates(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "earning_templates": "list[EarningsTemplate]",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "earning_templates": "earningTemplates",
    }

    def __init__(self, pagination=None, problem=None, earning_templates=None):
        self._pagination = None
        self._problem = None
        self._earning_templates = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if earning_templates is not None:
            self.earning_templates = earning_templates

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
    def earning_templates(self):
        return self._earning_templates

    @earning_templates.setter
    def earning_templates(self, earning_templates):
        self._earning_templates = earning_templates
