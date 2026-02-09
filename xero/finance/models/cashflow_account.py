from xero.models import BaseModel


class CashflowAccount(BaseModel):
    openapi_types = {
        "account_id": "str",
        "account_type": "str",
        "account_class": "str",
        "code": "str",
        "name": "str",
        "reporting_code": "str",
        "total": "float",
    }
    attribute_map = {
        "account_id": "accountId",
        "account_type": "accountType",
        "account_class": "accountClass",
        "code": "code",
        "name": "name",
        "reporting_code": "reportingCode",
        "total": "total",
    }

    def __init__(
        self,
        account_id=None,
        account_type=None,
        account_class=None,
        code=None,
        name=None,
        reporting_code=None,
        total=None,
    ):
        self._account_id = None
        self._account_type = None
        self._account_class = None
        self._code = None
        self._name = None
        self._reporting_code = None
        self._total = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if account_type is not None:
            self.account_type = account_type
        if account_class is not None:
            self.account_class = account_class
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if reporting_code is not None:
            self.reporting_code = reporting_code
        if total is not None:
            self.total = total

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        self._account_type = account_type

    @property
    def account_class(self):
        return self._account_class

    @account_class.setter
    def account_class(self, account_class):
        self._account_class = account_class

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

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
