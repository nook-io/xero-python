from xero.models import BaseModel


class BankAccount(BaseModel):
    openapi_types = {"account_name": "str", "account_number": "str", "sort_code": "str"}
    attribute_map = {
        "account_name": "accountName",
        "account_number": "accountNumber",
        "sort_code": "sortCode",
    }

    def __init__(self, account_name=None, account_number=None, sort_code=None):
        self._account_name = None
        self._account_number = None
        self._sort_code = None
        self.discriminator = None
        self.account_name = account_name
        self.account_number = account_number
        self.sort_code = sort_code

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")
        self._account_name = account_name

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")
        self._account_number = account_number

    @property
    def sort_code(self):
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        if sort_code is None:
            raise ValueError("Invalid value for `sort_code`, must not be `None`")
        self._sort_code = sort_code
