from xero.models import BaseModel


class DeductionLine(BaseModel):
    openapi_types = {
        "deduction_type_id": "str",
        "display_name": "str",
        "amount": "float",
        "subject_to_tax": "bool",
        "percentage": "float",
    }
    attribute_map = {
        "deduction_type_id": "deductionTypeID",
        "display_name": "displayName",
        "amount": "amount",
        "subject_to_tax": "subjectToTax",
        "percentage": "percentage",
    }

    def __init__(
        self,
        deduction_type_id=None,
        display_name=None,
        amount=None,
        subject_to_tax=None,
        percentage=None,
    ):
        self._deduction_type_id = None
        self._display_name = None
        self._amount = None
        self._subject_to_tax = None
        self._percentage = None
        self.discriminator = None
        if deduction_type_id is not None:
            self.deduction_type_id = deduction_type_id
        if display_name is not None:
            self.display_name = display_name
        if amount is not None:
            self.amount = amount
        if subject_to_tax is not None:
            self.subject_to_tax = subject_to_tax
        if percentage is not None:
            self.percentage = percentage

    @property
    def deduction_type_id(self):
        return self._deduction_type_id

    @deduction_type_id.setter
    def deduction_type_id(self, deduction_type_id):
        self._deduction_type_id = deduction_type_id

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        self._display_name = display_name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def subject_to_tax(self):
        return self._subject_to_tax

    @subject_to_tax.setter
    def subject_to_tax(self, subject_to_tax):
        self._subject_to_tax = subject_to_tax

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage
