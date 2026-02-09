from xero.models import BaseModel


class BankTransactions(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "warnings": "list[ValidationError]",
        "bank_transactions": "list[BankTransaction]",
    }
    attribute_map = {
        "pagination": "pagination",
        "warnings": "Warnings",
        "bank_transactions": "BankTransactions",
    }

    def __init__(self, pagination=None, warnings=None, bank_transactions=None):
        self._pagination = None
        self._warnings = None
        self._bank_transactions = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if warnings is not None:
            self.warnings = warnings
        if bank_transactions is not None:
            self.bank_transactions = bank_transactions

    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        self._pagination = pagination

    @property
    def warnings(self):
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        self._warnings = warnings

    @property
    def bank_transactions(self):
        return self._bank_transactions

    @bank_transactions.setter
    def bank_transactions(self, bank_transactions):
        self._bank_transactions = bank_transactions
