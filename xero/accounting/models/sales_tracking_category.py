from xero.models import BaseModel


class SalesTrackingCategory(BaseModel):
    openapi_types = {"tracking_category_name": "str", "tracking_option_name": "str"}
    attribute_map = {
        "tracking_category_name": "TrackingCategoryName",
        "tracking_option_name": "TrackingOptionName",
    }

    def __init__(self, tracking_category_name=None, tracking_option_name=None):
        self._tracking_category_name = None
        self._tracking_option_name = None
        self.discriminator = None
        if tracking_category_name is not None:
            self.tracking_category_name = tracking_category_name
        if tracking_option_name is not None:
            self.tracking_option_name = tracking_option_name

    @property
    def tracking_category_name(self):
        return self._tracking_category_name

    @tracking_category_name.setter
    def tracking_category_name(self, tracking_category_name):
        self._tracking_category_name = tracking_category_name

    @property
    def tracking_option_name(self):
        return self._tracking_option_name

    @tracking_option_name.setter
    def tracking_option_name(self, tracking_option_name):
        self._tracking_option_name = tracking_option_name
