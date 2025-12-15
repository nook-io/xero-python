from xero.models import BaseModel


class StatementLineResponse(BaseModel):
    openapi_types = {
        "statement_line_id": "str",
        "posted_date": "date",
        "payee": "str",
        "reference": "str",
        "notes": "str",
        "cheque_no": "str",
        "amount": "float",
        "transaction_date": "date",
        "type": "str",
        "is_reconciled": "bool",
        "is_duplicate": "bool",
        "is_deleted": "bool",
        "payments": "list[PaymentResponse]",
        "bank_transactions": "list[BankTransactionResponse]",
    }
    attribute_map = {
        "statement_line_id": "statementLineId",
        "posted_date": "postedDate",
        "payee": "payee",
        "reference": "reference",
        "notes": "notes",
        "cheque_no": "chequeNo",
        "amount": "amount",
        "transaction_date": "transactionDate",
        "type": "type",
        "is_reconciled": "isReconciled",
        "is_duplicate": "isDuplicate",
        "is_deleted": "isDeleted",
        "payments": "payments",
        "bank_transactions": "bankTransactions",
    }

    def __init__(
        self,
        statement_line_id=None,
        posted_date=None,
        payee=None,
        reference=None,
        notes=None,
        cheque_no=None,
        amount=None,
        transaction_date=None,
        type=None,
        is_reconciled=None,
        is_duplicate=None,
        is_deleted=None,
        payments=None,
        bank_transactions=None,
    ):
        self._statement_line_id = None
        self._posted_date = None
        self._payee = None
        self._reference = None
        self._notes = None
        self._cheque_no = None
        self._amount = None
        self._transaction_date = None
        self._type = None
        self._is_reconciled = None
        self._is_duplicate = None
        self._is_deleted = None
        self._payments = None
        self._bank_transactions = None
        self.discriminator = None
        if statement_line_id is not None:
            self.statement_line_id = statement_line_id
        if posted_date is not None:
            self.posted_date = posted_date
        if payee is not None:
            self.payee = payee
        if reference is not None:
            self.reference = reference
        if notes is not None:
            self.notes = notes
        if cheque_no is not None:
            self.cheque_no = cheque_no
        if amount is not None:
            self.amount = amount
        if transaction_date is not None:
            self.transaction_date = transaction_date
        if type is not None:
            self.type = type
        if is_reconciled is not None:
            self.is_reconciled = is_reconciled
        if is_duplicate is not None:
            self.is_duplicate = is_duplicate
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if payments is not None:
            self.payments = payments
        if bank_transactions is not None:
            self.bank_transactions = bank_transactions

    @property
    def statement_line_id(self):
        return self._statement_line_id

    @statement_line_id.setter
    def statement_line_id(self, statement_line_id):
        self._statement_line_id = statement_line_id

    @property
    def posted_date(self):
        return self._posted_date

    @posted_date.setter
    def posted_date(self, posted_date):
        self._posted_date = posted_date

    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, payee):
        self._payee = payee

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    @property
    def cheque_no(self):
        return self._cheque_no

    @cheque_no.setter
    def cheque_no(self, cheque_no):
        self._cheque_no = cheque_no

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def transaction_date(self):
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        self._transaction_date = transaction_date

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def is_reconciled(self):
        return self._is_reconciled

    @is_reconciled.setter
    def is_reconciled(self, is_reconciled):
        self._is_reconciled = is_reconciled

    @property
    def is_duplicate(self):
        return self._is_duplicate

    @is_duplicate.setter
    def is_duplicate(self, is_duplicate):
        self._is_duplicate = is_duplicate

    @property
    def is_deleted(self):
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        self._is_deleted = is_deleted

    @property
    def payments(self):
        return self._payments

    @payments.setter
    def payments(self, payments):
        self._payments = payments

    @property
    def bank_transactions(self):
        return self._bank_transactions

    @bank_transactions.setter
    def bank_transactions(self, bank_transactions):
        self._bank_transactions = bank_transactions
