from xero.models import BaseModel


class EmployeeOpeningBalance(BaseModel):
    openapi_types = {
        "period_end_date": "date",
        "days_paid": "int",
        "unpaid_weeks": "int",
        "gross_earnings": "float",
    }
    attribute_map = {
        "period_end_date": "periodEndDate",
        "days_paid": "daysPaid",
        "unpaid_weeks": "unpaidWeeks",
        "gross_earnings": "grossEarnings",
    }

    def __init__(
        self,
        period_end_date=None,
        days_paid=None,
        unpaid_weeks=None,
        gross_earnings=None,
    ):
        self._period_end_date = None
        self._days_paid = None
        self._unpaid_weeks = None
        self._gross_earnings = None
        self.discriminator = None
        if period_end_date is not None:
            self.period_end_date = period_end_date
        if days_paid is not None:
            self.days_paid = days_paid
        if unpaid_weeks is not None:
            self.unpaid_weeks = unpaid_weeks
        if gross_earnings is not None:
            self.gross_earnings = gross_earnings

    @property
    def period_end_date(self):
        return self._period_end_date

    @period_end_date.setter
    def period_end_date(self, period_end_date):
        self._period_end_date = period_end_date

    @property
    def days_paid(self):
        return self._days_paid

    @days_paid.setter
    def days_paid(self, days_paid):
        self._days_paid = days_paid

    @property
    def unpaid_weeks(self):
        return self._unpaid_weeks

    @unpaid_weeks.setter
    def unpaid_weeks(self, unpaid_weeks):
        self._unpaid_weeks = unpaid_weeks

    @property
    def gross_earnings(self):
        return self._gross_earnings

    @gross_earnings.setter
    def gross_earnings(self, gross_earnings):
        self._gross_earnings = gross_earnings
