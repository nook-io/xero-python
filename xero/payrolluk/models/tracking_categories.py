from xero.models import BaseModel


class TrackingCategories(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "tracking_categories": "TrackingCategory",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "tracking_categories": "trackingCategories",
    }

    def __init__(self, pagination=None, problem=None, tracking_categories=None):
        self._pagination = None
        self._problem = None
        self._tracking_categories = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if tracking_categories is not None:
            self.tracking_categories = tracking_categories

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
    def tracking_categories(self):
        return self._tracking_categories

    @tracking_categories.setter
    def tracking_categories(self, tracking_categories):
        self._tracking_categories = tracking_categories
