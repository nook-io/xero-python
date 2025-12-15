from xero.models import BaseModel


class TimesheetLine(BaseModel):
    openapi_types = {
        "earnings_rate_id": "str",
        "tracking_item_id": "str",
        "number_of_units": "list[float]",
        "updated_date_utc": "datetime[ms-format]",
    }
    attribute_map = {
        "earnings_rate_id": "EarningsRateID",
        "tracking_item_id": "TrackingItemID",
        "number_of_units": "NumberOfUnits",
        "updated_date_utc": "UpdatedDateUTC",
    }

    def __init__(
        self,
        earnings_rate_id=None,
        tracking_item_id=None,
        number_of_units=None,
        updated_date_utc=None,
    ):
        self._earnings_rate_id = None
        self._tracking_item_id = None
        self._number_of_units = None
        self._updated_date_utc = None
        self.discriminator = None
        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        if tracking_item_id is not None:
            self.tracking_item_id = tracking_item_id
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def earnings_rate_id(self):
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        self._earnings_rate_id = earnings_rate_id

    @property
    def tracking_item_id(self):
        return self._tracking_item_id

    @tracking_item_id.setter
    def tracking_item_id(self, tracking_item_id):
        self._tracking_item_id = tracking_item_id

    @property
    def number_of_units(self):
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        self._number_of_units = number_of_units

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc
