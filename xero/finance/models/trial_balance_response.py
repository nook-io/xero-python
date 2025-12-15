from xero.models import BaseModel


class TrialBalanceResponse(BaseModel):
    openapi_types = {
        "start_date": "date",
        "end_date": "date",
        "accounts": "list[TrialBalanceAccount]",
    }
    attribute_map = {
        "start_date": "startDate",
        "end_date": "endDate",
        "accounts": "accounts",
    }

    def __init__(self, start_date=None, end_date=None, accounts=None):
        self._start_date = None
        self._end_date = None
        self._accounts = None
        self.discriminator = None
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if accounts is not None:
            self.accounts = accounts

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
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts
