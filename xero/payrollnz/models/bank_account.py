from xero.models import BaseModel


class BankAccount(BaseModel):
    openapi_types = {
        "account_name": "str",
        "account_number": "str",
        "sort_code": "str",
        "particulars": "str",
        "code": "str",
        "dollar_amount": "float",
        "reference": "str",
        "calculation_type": "str",
    }
    attribute_map = {
        "account_name": "accountName",
        "account_number": "accountNumber",
        "sort_code": "sortCode",
        "particulars": "particulars",
        "code": "code",
        "dollar_amount": "dollarAmount",
        "reference": "reference",
        "calculation_type": "calculationType",
    }

    def __init__(
        self,
        account_name=None,
        account_number=None,
        sort_code=None,
        particulars=None,
        code=None,
        dollar_amount=None,
        reference=None,
        calculation_type=None,
    ):
        self._account_name = None
        self._account_number = None
        self._sort_code = None
        self._particulars = None
        self._code = None
        self._dollar_amount = None
        self._reference = None
        self._calculation_type = None
        self.discriminator = None
        self.account_name = account_name
        self.account_number = account_number
        self.sort_code = sort_code
        if particulars is not None:
            self.particulars = particulars
        if code is not None:
            self.code = code
        if dollar_amount is not None:
            self.dollar_amount = dollar_amount
        if reference is not None:
            self.reference = reference
        if calculation_type is not None:
            self.calculation_type = calculation_type

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

    @property
    def particulars(self):
        return self._particulars

    @particulars.setter
    def particulars(self, particulars):
        self._particulars = particulars

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def dollar_amount(self):
        return self._dollar_amount

    @dollar_amount.setter
    def dollar_amount(self, dollar_amount):
        self._dollar_amount = dollar_amount

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def calculation_type(self):
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        allowed_values = ["FixedAmount", "Balance", "None"]
        if calculation_type:
            if calculation_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `calculation_type` ({0}), must be one of {1}".format(
                        calculation_type, allowed_values
                    )
                )
        self._calculation_type = calculation_type
