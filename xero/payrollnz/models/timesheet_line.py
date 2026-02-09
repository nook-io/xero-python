from xero.models import BaseModel


class TimesheetLine(BaseModel):
    openapi_types = {
        "timesheet_line_id": "str",
        "date": "date",
        "earnings_rate_id": "str",
        "tracking_item_id": "str",
        "number_of_units": "float",
    }
    attribute_map = {
        "timesheet_line_id": "timesheetLineID",
        "date": "date",
        "earnings_rate_id": "earningsRateID",
        "tracking_item_id": "trackingItemID",
        "number_of_units": "numberOfUnits",
    }

    def __init__(
        self,
        timesheet_line_id=None,
        date=None,
        earnings_rate_id=None,
        tracking_item_id=None,
        number_of_units=None,
    ):
        self._timesheet_line_id = None
        self._date = None
        self._earnings_rate_id = None
        self._tracking_item_id = None
        self._number_of_units = None
        self.discriminator = None
        if timesheet_line_id is not None:
            self.timesheet_line_id = timesheet_line_id
        self.date = date
        self.earnings_rate_id = earnings_rate_id
        if tracking_item_id is not None:
            self.tracking_item_id = tracking_item_id
        self.number_of_units = number_of_units

    @property
    def timesheet_line_id(self):
        return self._timesheet_line_id

    @timesheet_line_id.setter
    def timesheet_line_id(self, timesheet_line_id):
        self._timesheet_line_id = timesheet_line_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")
        self._date = date

    @property
    def earnings_rate_id(self):
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        if earnings_rate_id is None:
            raise ValueError("Invalid value for `earnings_rate_id`, must not be `None`")
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
        if number_of_units is None:
            raise ValueError("Invalid value for `number_of_units`, must not be `None`")
        self._number_of_units = number_of_units
