from xero.models import BaseModel


class DeductionLine(BaseModel):
    openapi_types = {
        "deduction_type_id": "str",
        "calculation_type": "DeductionTypeCalculationType",
        "amount": "float",
        "percentage": "float",
        "number_of_units": "float",
    }
    attribute_map = {
        "deduction_type_id": "DeductionTypeID",
        "calculation_type": "CalculationType",
        "amount": "Amount",
        "percentage": "Percentage",
        "number_of_units": "NumberOfUnits",
    }

    def __init__(
        self,
        deduction_type_id=None,
        calculation_type=None,
        amount=None,
        percentage=None,
        number_of_units=None,
    ):
        self._deduction_type_id = None
        self._calculation_type = None
        self._amount = None
        self._percentage = None
        self._number_of_units = None
        self.discriminator = None
        self.deduction_type_id = deduction_type_id
        if calculation_type is not None:
            self.calculation_type = calculation_type
        if amount is not None:
            self.amount = amount
        if percentage is not None:
            self.percentage = percentage
        if number_of_units is not None:
            self.number_of_units = number_of_units

    @property
    def deduction_type_id(self):
        return self._deduction_type_id

    @deduction_type_id.setter
    def deduction_type_id(self, deduction_type_id):
        if deduction_type_id is None:
            raise ValueError(
                "Invalid value for `deduction_type_id`, must not be `None`"
            )
        self._deduction_type_id = deduction_type_id

    @property
    def calculation_type(self):
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        self._calculation_type = calculation_type

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage

    @property
    def number_of_units(self):
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        self._number_of_units = number_of_units
