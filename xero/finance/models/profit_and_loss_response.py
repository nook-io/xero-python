from xero.models import BaseModel


class ProfitAndLossResponse(BaseModel):
    openapi_types = {
        "start_date": "date",
        "end_date": "date",
        "net_profit_loss": "float",
        "revenue": "PnlAccountClass",
        "expense": "PnlAccountClass",
    }
    attribute_map = {
        "start_date": "startDate",
        "end_date": "endDate",
        "net_profit_loss": "netProfitLoss",
        "revenue": "revenue",
        "expense": "expense",
    }

    def __init__(
        self,
        start_date=None,
        end_date=None,
        net_profit_loss=None,
        revenue=None,
        expense=None,
    ):
        self._start_date = None
        self._end_date = None
        self._net_profit_loss = None
        self._revenue = None
        self._expense = None
        self.discriminator = None
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if net_profit_loss is not None:
            self.net_profit_loss = net_profit_loss
        if revenue is not None:
            self.revenue = revenue
        if expense is not None:
            self.expense = expense

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
    def net_profit_loss(self):
        return self._net_profit_loss

    @net_profit_loss.setter
    def net_profit_loss(self, net_profit_loss):
        self._net_profit_loss = net_profit_loss

    @property
    def revenue(self):
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        self._revenue = revenue

    @property
    def expense(self):
        return self._expense

    @expense.setter
    def expense(self, expense):
        self._expense = expense
