from xero.models import BaseModel


class TrackingCategory(BaseModel):
    openapi_types = {
        "tracking_category_id": "str",
        "tracking_option_id": "str",
        "name": "str",
        "option": "str",
        "status": "str",
        "options": "list[TrackingOption]",
    }
    attribute_map = {
        "tracking_category_id": "TrackingCategoryID",
        "tracking_option_id": "TrackingOptionID",
        "name": "Name",
        "option": "Option",
        "status": "Status",
        "options": "Options",
    }

    def __init__(
        self,
        tracking_category_id=None,
        tracking_option_id=None,
        name=None,
        option=None,
        status=None,
        options=None,
    ):
        self._tracking_category_id = None
        self._tracking_option_id = None
        self._name = None
        self._option = None
        self._status = None
        self._options = None
        self.discriminator = None
        if tracking_category_id is not None:
            self.tracking_category_id = tracking_category_id
        if tracking_option_id is not None:
            self.tracking_option_id = tracking_option_id
        if name is not None:
            self.name = name
        if option is not None:
            self.option = option
        if status is not None:
            self.status = status
        if options is not None:
            self.options = options

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
        if option is not None and len(option) > 100:
            raise ValueError(
                "Invalid value for `option`, length must be less than or equal to `100`"
            )
        self._option = option

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
    def options(self):
        return self._options

    @options.setter
    def options(self, options):
        self._options = options
