from xero.models import BaseModel


class EmployeeLeaveType(BaseModel):
    openapi_types = {
        "leave_type_id": "str",
        "schedule_of_accrual": "str",
        "hours_accrued_annually": "float",
        "maximum_to_accrue": "float",
        "opening_balance": "float",
        "rate_accrued_hourly": "float",
        "schedule_of_accrual_date": "date",
    }
    attribute_map = {
        "leave_type_id": "leaveTypeID",
        "schedule_of_accrual": "scheduleOfAccrual",
        "hours_accrued_annually": "hoursAccruedAnnually",
        "maximum_to_accrue": "maximumToAccrue",
        "opening_balance": "openingBalance",
        "rate_accrued_hourly": "rateAccruedHourly",
        "schedule_of_accrual_date": "scheduleOfAccrualDate",
    }

    def __init__(
        self,
        leave_type_id=None,
        schedule_of_accrual=None,
        hours_accrued_annually=None,
        maximum_to_accrue=None,
        opening_balance=None,
        rate_accrued_hourly=None,
        schedule_of_accrual_date=None,
    ):
        self._leave_type_id = None
        self._schedule_of_accrual = None
        self._hours_accrued_annually = None
        self._maximum_to_accrue = None
        self._opening_balance = None
        self._rate_accrued_hourly = None
        self._schedule_of_accrual_date = None
        self.discriminator = None
        self.leave_type_id = leave_type_id
        self.schedule_of_accrual = schedule_of_accrual
        if hours_accrued_annually is not None:
            self.hours_accrued_annually = hours_accrued_annually
        if maximum_to_accrue is not None:
            self.maximum_to_accrue = maximum_to_accrue
        if opening_balance is not None:
            self.opening_balance = opening_balance
        if rate_accrued_hourly is not None:
            self.rate_accrued_hourly = rate_accrued_hourly
        if schedule_of_accrual_date is not None:
            self.schedule_of_accrual_date = schedule_of_accrual_date

    @property
    def leave_type_id(self):
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        if leave_type_id is None:
            raise ValueError("Invalid value for `leave_type_id`, must not be `None`")
        self._leave_type_id = leave_type_id

    @property
    def schedule_of_accrual(self):
        return self._schedule_of_accrual

    @schedule_of_accrual.setter
    def schedule_of_accrual(self, schedule_of_accrual):
        if schedule_of_accrual is None:
            raise ValueError(
                "Invalid value for `schedule_of_accrual`, must not be `None`"
            )
        allowed_values = [
            "BeginningOfCalendarYear",
            "OnAnniversaryDate",
            "EachPayPeriod",
            "OnHourWorked",
            "None",
        ]
        if schedule_of_accrual:
            if schedule_of_accrual not in allowed_values:
                raise ValueError(
                    "Invalid value for `schedule_of_accrual` ({0}), must be one of {1}".format(
                        schedule_of_accrual, allowed_values
                    )
                )
        self._schedule_of_accrual = schedule_of_accrual

    @property
    def hours_accrued_annually(self):
        return self._hours_accrued_annually

    @hours_accrued_annually.setter
    def hours_accrued_annually(self, hours_accrued_annually):
        self._hours_accrued_annually = hours_accrued_annually

    @property
    def maximum_to_accrue(self):
        return self._maximum_to_accrue

    @maximum_to_accrue.setter
    def maximum_to_accrue(self, maximum_to_accrue):
        self._maximum_to_accrue = maximum_to_accrue

    @property
    def opening_balance(self):
        return self._opening_balance

    @opening_balance.setter
    def opening_balance(self, opening_balance):
        self._opening_balance = opening_balance

    @property
    def rate_accrued_hourly(self):
        return self._rate_accrued_hourly

    @rate_accrued_hourly.setter
    def rate_accrued_hourly(self, rate_accrued_hourly):
        self._rate_accrued_hourly = rate_accrued_hourly

    @property
    def schedule_of_accrual_date(self):
        return self._schedule_of_accrual_date

    @schedule_of_accrual_date.setter
    def schedule_of_accrual_date(self, schedule_of_accrual_date):
        self._schedule_of_accrual_date = schedule_of_accrual_date
