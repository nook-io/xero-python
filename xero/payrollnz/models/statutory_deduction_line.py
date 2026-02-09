from xero.models import BaseModel


class StatutoryDeductionLine(BaseModel):
    openapi_types = {
        "statutory_deduction_type_id": "str",
        "amount": "float",
        "fixed_amount": "float",
        "manual_adjustment": "bool",
    }
    attribute_map = {
        "statutory_deduction_type_id": "statutoryDeductionTypeID",
        "amount": "amount",
        "fixed_amount": "fixedAmount",
        "manual_adjustment": "manualAdjustment",
    }

    def __init__(
        self,
        statutory_deduction_type_id=None,
        amount=None,
        fixed_amount=None,
        manual_adjustment=None,
    ):
        self._statutory_deduction_type_id = None
        self._amount = None
        self._fixed_amount = None
        self._manual_adjustment = None
        self.discriminator = None
        if statutory_deduction_type_id is not None:
            self.statutory_deduction_type_id = statutory_deduction_type_id
        if amount is not None:
            self.amount = amount
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount
        if manual_adjustment is not None:
            self.manual_adjustment = manual_adjustment

    @property
    def statutory_deduction_type_id(self):
        return self._statutory_deduction_type_id

    @statutory_deduction_type_id.setter
    def statutory_deduction_type_id(self, statutory_deduction_type_id):
        self._statutory_deduction_type_id = statutory_deduction_type_id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def fixed_amount(self):
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        self._fixed_amount = fixed_amount

    @property
    def manual_adjustment(self):
        return self._manual_adjustment

    @manual_adjustment.setter
    def manual_adjustment(self, manual_adjustment):
        self._manual_adjustment = manual_adjustment
