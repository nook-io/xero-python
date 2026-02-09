from xero.models import BaseModel


class AccountUsageResponse(BaseModel):
    openapi_types = {
        "organisation_id": "str",
        "start_month": "str",
        "end_month": "str",
        "account_usage": "list[AccountUsage]",
    }
    attribute_map = {
        "organisation_id": "organisationId",
        "start_month": "startMonth",
        "end_month": "endMonth",
        "account_usage": "accountUsage",
    }

    def __init__(
        self, organisation_id=None, start_month=None, end_month=None, account_usage=None
    ):
        self._organisation_id = None
        self._start_month = None
        self._end_month = None
        self._account_usage = None
        self.discriminator = None
        if organisation_id is not None:
            self.organisation_id = organisation_id
        if start_month is not None:
            self.start_month = start_month
        if end_month is not None:
            self.end_month = end_month
        if account_usage is not None:
            self.account_usage = account_usage

    @property
    def organisation_id(self):
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        self._organisation_id = organisation_id

    @property
    def start_month(self):
        return self._start_month

    @start_month.setter
    def start_month(self, start_month):
        self._start_month = start_month

    @property
    def end_month(self):
        return self._end_month

    @end_month.setter
    def end_month(self, end_month):
        self._end_month = end_month

    @property
    def account_usage(self):
        return self._account_usage

    @account_usage.setter
    def account_usage(self, account_usage):
        self._account_usage = account_usage
