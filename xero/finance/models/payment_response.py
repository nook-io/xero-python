from xero.models import BaseModel


class PaymentResponse(BaseModel):
    openapi_types = {
        "payment_id": "str",
        "batch_payment_id": "str",
        "date": "date",
        "amount": "float",
        "bank_amount": "float",
        "currency_rate": "float",
        "invoice": "InvoiceResponse",
        "credit_note": "CreditNoteResponse",
        "prepayment": "PrepaymentResponse",
        "overpayment": "OverpaymentResponse",
    }
    attribute_map = {
        "payment_id": "paymentId",
        "batch_payment_id": "batchPaymentId",
        "date": "date",
        "amount": "amount",
        "bank_amount": "bankAmount",
        "currency_rate": "currencyRate",
        "invoice": "invoice",
        "credit_note": "creditNote",
        "prepayment": "prepayment",
        "overpayment": "overpayment",
    }

    def __init__(
        self,
        payment_id=None,
        batch_payment_id=None,
        date=None,
        amount=None,
        bank_amount=None,
        currency_rate=None,
        invoice=None,
        credit_note=None,
        prepayment=None,
        overpayment=None,
    ):
        self._payment_id = None
        self._batch_payment_id = None
        self._date = None
        self._amount = None
        self._bank_amount = None
        self._currency_rate = None
        self._invoice = None
        self._credit_note = None
        self._prepayment = None
        self._overpayment = None
        self.discriminator = None
        if payment_id is not None:
            self.payment_id = payment_id
        if batch_payment_id is not None:
            self.batch_payment_id = batch_payment_id
        if date is not None:
            self.date = date
        if amount is not None:
            self.amount = amount
        if bank_amount is not None:
            self.bank_amount = bank_amount
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if invoice is not None:
            self.invoice = invoice
        if credit_note is not None:
            self.credit_note = credit_note
        if prepayment is not None:
            self.prepayment = prepayment
        if overpayment is not None:
            self.overpayment = overpayment

    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        self._payment_id = payment_id

    @property
    def batch_payment_id(self):
        return self._batch_payment_id

    @batch_payment_id.setter
    def batch_payment_id(self, batch_payment_id):
        self._batch_payment_id = batch_payment_id

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
    def bank_amount(self):
        return self._bank_amount

    @bank_amount.setter
    def bank_amount(self, bank_amount):
        self._bank_amount = bank_amount

    @property
    def currency_rate(self):
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        self._currency_rate = currency_rate

    @property
    def invoice(self):
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        self._invoice = invoice

    @property
    def credit_note(self):
        return self._credit_note

    @credit_note.setter
    def credit_note(self, credit_note):
        self._credit_note = credit_note

    @property
    def prepayment(self):
        return self._prepayment

    @prepayment.setter
    def prepayment(self, prepayment):
        self._prepayment = prepayment

    @property
    def overpayment(self):
        return self._overpayment

    @overpayment.setter
    def overpayment(self, overpayment):
        self._overpayment = overpayment
