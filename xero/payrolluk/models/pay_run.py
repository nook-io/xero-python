from xero.models import BaseModel


class PayRun(BaseModel):
    openapi_types = {
        "pay_run_id": "str",
        "payroll_calendar_id": "str",
        "period_start_date": "date",
        "period_end_date": "date",
        "payment_date": "date",
        "total_cost": "float",
        "total_pay": "float",
        "pay_run_status": "str",
        "pay_run_type": "str",
        "calendar_type": "str",
        "posted_date_time": "date",
        "pay_slips": "list[Payslip]",
    }
    attribute_map = {
        "pay_run_id": "payRunID",
        "payroll_calendar_id": "payrollCalendarID",
        "period_start_date": "periodStartDate",
        "period_end_date": "periodEndDate",
        "payment_date": "paymentDate",
        "total_cost": "totalCost",
        "total_pay": "totalPay",
        "pay_run_status": "payRunStatus",
        "pay_run_type": "payRunType",
        "calendar_type": "calendarType",
        "posted_date_time": "postedDateTime",
        "pay_slips": "paySlips",
    }

    def __init__(
        self,
        pay_run_id=None,
        payroll_calendar_id=None,
        period_start_date=None,
        period_end_date=None,
        payment_date=None,
        total_cost=None,
        total_pay=None,
        pay_run_status=None,
        pay_run_type=None,
        calendar_type=None,
        posted_date_time=None,
        pay_slips=None,
    ):
        self._pay_run_id = None
        self._payroll_calendar_id = None
        self._period_start_date = None
        self._period_end_date = None
        self._payment_date = None
        self._total_cost = None
        self._total_pay = None
        self._pay_run_status = None
        self._pay_run_type = None
        self._calendar_type = None
        self._posted_date_time = None
        self._pay_slips = None
        self.discriminator = None
        if pay_run_id is not None:
            self.pay_run_id = pay_run_id
        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        if period_start_date is not None:
            self.period_start_date = period_start_date
        if period_end_date is not None:
            self.period_end_date = period_end_date
        if payment_date is not None:
            self.payment_date = payment_date
        if total_cost is not None:
            self.total_cost = total_cost
        if total_pay is not None:
            self.total_pay = total_pay
        if pay_run_status is not None:
            self.pay_run_status = pay_run_status
        if pay_run_type is not None:
            self.pay_run_type = pay_run_type
        if calendar_type is not None:
            self.calendar_type = calendar_type
        if posted_date_time is not None:
            self.posted_date_time = posted_date_time
        if pay_slips is not None:
            self.pay_slips = pay_slips

    @property
    def pay_run_id(self):
        return self._pay_run_id

    @pay_run_id.setter
    def pay_run_id(self, pay_run_id):
        self._pay_run_id = pay_run_id

    @property
    def payroll_calendar_id(self):
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        self._payroll_calendar_id = payroll_calendar_id

    @property
    def period_start_date(self):
        return self._period_start_date

    @period_start_date.setter
    def period_start_date(self, period_start_date):
        self._period_start_date = period_start_date

    @property
    def period_end_date(self):
        return self._period_end_date

    @period_end_date.setter
    def period_end_date(self, period_end_date):
        self._period_end_date = period_end_date

    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        self._payment_date = payment_date

    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        self._total_cost = total_cost

    @property
    def total_pay(self):
        return self._total_pay

    @total_pay.setter
    def total_pay(self, total_pay):
        self._total_pay = total_pay

    @property
    def pay_run_status(self):
        return self._pay_run_status

    @pay_run_status.setter
    def pay_run_status(self, pay_run_status):
        allowed_values = ["Draft", "Posted", "None"]
        if pay_run_status:
            if pay_run_status not in allowed_values:
                raise ValueError(
                    "Invalid value for `pay_run_status` ({0}), must be one of {1}".format(
                        pay_run_status, allowed_values
                    )
                )
        self._pay_run_status = pay_run_status

    @property
    def pay_run_type(self):
        return self._pay_run_type

    @pay_run_type.setter
    def pay_run_type(self, pay_run_type):
        allowed_values = [
            "Scheduled",
            "Unscheduled",
            "EarlierYearUpdate",
            "None",
        ]
        if pay_run_type:
            if pay_run_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `pay_run_type` ({0}), must be one of {1}".format(
                        pay_run_type, allowed_values
                    )
                )
        self._pay_run_type = pay_run_type

    @property
    def calendar_type(self):
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type):
        allowed_values = [
            "Weekly",
            "Fortnightly",
            "FourWeekly",
            "Monthly",
            "Annual",
            "Quarterly",
            "None",
        ]
        if calendar_type:
            if calendar_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `calendar_type` ({0}), must be one of {1}".format(
                        calendar_type, allowed_values
                    )
                )
        self._calendar_type = calendar_type

    @property
    def posted_date_time(self):
        return self._posted_date_time

    @posted_date_time.setter
    def posted_date_time(self, posted_date_time):
        self._posted_date_time = posted_date_time

    @property
    def pay_slips(self):
        return self._pay_slips

    @pay_slips.setter
    def pay_slips(self, pay_slips):
        self._pay_slips = pay_slips
