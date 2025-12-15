from xero.models import BaseModel


class Settings(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "settings": "Accounts",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "settings": "settings",
    }

    def __init__(self, pagination=None, problem=None, settings=None):
        self._pagination = None
        self._problem = None
        self._settings = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if settings is not None:
            self.settings = settings

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
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, settings):
        self._settings = settings
