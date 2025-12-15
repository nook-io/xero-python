from xero.models import BaseModel


class LineItemTracking(BaseModel):
    openapi_types = {
        "tracking_category_id": "str",
        "tracking_option_id": "str",
        "name": "str",
        "option": "str",
    }
    attribute_map = {
        "tracking_category_id": "TrackingCategoryID",
        "tracking_option_id": "TrackingOptionID",
        "name": "Name",
        "option": "Option",
    }

    def __init__(
        self, tracking_category_id=None, tracking_option_id=None, name=None, option=None
    ):
        self._tracking_category_id = None
        self._tracking_option_id = None
        self._name = None
        self._option = None
        self.discriminator = None
        if tracking_category_id is not None:
            self.tracking_category_id = tracking_category_id
        if tracking_option_id is not None:
            self.tracking_option_id = tracking_option_id
        if name is not None:
            self.name = name
        if option is not None:
            self.option = option

    @property
    def tracking_category_id(self):
        return self._tracking_category_id

    @tracking_category_id.setter
    def tracking_category_id(self, tracking_category_id):
        self._tracking_category_id = tracking_category_id

    @property
    def tracking_option_id(self):
        return self._tracking_option_id

    @tracking_option_id.setter
    def tracking_option_id(self, tracking_option_id):
        self._tracking_option_id = tracking_option_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 100:
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `100`"
            )
        self._name = name

    @property
    def option(self):
        return self._option

    @option.setter
    def option(self, option):
        self._option = option
