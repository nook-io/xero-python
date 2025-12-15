from xero.models import BaseModel


class Allocation(BaseModel):
    openapi_types = {
        "allocation_id": "str",
        "invoice": "Invoice",
        "overpayment": "Overpayment",
        "prepayment": "Prepayment",
        "credit_note": "CreditNote",
        "amount": "float",
        "date": "date[ms-format]",
        "is_deleted": "bool",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "allocation_id": "AllocationID",
        "invoice": "Invoice",
        "overpayment": "Overpayment",
        "prepayment": "Prepayment",
        "credit_note": "CreditNote",
        "amount": "Amount",
        "date": "Date",
        "is_deleted": "IsDeleted",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        allocation_id=None,
        invoice=None,
        overpayment=None,
        prepayment=None,
        credit_note=None,
        amount=None,
        date=None,
        is_deleted=None,
        status_attribute_string=None,
        validation_errors=None,
    ):
        self._allocation_id = None
        self._invoice = None
        self._overpayment = None
        self._prepayment = None
        self._credit_note = None
        self._amount = None
        self._date = None
        self._is_deleted = None
        self._status_attribute_string = None
        self._validation_errors = None
        self.discriminator = None
        if allocation_id is not None:
            self.allocation_id = allocation_id
        self.invoice = invoice
        if overpayment is not None:
            self.overpayment = overpayment
        if prepayment is not None:
            self.prepayment = prepayment
        if credit_note is not None:
            self.credit_note = credit_note
        self.amount = amount
        self.date = date
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def allocation_id(self):
        return self._allocation_id

    @allocation_id.setter
    def allocation_id(self, allocation_id):
        self._allocation_id = allocation_id

    @property
    def invoice(self):
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        if invoice is None:
            raise ValueError("Invalid value for `invoice`, must not be `None`")
        self._invoice = invoice

    @property
    def overpayment(self):
        return self._overpayment

    @overpayment.setter
    def overpayment(self, overpayment):
        self._overpayment = overpayment

    @property
    def prepayment(self):
        return self._prepayment

    @prepayment.setter
    def prepayment(self, prepayment):
        self._prepayment = prepayment

    @property
    def credit_note(self):
        return self._credit_note

    @credit_note.setter
    def credit_note(self, credit_note):
        self._credit_note = credit_note

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")
        self._amount = amount

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")
        self._date = date

    @property
    def is_deleted(self):
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        self._is_deleted = is_deleted

    @property
    def status_attribute_string(self):
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
