from xero.models import BaseModel


class LeavePeriod(BaseModel):
    openapi_types = {
        "number_of_units": "float",
        "pay_period_end_date": "date[ms-format]",
        "pay_period_start_date": "date[ms-format]",
        "leave_period_status": "LeavePeriodStatus",
    }
    attribute_map = {
        "number_of_units": "NumberOfUnits",
        "pay_period_end_date": "PayPeriodEndDate",
        "pay_period_start_date": "PayPeriodStartDate",
        "leave_period_status": "LeavePeriodStatus",
    }

    def __init__(
        self,
        number_of_units=None,
        pay_period_end_date=None,
        pay_period_start_date=None,
        leave_period_status=None,
    ):
        self._number_of_units = None
        self._pay_period_end_date = None
        self._pay_period_start_date = None
        self._leave_period_status = None
        self.discriminator = None
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if pay_period_end_date is not None:
            self.pay_period_end_date = pay_period_end_date
        if pay_period_start_date is not None:
            self.pay_period_start_date = pay_period_start_date
        if leave_period_status is not None:
            self.leave_period_status = leave_period_status

    @property
    def number_of_units(self):
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        self._number_of_units = number_of_units

    @property
    def pay_period_end_date(self):
        return self._pay_period_end_date

    @pay_period_end_date.setter
    def pay_period_end_date(self, pay_period_end_date):
        self._pay_period_end_date = pay_period_end_date

    @property
    def pay_period_start_date(self):
        return self._pay_period_start_date

    @pay_period_start_date.setter
    def pay_period_start_date(self, pay_period_start_date):
        self._pay_period_start_date = pay_period_start_date

    @property
    def leave_period_status(self):
        return self._leave_period_status

    @leave_period_status.setter
    def leave_period_status(self, leave_period_status):
        self._leave_period_status = leave_period_status
