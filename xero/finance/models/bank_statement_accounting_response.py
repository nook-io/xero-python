from xero.models import BaseModel


class BankStatementAccountingResponse(BaseModel):
    openapi_types = {
        "bank_account_id": "str",
        "bank_account_name": "str",
        "bank_account_currency_code": "str",
        "statements": "list[StatementResponse]",
    }
    attribute_map = {
        "bank_account_id": "bankAccountId",
        "bank_account_name": "bankAccountName",
        "bank_account_currency_code": "bankAccountCurrencyCode",
        "statements": "statements",
    }

    def __init__(
        self,
        bank_account_id=None,
        bank_account_name=None,
        bank_account_currency_code=None,
        statements=None,
    ):
        self._bank_account_id = None
        self._bank_account_name = None
        self._bank_account_currency_code = None
        self._statements = None
        self.discriminator = None
        if bank_account_id is not None:
            self.bank_account_id = bank_account_id
        if bank_account_name is not None:
            self.bank_account_name = bank_account_name
        if bank_account_currency_code is not None:
            self.bank_account_currency_code = bank_account_currency_code
        if statements is not None:
            self.statements = statements

    @property
    def bank_account_id(self):
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        self._bank_account_id = bank_account_id

    @property
    def bank_account_name(self):
        return self._bank_account_name

    @bank_account_name.setter
    def bank_account_name(self, bank_account_name):
        self._bank_account_name = bank_account_name

    @property
    def bank_account_currency_code(self):
        return self._bank_account_currency_code

    @bank_account_currency_code.setter
    def bank_account_currency_code(self, bank_account_currency_code):
        self._bank_account_currency_code = bank_account_currency_code

    @property
    def statements(self):
        return self._statements

    @statements.setter
    def statements(self, statements):
        self._statements = statements
