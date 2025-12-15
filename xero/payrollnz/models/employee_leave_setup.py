from xero.models import BaseModel


class EmployeeLeaveSetup(BaseModel):
    openapi_types = {
        "include_holiday_pay": "bool",
        "holiday_pay_opening_balance": "float",
        "annual_leave_opening_balance": "float",
        "negative_annual_leave_balance_paid_amount": "float",
        "sick_leave_hours_to_accrue_annually": "float",
        "sick_leave_maximum_hours_to_accrue": "float",
        "sick_leave_opening_balance": "float",
        "sick_leave_schedule_of_accrual": "str",
        "sick_leave_anniversary_date": "date",
    }
    attribute_map = {
        "include_holiday_pay": "includeHolidayPay",
        "holiday_pay_opening_balance": "holidayPayOpeningBalance",
        "annual_leave_opening_balance": "annualLeaveOpeningBalance",
        "negative_annual_leave_balance_paid_amount": "negativeAnnualLeaveBalancePaidAmount",
        "sick_leave_hours_to_accrue_annually": "sickLeaveHoursToAccrueAnnually",
        "sick_leave_maximum_hours_to_accrue": "sickLeaveMaximumHoursToAccrue",
        "sick_leave_opening_balance": "sickLeaveOpeningBalance",
        "sick_leave_schedule_of_accrual": "SickLeaveScheduleOfAccrual",
        "sick_leave_anniversary_date": "SickLeaveAnniversaryDate",
    }

    def __init__(
        self,
        include_holiday_pay=None,
        holiday_pay_opening_balance=None,
        annual_leave_opening_balance=None,
        negative_annual_leave_balance_paid_amount=None,
        sick_leave_hours_to_accrue_annually=None,
        sick_leave_maximum_hours_to_accrue=None,
        sick_leave_opening_balance=None,
        sick_leave_schedule_of_accrual=None,
        sick_leave_anniversary_date=None,
    ):
        self._include_holiday_pay = None
        self._holiday_pay_opening_balance = None
        self._annual_leave_opening_balance = None
        self._negative_annual_leave_balance_paid_amount = None
        self._sick_leave_hours_to_accrue_annually = None
        self._sick_leave_maximum_hours_to_accrue = None
        self._sick_leave_opening_balance = None
        self._sick_leave_schedule_of_accrual = None
        self._sick_leave_anniversary_date = None
        self.discriminator = None
        if include_holiday_pay is not None:
            self.include_holiday_pay = include_holiday_pay
        if holiday_pay_opening_balance is not None:
            self.holiday_pay_opening_balance = holiday_pay_opening_balance
        if annual_leave_opening_balance is not None:
            self.annual_leave_opening_balance = annual_leave_opening_balance
        if negative_annual_leave_balance_paid_amount is not None:
            self.negative_annual_leave_balance_paid_amount = (
                negative_annual_leave_balance_paid_amount
            )
        if sick_leave_hours_to_accrue_annually is not None:
            self.sick_leave_hours_to_accrue_annually = (
                sick_leave_hours_to_accrue_annually
            )
        if sick_leave_maximum_hours_to_accrue is not None:
            self.sick_leave_maximum_hours_to_accrue = sick_leave_maximum_hours_to_accrue
        if sick_leave_opening_balance is not None:
            self.sick_leave_opening_balance = sick_leave_opening_balance
        if sick_leave_schedule_of_accrual is not None:
            self.sick_leave_schedule_of_accrual = sick_leave_schedule_of_accrual
        if sick_leave_anniversary_date is not None:
            self.sick_leave_anniversary_date = sick_leave_anniversary_date

    @property
    def include_holiday_pay(self):
        return self._include_holiday_pay

    @include_holiday_pay.setter
    def include_holiday_pay(self, include_holiday_pay):
        self._include_holiday_pay = include_holiday_pay

    @property
    def holiday_pay_opening_balance(self):
        return self._holiday_pay_opening_balance

    @holiday_pay_opening_balance.setter
    def holiday_pay_opening_balance(self, holiday_pay_opening_balance):
        self._holiday_pay_opening_balance = holiday_pay_opening_balance

    @property
    def annual_leave_opening_balance(self):
        return self._annual_leave_opening_balance

    @annual_leave_opening_balance.setter
    def annual_leave_opening_balance(self, annual_leave_opening_balance):
        self._annual_leave_opening_balance = annual_leave_opening_balance

    @property
    def negative_annual_leave_balance_paid_amount(self):
        return self._negative_annual_leave_balance_paid_amount

    @negative_annual_leave_balance_paid_amount.setter
    def negative_annual_leave_balance_paid_amount(
        self, negative_annual_leave_balance_paid_amount
    ):
        self._negative_annual_leave_balance_paid_amount = (
            negative_annual_leave_balance_paid_amount
        )

    @property
    def sick_leave_hours_to_accrue_annually(self):
        return self._sick_leave_hours_to_accrue_annually

    @sick_leave_hours_to_accrue_annually.setter
    def sick_leave_hours_to_accrue_annually(self, sick_leave_hours_to_accrue_annually):
        self._sick_leave_hours_to_accrue_annually = sick_leave_hours_to_accrue_annually

    @property
    def sick_leave_maximum_hours_to_accrue(self):
        return self._sick_leave_maximum_hours_to_accrue

    @sick_leave_maximum_hours_to_accrue.setter
    def sick_leave_maximum_hours_to_accrue(self, sick_leave_maximum_hours_to_accrue):
        self._sick_leave_maximum_hours_to_accrue = sick_leave_maximum_hours_to_accrue

    @property
    def sick_leave_opening_balance(self):
        return self._sick_leave_opening_balance

    @sick_leave_opening_balance.setter
    def sick_leave_opening_balance(self, sick_leave_opening_balance):
        self._sick_leave_opening_balance = sick_leave_opening_balance

    @property
    def sick_leave_schedule_of_accrual(self):
        return self._sick_leave_schedule_of_accrual

    @sick_leave_schedule_of_accrual.setter
    def sick_leave_schedule_of_accrual(self, sick_leave_schedule_of_accrual):
        self._sick_leave_schedule_of_accrual = sick_leave_schedule_of_accrual

    @property
    def sick_leave_anniversary_date(self):
        return self._sick_leave_anniversary_date

    @sick_leave_anniversary_date.setter
    def sick_leave_anniversary_date(self, sick_leave_anniversary_date):
        self._sick_leave_anniversary_date = sick_leave_anniversary_date
