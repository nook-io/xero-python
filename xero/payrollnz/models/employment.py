from xero.models import BaseModel


class Employment(BaseModel):
    openapi_types = {
        "payroll_calendar_id": "str",
        "pay_run_calendar_id": "str",
        "start_date": "date",
        "engagement_type": "str",
        "fixed_term_end_date": "date",
    }
    attribute_map = {
        "payroll_calendar_id": "payrollCalendarID",
        "pay_run_calendar_id": "payRunCalendarID",
        "start_date": "startDate",
        "engagement_type": "engagementType",
        "fixed_term_end_date": "fixedTermEndDate",
    }

    def __init__(
        self,
        payroll_calendar_id=None,
        pay_run_calendar_id=None,
        start_date=None,
        engagement_type=None,
        fixed_term_end_date=None,
    ):
        self._payroll_calendar_id = None
        self._pay_run_calendar_id = None
        self._start_date = None
        self._engagement_type = None
        self._fixed_term_end_date = None
        self.discriminator = None
        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        if pay_run_calendar_id is not None:
            self.pay_run_calendar_id = pay_run_calendar_id
        if start_date is not None:
            self.start_date = start_date
        if engagement_type is not None:
            self.engagement_type = engagement_type
        if fixed_term_end_date is not None:
            self.fixed_term_end_date = fixed_term_end_date

    @property
    def payroll_calendar_id(self):
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        self._payroll_calendar_id = payroll_calendar_id

    @property
    def pay_run_calendar_id(self):
        return self._pay_run_calendar_id

    @pay_run_calendar_id.setter
    def pay_run_calendar_id(self, pay_run_calendar_id):
        self._pay_run_calendar_id = pay_run_calendar_id

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def engagement_type(self):
        return self._engagement_type

    @engagement_type.setter
    def engagement_type(self, engagement_type):
        self._engagement_type = engagement_type

    @property
    def fixed_term_end_date(self):
        return self._fixed_term_end_date

    @fixed_term_end_date.setter
    def fixed_term_end_date(self, fixed_term_end_date):
        self._fixed_term_end_date = fixed_term_end_date
