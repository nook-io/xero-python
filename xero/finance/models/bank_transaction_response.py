from xero.models import BaseModel


class BankTransactionResponse(BaseModel):
    openapi_types = {
        "bank_transaction_id": "str",
        "batch_payment_id": "str",
        "contact": "ContactResponse",
        "date": "date",
        "amount": "float",
        "line_items": "list[LineItemResponse]",
    }
    attribute_map = {
        "bank_transaction_id": "bankTransactionId",
        "batch_payment_id": "batchPaymentId",
        "contact": "contact",
        "date": "date",
        "amount": "amount",
        "line_items": "lineItems",
    }

    def __init__(
        self,
        bank_transaction_id=None,
        batch_payment_id=None,
        contact=None,
        date=None,
        amount=None,
        line_items=None,
    ):
        self._bank_transaction_id = None
        self._batch_payment_id = None
        self._contact = None
        self._date = None
        self._amount = None
        self._line_items = None
        self.discriminator = None
        if bank_transaction_id is not None:
            self.bank_transaction_id = bank_transaction_id
        if batch_payment_id is not None:
            self.batch_payment_id = batch_payment_id
        if contact is not None:
            self.contact = contact
        if date is not None:
            self.date = date
        if amount is not None:
            self.amount = amount
        if line_items is not None:
            self.line_items = line_items

    @property
    def bank_transaction_id(self):
        return self._bank_transaction_id

    @bank_transaction_id.setter
    def bank_transaction_id(self, bank_transaction_id):
        self._bank_transaction_id = bank_transaction_id

    @property
    def batch_payment_id(self):
        return self._batch_payment_id

    @batch_payment_id.setter
    def batch_payment_id(self, batch_payment_id):
        self._batch_payment_id = batch_payment_id

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def line_items(self):
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        self._line_items = line_items
