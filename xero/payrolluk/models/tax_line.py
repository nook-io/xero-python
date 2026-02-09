from xero.models import BaseModel


class TaxLine(BaseModel):
    openapi_types = {
        "tax_line_id": "str",
        "description": "str",
        "is_employer_tax": "bool",
        "amount": "float",
        "global_tax_type_id": "str",
        "manual_adjustment": "bool",
    }
    attribute_map = {
        "tax_line_id": "taxLineID",
        "description": "description",
        "is_employer_tax": "isEmployerTax",
        "amount": "amount",
        "global_tax_type_id": "globalTaxTypeID",
        "manual_adjustment": "manualAdjustment",
    }

    def __init__(
        self,
        tax_line_id=None,
        description=None,
        is_employer_tax=None,
        amount=None,
        global_tax_type_id=None,
        manual_adjustment=None,
    ):
        self._tax_line_id = None
        self._description = None
        self._is_employer_tax = None
        self._amount = None
        self._global_tax_type_id = None
        self._manual_adjustment = None
        self.discriminator = None
        if tax_line_id is not None:
            self.tax_line_id = tax_line_id
        if description is not None:
            self.description = description
        if is_employer_tax is not None:
            self.is_employer_tax = is_employer_tax
        if amount is not None:
            self.amount = amount
        if global_tax_type_id is not None:
            self.global_tax_type_id = global_tax_type_id
        if manual_adjustment is not None:
            self.manual_adjustment = manual_adjustment

    @property
    def tax_line_id(self):
        return self._tax_line_id

    @tax_line_id.setter
    def tax_line_id(self, tax_line_id):
        self._tax_line_id = tax_line_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def is_employer_tax(self):
        return self._is_employer_tax

    @is_employer_tax.setter
    def is_employer_tax(self, is_employer_tax):
        self._is_employer_tax = is_employer_tax

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def global_tax_type_id(self):
        return self._global_tax_type_id

    @global_tax_type_id.setter
    def global_tax_type_id(self, global_tax_type_id):
        self._global_tax_type_id = global_tax_type_id

    @property
    def manual_adjustment(self):
        return self._manual_adjustment

    @manual_adjustment.setter
    def manual_adjustment(self, manual_adjustment):
        self._manual_adjustment = manual_adjustment
