from xero.models import BaseModel


class ReimbursementLine(BaseModel):
    openapi_types = {
        "reimbursement_type_id": "str",
        "description": "str",
        "amount": "float",
        "rate_per_unit": "float",
        "number_of_units": "float",
    }
    attribute_map = {
        "reimbursement_type_id": "reimbursementTypeID",
        "description": "description",
        "amount": "amount",
        "rate_per_unit": "ratePerUnit",
        "number_of_units": "numberOfUnits",
    }

    def __init__(
        self,
        reimbursement_type_id=None,
        description=None,
        amount=None,
        rate_per_unit=None,
        number_of_units=None,
    ):
        self._reimbursement_type_id = None
        self._description = None
        self._amount = None
        self._rate_per_unit = None
        self._number_of_units = None
        self.discriminator = None
        if reimbursement_type_id is not None:
            self.reimbursement_type_id = reimbursement_type_id
        if description is not None:
            self.description = description
        if amount is not None:
            self.amount = amount
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if number_of_units is not None:
            self.number_of_units = number_of_units

    @property
    def reimbursement_type_id(self):
        return self._reimbursement_type_id

    @reimbursement_type_id.setter
    def reimbursement_type_id(self, reimbursement_type_id):
        self._reimbursement_type_id = reimbursement_type_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def rate_per_unit(self):
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        self._rate_per_unit = rate_per_unit

    @property
    def number_of_units(self):
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        self._number_of_units = number_of_units
