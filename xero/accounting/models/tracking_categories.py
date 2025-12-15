from xero.models import BaseModel


class TrackingCategories(BaseModel):
    openapi_types = {"tracking_categories": "list[TrackingCategory]"}
    attribute_map = {"tracking_categories": "TrackingCategories"}

    def __init__(self, tracking_categories=None):
        self._tracking_categories = None
        self.discriminator = None
        if tracking_categories is not None:
            self.tracking_categories = tracking_categories

    @property
    def tracking_categories(self):
        return self._tracking_categories

    @tracking_categories.setter
    def tracking_categories(self, tracking_categories):
        self._tracking_categories = tracking_categories
