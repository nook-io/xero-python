from xero.models import BaseModel


class PaymentLine(BaseModel):
    openapi_types = {
        "payment_line_id": "str",
        "amount": "float",
        "account_number": "str",
        "sort_code": "str",
        "account_name": "str",
    }
    attribute_map = {
        "payment_line_id": "paymentLineID",
        "amount": "amount",
        "account_number": "accountNumber",
        "sort_code": "sortCode",
        "account_name": "accountName",
    }

    def __init__(
        self,
        payment_line_id=None,
        amount=None,
        account_number=None,
        sort_code=None,
        account_name=None,
    ):
        self._payment_line_id = None
        self._amount = None
        self._account_number = None
        self._sort_code = None
        self._account_name = None
        self.discriminator = None
        if payment_line_id is not None:
            self.payment_line_id = payment_line_id
        if amount is not None:
            self.amount = amount
        if account_number is not None:
            self.account_number = account_number
        if sort_code is not None:
            self.sort_code = sort_code
        if account_name is not None:
            self.account_name = account_name

    @property
    def payment_line_id(self):
        return self._payment_line_id

    @payment_line_id.setter
    def payment_line_id(self, payment_line_id):
        self._payment_line_id = payment_line_id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        self._account_number = account_number

    @property
    def sort_code(self):
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        self._sort_code = sort_code

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        self._account_name = account_name
