from xero.models import BaseModel


class Element(BaseModel):
    openapi_types = {
        "validation_errors": "list[ValidationError]",
        "batch_payment_id": "str",
        "bank_transaction_id": "str",
        "credit_note_id": "str",
        "contact_id": "str",
        "invoice_id": "str",
        "item_id": "str",
        "purchase_order_id": "str",
    }
    attribute_map = {
        "validation_errors": "ValidationErrors",
        "batch_payment_id": "BatchPaymentID",
        "bank_transaction_id": "BankTransactionID",
        "credit_note_id": "CreditNoteID",
        "contact_id": "ContactID",
        "invoice_id": "InvoiceID",
        "item_id": "ItemID",
        "purchase_order_id": "PurchaseOrderID",
    }

    def __init__(
        self,
        validation_errors=None,
        batch_payment_id=None,
        bank_transaction_id=None,
        credit_note_id=None,
        contact_id=None,
        invoice_id=None,
        item_id=None,
        purchase_order_id=None,
    ):
        self._validation_errors = None
        self._batch_payment_id = None
        self._bank_transaction_id = None
        self._credit_note_id = None
        self._contact_id = None
        self._invoice_id = None
        self._item_id = None
        self._purchase_order_id = None
        self.discriminator = None
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if batch_payment_id is not None:
            self.batch_payment_id = batch_payment_id
        if bank_transaction_id is not None:
            self.bank_transaction_id = bank_transaction_id
        if credit_note_id is not None:
            self.credit_note_id = credit_note_id
        if contact_id is not None:
            self.contact_id = contact_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if item_id is not None:
            self.item_id = item_id
        if purchase_order_id is not None:
            self.purchase_order_id = purchase_order_id

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors

    @property
    def batch_payment_id(self):
        return self._batch_payment_id

    @batch_payment_id.setter
    def batch_payment_id(self, batch_payment_id):
        self._batch_payment_id = batch_payment_id

    @property
    def bank_transaction_id(self):
        return self._bank_transaction_id

    @bank_transaction_id.setter
    def bank_transaction_id(self, bank_transaction_id):
        self._bank_transaction_id = bank_transaction_id

    @property
    def credit_note_id(self):
        return self._credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, credit_note_id):
        self._credit_note_id = credit_note_id

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        self._invoice_id = invoice_id

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        self._item_id = item_id

    @property
    def purchase_order_id(self):
        return self._purchase_order_id

    @purchase_order_id.setter
    def purchase_order_id(self, purchase_order_id):
        self._purchase_order_id = purchase_order_id
