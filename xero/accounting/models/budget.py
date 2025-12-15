from xero.models import BaseModel


class Budget(BaseModel):
    openapi_types = {
        "budget_id": "str",
        "type": "str",
        "description": "str",
        "updated_date_utc": "datetime[ms-format]",
        "budget_lines": "list[BudgetLine]",
        "tracking": "list[TrackingCategory]",
    }
    attribute_map = {
        "budget_id": "BudgetID",
        "type": "Type",
        "description": "Description",
        "updated_date_utc": "UpdatedDateUTC",
        "budget_lines": "BudgetLines",
        "tracking": "Tracking",
    }

    def __init__(
        self,
        budget_id=None,
        type=None,
        description=None,
        updated_date_utc=None,
        budget_lines=None,
        tracking=None,
    ):
        self._budget_id = None
        self._type = None
        self._description = None
        self._updated_date_utc = None
        self._budget_lines = None
        self._tracking = None
        self.discriminator = None
        if budget_id is not None:
            self.budget_id = budget_id
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if budget_lines is not None:
            self.budget_lines = budget_lines
        if tracking is not None:
            self.tracking = tracking

    @property
    def budget_id(self):
        return self._budget_id

    @budget_id.setter
    def budget_id(self, budget_id):
        self._budget_id = budget_id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_values = ["OVERALL", "TRACKING", "None"]
        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(
                        type, allowed_values
                    )
                )
        self._type = type

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if description is not None and len(description) > 255:
            raise ValueError(
                "Invalid value for `description`, "
                "length must be less than or equal to `255`"
            )
        self._description = description

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def budget_lines(self):
        return self._budget_lines

    @budget_lines.setter
    def budget_lines(self, budget_lines):
        self._budget_lines = budget_lines

    @property
    def tracking(self):
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        self._tracking = tracking
