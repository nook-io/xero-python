from xero.models import BaseModel


class TrialBalanceAccount(BaseModel):
    openapi_types = {
        "account_id": "str",
        "account_type": "str",
        "account_code": "str",
        "account_class": "str",
        "status": "str",
        "reporting_code": "str",
        "account_name": "str",
        "balance": "TrialBalanceEntry",
        "signed_balance": "float",
        "account_movement": "TrialBalanceMovement",
    }
    attribute_map = {
        "account_id": "accountId",
        "account_type": "accountType",
        "account_code": "accountCode",
        "account_class": "accountClass",
        "status": "status",
        "reporting_code": "reportingCode",
        "account_name": "accountName",
        "balance": "balance",
        "signed_balance": "signedBalance",
        "account_movement": "accountMovement",
    }

    def __init__(
        self,
        account_id=None,
        account_type=None,
        account_code=None,
        account_class=None,
        status=None,
        reporting_code=None,
        account_name=None,
        balance=None,
        signed_balance=None,
        account_movement=None,
    ):
        self._account_id = None
        self._account_type = None
        self._account_code = None
        self._account_class = None
        self._status = None
        self._reporting_code = None
        self._account_name = None
        self._balance = None
        self._signed_balance = None
        self._account_movement = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if account_type is not None:
            self.account_type = account_type
        if account_code is not None:
            self.account_code = account_code
        if account_class is not None:
            self.account_class = account_class
        if status is not None:
            self.status = status
        if reporting_code is not None:
            self.reporting_code = reporting_code
        if account_name is not None:
            self.account_name = account_name
        if balance is not None:
            self.balance = balance
        if signed_balance is not None:
            self.signed_balance = signed_balance
        if account_movement is not None:
            self.account_movement = account_movement

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
    def account_code(self):
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        self._account_code = account_code

    @property
    def account_class(self):
        return self._account_class

    @account_class.setter
    def account_class(self, account_class):
        self._account_class = account_class

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def reporting_code(self):
        return self._reporting_code

    @reporting_code.setter
    def reporting_code(self, reporting_code):
        self._reporting_code = reporting_code

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        self._account_name = account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def signed_balance(self):
        return self._signed_balance

    @signed_balance.setter
    def signed_balance(self, signed_balance):
        self._signed_balance = signed_balance

    @property
    def account_movement(self):
        return self._account_movement

    @account_movement.setter
    def account_movement(self, account_movement):
        self._account_movement = account_movement
