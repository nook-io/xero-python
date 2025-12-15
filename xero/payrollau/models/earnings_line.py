from xero.models import BaseModel


class EarningsLine(BaseModel):
    openapi_types = {
        "earnings_rate_id": "str",
        "calculation_type": "EarningsRateCalculationType",
        "annual_salary": "float",
        "number_of_units_per_week": "float",
        "rate_per_unit": "float",
        "normal_number_of_units": "float",
        "amount": "float",
        "number_of_units": "float",
        "fixed_amount": "float",
    }
    attribute_map = {
        "earnings_rate_id": "EarningsRateID",
        "calculation_type": "CalculationType",
        "annual_salary": "AnnualSalary",
        "number_of_units_per_week": "NumberOfUnitsPerWeek",
        "rate_per_unit": "RatePerUnit",
        "normal_number_of_units": "NormalNumberOfUnits",
        "amount": "Amount",
        "number_of_units": "NumberOfUnits",
        "fixed_amount": "FixedAmount",
    }

    def __init__(
        self,
        earnings_rate_id=None,
        calculation_type=None,
        annual_salary=None,
        number_of_units_per_week=None,
        rate_per_unit=None,
        normal_number_of_units=None,
        amount=None,
        number_of_units=None,
        fixed_amount=None,
    ):
        self._earnings_rate_id = None
        self._calculation_type = None
        self._annual_salary = None
        self._number_of_units_per_week = None
        self._rate_per_unit = None
        self._normal_number_of_units = None
        self._amount = None
        self._number_of_units = None
        self._fixed_amount = None
        self.discriminator = None
        self.earnings_rate_id = earnings_rate_id
        if calculation_type is not None:
            self.calculation_type = calculation_type
        if annual_salary is not None:
            self.annual_salary = annual_salary
        if number_of_units_per_week is not None:
            self.number_of_units_per_week = number_of_units_per_week
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if normal_number_of_units is not None:
            self.normal_number_of_units = normal_number_of_units
        if amount is not None:
            self.amount = amount
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount

    @property
    def earnings_rate_id(self):
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        if earnings_rate_id is None:
            raise ValueError("Invalid value for `earnings_rate_id`, must not be `None`")
        self._earnings_rate_id = earnings_rate_id

    @property
    def calculation_type(self):
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        self._calculation_type = calculation_type

    @property
    def annual_salary(self):
        return self._annual_salary

    @annual_salary.setter
    def annual_salary(self, annual_salary):
        self._annual_salary = annual_salary

    @property
    def number_of_units_per_week(self):
        return self._number_of_units_per_week

    @number_of_units_per_week.setter
    def number_of_units_per_week(self, number_of_units_per_week):
        self._number_of_units_per_week = number_of_units_per_week

    @property
    def rate_per_unit(self):
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        self._rate_per_unit = rate_per_unit

    @property
    def normal_number_of_units(self):
        return self._normal_number_of_units

    @normal_number_of_units.setter
    def normal_number_of_units(self, normal_number_of_units):
        self._normal_number_of_units = normal_number_of_units

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def number_of_units(self):
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        self._number_of_units = number_of_units

    @property
    def fixed_amount(self):
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        self._fixed_amount = fixed_amount
