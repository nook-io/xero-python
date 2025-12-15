from xero.models import BaseModel


class PaymentMethod(BaseModel):
    openapi_types = {"payment_method": "str", "bank_accounts": "list[BankAccount]"}
    attribute_map = {"payment_method": "paymentMethod", "bank_accounts": "bankAccounts"}

    def __init__(self, payment_method=None, bank_accounts=None):
        self._payment_method = None
        self._bank_accounts = None
        self.discriminator = None
        if payment_method is not None:
            self.payment_method = payment_method
        if bank_accounts is not None:
            self.bank_accounts = bank_accounts

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        allowed_values = ["Cheque", "Electronically", "Manual", "None"]
        if payment_method:
            if payment_method not in allowed_values:
                raise ValueError(
                    "Invalid value for `payment_method` ({0}), must be one of {1}".format(
                        payment_method, allowed_values
                    )
                )
        self._payment_method = payment_method

    @property
    def bank_accounts(self):
        return self._bank_accounts

    @bank_accounts.setter
    def bank_accounts(self, bank_accounts):
        self._bank_accounts = bank_accounts
