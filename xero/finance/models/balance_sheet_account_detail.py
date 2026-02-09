from xero.models import BaseModel


class BalanceSheetAccountDetail(BaseModel):
    openapi_types = {
        "code": "str",
        "account_id": "str",
        "name": "str",
        "reporting_code": "str",
        "total": "float",
    }
    attribute_map = {
        "code": "code",
        "account_id": "accountID",
        "name": "name",
        "reporting_code": "reportingCode",
        "total": "total",
    }

    def __init__(
        self, code=None, account_id=None, name=None, reporting_code=None, total=None
    ):
        self._code = None
        self._account_id = None
        self._name = None
        self._reporting_code = None
        self._total = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if reporting_code is not None:
            self.reporting_code = reporting_code
        if total is not None:
            self.total = total

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def reporting_code(self):
        return self._reporting_code

    @reporting_code.setter
    def reporting_code(self, reporting_code):
        self._reporting_code = reporting_code

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total
