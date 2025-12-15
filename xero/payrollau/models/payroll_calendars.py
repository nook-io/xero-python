from xero.models import BaseModel


class PayrollCalendars(BaseModel):
    openapi_types = {"payroll_calendars": "list[PayrollCalendar]"}
    attribute_map = {"payroll_calendars": "PayrollCalendars"}

    def __init__(self, payroll_calendars=None):
        self._payroll_calendars = None
        self.discriminator = None
        if payroll_calendars is not None:
            self.payroll_calendars = payroll_calendars

    @property
    def payroll_calendars(self):
        return self._payroll_calendars

    @payroll_calendars.setter
    def payroll_calendars(self, payroll_calendars):
        self._payroll_calendars = payroll_calendars
