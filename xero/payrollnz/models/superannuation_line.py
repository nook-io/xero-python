from xero.models import BaseModel


class SuperannuationLine(BaseModel):
    openapi_types = {
        "superannuation_type_id": "str",
        "display_name": "str",
        "amount": "float",
        "fixed_amount": "float",
        "percentage": "float",
        "manual_adjustment": "bool",
    }
    attribute_map = {
        "superannuation_type_id": "superannuationTypeID",
        "display_name": "displayName",
        "amount": "amount",
        "fixed_amount": "fixedAmount",
        "percentage": "percentage",
        "manual_adjustment": "manualAdjustment",
    }

    def __init__(
        self,
        superannuation_type_id=None,
        display_name=None,
        amount=None,
        fixed_amount=None,
        percentage=None,
        manual_adjustment=None,
    ):
        self._superannuation_type_id = None
        self._display_name = None
        self._amount = None
        self._fixed_amount = None
        self._percentage = None
        self._manual_adjustment = None
        self.discriminator = None
        if superannuation_type_id is not None:
            self.superannuation_type_id = superannuation_type_id
        if display_name is not None:
            self.display_name = display_name
        if amount is not None:
            self.amount = amount
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount
        if percentage is not None:
            self.percentage = percentage
        if manual_adjustment is not None:
            self.manual_adjustment = manual_adjustment

    @property
    def superannuation_type_id(self):
        return self._superannuation_type_id

    @superannuation_type_id.setter
    def superannuation_type_id(self, superannuation_type_id):
        self._superannuation_type_id = superannuation_type_id

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
    def fixed_amount(self):
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        self._fixed_amount = fixed_amount

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage

    @property
    def manual_adjustment(self):
        return self._manual_adjustment

    @manual_adjustment.setter
    def manual_adjustment(self, manual_adjustment):
        self._manual_adjustment = manual_adjustment
