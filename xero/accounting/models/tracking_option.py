from xero.models import BaseModel


class TrackingOption(BaseModel):
    openapi_types = {
        "tracking_option_id": "str",
        "name": "str",
        "status": "str",
        "tracking_category_id": "str",
    }
    attribute_map = {
        "tracking_option_id": "TrackingOptionID",
        "name": "Name",
        "status": "Status",
        "tracking_category_id": "TrackingCategoryID",
    }

    def __init__(
        self, tracking_option_id=None, name=None, status=None, tracking_category_id=None
    ):
        self._tracking_option_id = None
        self._name = None
        self._status = None
        self._tracking_category_id = None
        self.discriminator = None
        if tracking_option_id is not None:
            self.tracking_option_id = tracking_option_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if tracking_category_id is not None:
            self.tracking_category_id = tracking_category_id

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
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["ACTIVE", "ARCHIVED", "DELETED", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def tracking_category_id(self):
        return self._tracking_category_id

    @tracking_category_id.setter
    def tracking_category_id(self, tracking_category_id):
        self._tracking_category_id = tracking_category_id
