from xero.models import BaseModel


class EarningsTemplateObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "earning_template": "EarningsTemplate",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "earning_template": "earningTemplate",
    }

    def __init__(self, pagination=None, problem=None, earning_template=None):
        self._pagination = None
        self._problem = None
        self._earning_template = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if earning_template is not None:
            self.earning_template = earning_template

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
    def earning_template(self):
        return self._earning_template

    @earning_template.setter
    def earning_template(self, earning_template):
        self._earning_template = earning_template
