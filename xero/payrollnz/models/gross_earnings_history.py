from xero.models import BaseModel


class GrossEarningsHistory(BaseModel):
    openapi_types = {"days_paid": "int", "unpaid_weeks": "int"}
    attribute_map = {"days_paid": "daysPaid", "unpaid_weeks": "unpaidWeeks"}

    def __init__(self, days_paid=None, unpaid_weeks=None):
        self._days_paid = None
        self._unpaid_weeks = None
        self.discriminator = None
        if days_paid is not None:
            self.days_paid = days_paid
        if unpaid_weeks is not None:
            self.unpaid_weeks = unpaid_weeks

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
