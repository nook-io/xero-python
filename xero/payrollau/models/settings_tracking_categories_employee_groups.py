from xero.models import BaseModel


class SettingsTrackingCategoriesEmployeeGroups(BaseModel):
    openapi_types = {"tracking_category_id": "str", "tracking_category_name": "str"}
    attribute_map = {
        "tracking_category_id": "TrackingCategoryID",
        "tracking_category_name": "TrackingCategoryName",
    }

    def __init__(self, tracking_category_id=None, tracking_category_name=None):
        self._tracking_category_id = None
        self._tracking_category_name = None
        self.discriminator = None
        if tracking_category_id is not None:
            self.tracking_category_id = tracking_category_id
        if tracking_category_name is not None:
            self.tracking_category_name = tracking_category_name

    @property
    def tracking_category_id(self):
        return self._tracking_category_id

    @tracking_category_id.setter
    def tracking_category_id(self, tracking_category_id):
        self._tracking_category_id = tracking_category_id

    @property
    def tracking_category_name(self):
        return self._tracking_category_name

    @tracking_category_name.setter
    def tracking_category_name(self, tracking_category_name):
        self._tracking_category_name = tracking_category_name
