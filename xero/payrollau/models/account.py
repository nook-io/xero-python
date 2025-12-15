from xero.models import BaseModel


class Account(BaseModel):
    openapi_types = {
        "account_id": "str",
        "type": "AccountType",
        "code": "str",
        "name": "str",
    }
    attribute_map = {
        "account_id": "AccountID",
        "type": "Type",
        "code": "Code",
        "name": "Name",
    }

    def __init__(self, account_id=None, type=None, code=None, name=None):
        self._account_id = None
        self._type = None
        self._code = None
        self._name = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if type is not None:
            self.type = type
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

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
