from xero.models import BaseModel


class TimesheetEarningsLine(BaseModel):
    openapi_types = {
        "earnings_line_id": "str",
        "earnings_rate_id": "str",
        "display_name": "str",
        "rate_per_unit": "float",
        "number_of_units": "float",
        "fixed_amount": "float",
        "amount": "float",
        "is_linked_to_timesheet": "bool",
        "is_average_daily_pay_rate": "bool",
        "is_system_generated": "bool",
    }
    attribute_map = {
        "earnings_line_id": "earningsLineID",
        "earnings_rate_id": "earningsRateID",
        "display_name": "displayName",
        "rate_per_unit": "ratePerUnit",
        "number_of_units": "numberOfUnits",
        "fixed_amount": "fixedAmount",
        "amount": "amount",
        "is_linked_to_timesheet": "isLinkedToTimesheet",
        "is_average_daily_pay_rate": "isAverageDailyPayRate",
        "is_system_generated": "isSystemGenerated",
    }

    def __init__(
        self,
        earnings_line_id=None,
        earnings_rate_id=None,
        display_name=None,
        rate_per_unit=None,
        number_of_units=None,
        fixed_amount=None,
        amount=None,
        is_linked_to_timesheet=None,
        is_average_daily_pay_rate=None,
        is_system_generated=None,
    ):
        self._earnings_line_id = None
        self._earnings_rate_id = None
        self._display_name = None
        self._rate_per_unit = None
        self._number_of_units = None
        self._fixed_amount = None
        self._amount = None
        self._is_linked_to_timesheet = None
        self._is_average_daily_pay_rate = None
        self._is_system_generated = None
        self.discriminator = None
        if earnings_line_id is not None:
            self.earnings_line_id = earnings_line_id
        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        if display_name is not None:
            self.display_name = display_name
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount
        if amount is not None:
            self.amount = amount
        if is_linked_to_timesheet is not None:
            self.is_linked_to_timesheet = is_linked_to_timesheet
        if is_average_daily_pay_rate is not None:
            self.is_average_daily_pay_rate = is_average_daily_pay_rate
        if is_system_generated is not None:
            self.is_system_generated = is_system_generated

    @property
    def earnings_line_id(self):
        return self._earnings_line_id

    @earnings_line_id.setter
    def earnings_line_id(self, earnings_line_id):
        self._earnings_line_id = earnings_line_id

    @property
    def earnings_rate_id(self):
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        self._earnings_rate_id = earnings_rate_id

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        self._display_name = display_name

    @property
    def rate_per_unit(self):
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        self._rate_per_unit = rate_per_unit

    @property
    def number_of_units(self):
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        self._number_of_units = number_of_units

    @property
    def fixed_amount(self):
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        self._fixed_amount = fixed_amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def is_linked_to_timesheet(self):
        return self._is_linked_to_timesheet

    @is_linked_to_timesheet.setter
    def is_linked_to_timesheet(self, is_linked_to_timesheet):
        self._is_linked_to_timesheet = is_linked_to_timesheet

    @property
    def is_average_daily_pay_rate(self):
        return self._is_average_daily_pay_rate

    @is_average_daily_pay_rate.setter
    def is_average_daily_pay_rate(self, is_average_daily_pay_rate):
        self._is_average_daily_pay_rate = is_average_daily_pay_rate

    @property
    def is_system_generated(self):
        return self._is_system_generated

    @is_system_generated.setter
    def is_system_generated(self, is_system_generated):
        self._is_system_generated = is_system_generated
