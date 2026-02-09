from xero.models import BaseModel


class EmployeeLeaveType(BaseModel):
    openapi_types = {
        "leave_type_id": "str",
        "schedule_of_accrual": "str",
        "hours_accrued_annually": "float",
        "maximum_to_accrue": "float",
        "opening_balance": "float",
        "rate_accrued_hourly": "float",
        "percentage_of_gross_earnings": "float",
        "include_holiday_pay_every_pay": "bool",
        "show_annual_leave_in_advance": "bool",
        "annual_leave_total_amount_paid": "float",
        "schedule_of_accrual_date": "date",
    }
    attribute_map = {
        "leave_type_id": "leaveTypeID",
        "schedule_of_accrual": "scheduleOfAccrual",
        "hours_accrued_annually": "hoursAccruedAnnually",
        "maximum_to_accrue": "maximumToAccrue",
        "opening_balance": "openingBalance",
        "rate_accrued_hourly": "rateAccruedHourly",
        "percentage_of_gross_earnings": "percentageOfGrossEarnings",
        "include_holiday_pay_every_pay": "includeHolidayPayEveryPay",
        "show_annual_leave_in_advance": "showAnnualLeaveInAdvance",
        "annual_leave_total_amount_paid": "annualLeaveTotalAmountPaid",
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
        percentage_of_gross_earnings=None,
        include_holiday_pay_every_pay=None,
        show_annual_leave_in_advance=None,
        annual_leave_total_amount_paid=None,
        schedule_of_accrual_date=None,
    ):
        self._leave_type_id = None
        self._schedule_of_accrual = None
        self._hours_accrued_annually = None
        self._maximum_to_accrue = None
        self._opening_balance = None
        self._rate_accrued_hourly = None
        self._percentage_of_gross_earnings = None
        self._include_holiday_pay_every_pay = None
        self._show_annual_leave_in_advance = None
        self._annual_leave_total_amount_paid = None
        self._schedule_of_accrual_date = None
        self.discriminator = None
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if schedule_of_accrual is not None:
            self.schedule_of_accrual = schedule_of_accrual
        if hours_accrued_annually is not None:
            self.hours_accrued_annually = hours_accrued_annually
        if maximum_to_accrue is not None:
            self.maximum_to_accrue = maximum_to_accrue
        if opening_balance is not None:
            self.opening_balance = opening_balance
        if rate_accrued_hourly is not None:
            self.rate_accrued_hourly = rate_accrued_hourly
        if percentage_of_gross_earnings is not None:
            self.percentage_of_gross_earnings = percentage_of_gross_earnings
        if include_holiday_pay_every_pay is not None:
            self.include_holiday_pay_every_pay = include_holiday_pay_every_pay
        if show_annual_leave_in_advance is not None:
            self.show_annual_leave_in_advance = show_annual_leave_in_advance
        if annual_leave_total_amount_paid is not None:
            self.annual_leave_total_amount_paid = annual_leave_total_amount_paid
        if schedule_of_accrual_date is not None:
            self.schedule_of_accrual_date = schedule_of_accrual_date

    @property
    def leave_type_id(self):
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        self._leave_type_id = leave_type_id

    @property
    def schedule_of_accrual(self):
        return self._schedule_of_accrual

    @schedule_of_accrual.setter
    def schedule_of_accrual(self, schedule_of_accrual):
        allowed_values = [
            "AnnuallyAfter6Months",
            "OnAnniversaryDate",
            "PercentageOfGrossEarnings",
            "NoAccruals",
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
    def percentage_of_gross_earnings(self):
        return self._percentage_of_gross_earnings

    @percentage_of_gross_earnings.setter
    def percentage_of_gross_earnings(self, percentage_of_gross_earnings):
        self._percentage_of_gross_earnings = percentage_of_gross_earnings

    @property
    def include_holiday_pay_every_pay(self):
        return self._include_holiday_pay_every_pay

    @include_holiday_pay_every_pay.setter
    def include_holiday_pay_every_pay(self, include_holiday_pay_every_pay):
        self._include_holiday_pay_every_pay = include_holiday_pay_every_pay

    @property
    def show_annual_leave_in_advance(self):
        return self._show_annual_leave_in_advance

    @show_annual_leave_in_advance.setter
    def show_annual_leave_in_advance(self, show_annual_leave_in_advance):
        self._show_annual_leave_in_advance = show_annual_leave_in_advance

    @property
    def annual_leave_total_amount_paid(self):
        return self._annual_leave_total_amount_paid

    @annual_leave_total_amount_paid.setter
    def annual_leave_total_amount_paid(self, annual_leave_total_amount_paid):
        self._annual_leave_total_amount_paid = annual_leave_total_amount_paid

    @property
    def schedule_of_accrual_date(self):
        return self._schedule_of_accrual_date

    @schedule_of_accrual_date.setter
    def schedule_of_accrual_date(self, schedule_of_accrual_date):
        self._schedule_of_accrual_date = schedule_of_accrual_date
