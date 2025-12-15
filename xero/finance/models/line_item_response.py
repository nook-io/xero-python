from xero.models import BaseModel


class LineItemResponse(BaseModel):
    openapi_types = {
        "account_id": "str",
        "reporting_code": "str",
        "line_amount": "float",
        "account_type": "str",
    }
    attribute_map = {
        "account_id": "accountId",
        "reporting_code": "reportingCode",
        "line_amount": "lineAmount",
        "account_type": "accountType",
    }

    def __init__(
        self, account_id=None, reporting_code=None, line_amount=None, account_type=None
    ):
        self._account_id = None
        self._reporting_code = None
        self._line_amount = None
        self._account_type = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if reporting_code is not None:
            self.reporting_code = reporting_code
        if line_amount is not None:
            self.line_amount = line_amount
        if account_type is not None:
            self.account_type = account_type

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def reporting_code(self):
        return self._reporting_code

    @reporting_code.setter
    def reporting_code(self, reporting_code):
        self._reporting_code = reporting_code

    @property
    def line_amount(self):
        return self._line_amount

    @line_amount.setter
    def line_amount(self, line_amount):
        self._line_amount = line_amount

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        self._account_type = account_type
