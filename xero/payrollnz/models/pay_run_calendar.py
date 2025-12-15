from xero.models import BaseModel


class PayRunCalendar(BaseModel):
    openapi_types = {
        "payroll_calendar_id": "str",
        "name": "str",
        "calendar_type": "CalendarType",
        "period_start_date": "date",
        "period_end_date": "date",
        "payment_date": "date",
        "updated_date_utc": "datetime",
    }
    attribute_map = {
        "payroll_calendar_id": "payrollCalendarID",
        "name": "name",
        "calendar_type": "calendarType",
        "period_start_date": "periodStartDate",
        "period_end_date": "periodEndDate",
        "payment_date": "paymentDate",
        "updated_date_utc": "updatedDateUTC",
    }

    def __init__(
        self,
        payroll_calendar_id=None,
        name=None,
        calendar_type=None,
        period_start_date=None,
        period_end_date=None,
        payment_date=None,
        updated_date_utc=None,
    ):
        self._payroll_calendar_id = None
        self._name = None
        self._calendar_type = None
        self._period_start_date = None
        self._period_end_date = None
        self._payment_date = None
        self._updated_date_utc = None
        self.discriminator = None
        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        self.name = name
        self.calendar_type = calendar_type
        self.period_start_date = period_start_date
        if period_end_date is not None:
            self.period_end_date = period_end_date
        self.payment_date = payment_date
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def payroll_calendar_id(self):
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        self._payroll_calendar_id = payroll_calendar_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def calendar_type(self):
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type):
        if calendar_type is None:
            raise ValueError("Invalid value for `calendar_type`, must not be `None`")
        self._calendar_type = calendar_type

    @property
    def period_start_date(self):
        return self._period_start_date

    @period_start_date.setter
    def period_start_date(self, period_start_date):
        if period_start_date is None:
            raise ValueError(
                "Invalid value for `period_start_date`, must not be `None`"
            )
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
        if payment_date is None:
            raise ValueError("Invalid value for `payment_date`, must not be `None`")
        self._payment_date = payment_date

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc
