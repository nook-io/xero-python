from xero.models import BaseModel


class CashflowResponse(BaseModel):
    openapi_types = {
        "start_date": "date",
        "end_date": "date",
        "cash_balance": "CashBalance",
        "cashflow_activities": "list[CashflowActivity]",
    }
    attribute_map = {
        "start_date": "startDate",
        "end_date": "endDate",
        "cash_balance": "cashBalance",
        "cashflow_activities": "cashflowActivities",
    }

    def __init__(
        self,
        start_date=None,
        end_date=None,
        cash_balance=None,
        cashflow_activities=None,
    ):
        self._start_date = None
        self._end_date = None
        self._cash_balance = None
        self._cashflow_activities = None
        self.discriminator = None
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if cash_balance is not None:
            self.cash_balance = cash_balance
        if cashflow_activities is not None:
            self.cashflow_activities = cashflow_activities

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @property
    def cash_balance(self):
        return self._cash_balance

    @cash_balance.setter
    def cash_balance(self, cash_balance):
        self._cash_balance = cash_balance

    @property
    def cashflow_activities(self):
        return self._cashflow_activities

    @cashflow_activities.setter
    def cashflow_activities(self, cashflow_activities):
        self._cashflow_activities = cashflow_activities
