from xero.models import BaseModel


class LinkedTransactions(BaseModel):
    openapi_types = {"linked_transactions": "list[LinkedTransaction]"}
    attribute_map = {"linked_transactions": "LinkedTransactions"}

    def __init__(self, linked_transactions=None):
        self._linked_transactions = None
        self.discriminator = None
        if linked_transactions is not None:
            self.linked_transactions = linked_transactions

    @property
    def linked_transactions(self):
        return self._linked_transactions

    @linked_transactions.setter
    def linked_transactions(self, linked_transactions):
        self._linked_transactions = linked_transactions
