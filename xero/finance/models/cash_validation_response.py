from xero.models import BaseModel


class CashValidationResponse(BaseModel):
    openapi_types = {
        "account_id": "str",
        "statement_balance": "StatementBalanceResponse",
        "statement_balance_date": "date",
        "bank_statement": "BankStatementResponse",
        "cash_account": "CashAccountResponse",
    }
    attribute_map = {
        "account_id": "accountId",
        "statement_balance": "statementBalance",
        "statement_balance_date": "statementBalanceDate",
        "bank_statement": "bankStatement",
        "cash_account": "cashAccount",
    }

    def __init__(
        self,
        account_id=None,
        statement_balance=None,
        statement_balance_date=None,
        bank_statement=None,
        cash_account=None,
    ):
        self._account_id = None
        self._statement_balance = None
        self._statement_balance_date = None
        self._bank_statement = None
        self._cash_account = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if statement_balance is not None:
            self.statement_balance = statement_balance
        if statement_balance_date is not None:
            self.statement_balance_date = statement_balance_date
        if bank_statement is not None:
            self.bank_statement = bank_statement
        if cash_account is not None:
            self.cash_account = cash_account

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def statement_balance(self):
        return self._statement_balance

    @statement_balance.setter
    def statement_balance(self, statement_balance):
        self._statement_balance = statement_balance

    @property
    def statement_balance_date(self):
        return self._statement_balance_date

    @statement_balance_date.setter
    def statement_balance_date(self, statement_balance_date):
        self._statement_balance_date = statement_balance_date

    @property
    def bank_statement(self):
        return self._bank_statement

    @bank_statement.setter
    def bank_statement(self, bank_statement):
        self._bank_statement = bank_statement

    @property
    def cash_account(self):
        return self._cash_account

    @cash_account.setter
    def cash_account(self, cash_account):
        self._cash_account = cash_account
