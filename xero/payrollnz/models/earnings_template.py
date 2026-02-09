from xero.models import BaseModel


class EarningsTemplate(BaseModel):
    openapi_types = {
        "pay_template_earning_id": "str",
        "rate_per_unit": "float",
        "number_of_units": "float",
        "fixed_amount": "float",
        "earnings_rate_id": "str",
        "name": "str",
    }
    attribute_map = {
        "pay_template_earning_id": "payTemplateEarningID",
        "rate_per_unit": "ratePerUnit",
        "number_of_units": "numberOfUnits",
        "fixed_amount": "fixedAmount",
        "earnings_rate_id": "earningsRateID",
        "name": "name",
    }

    def __init__(
        self,
        pay_template_earning_id=None,
        rate_per_unit=None,
        number_of_units=None,
        fixed_amount=None,
        earnings_rate_id=None,
        name=None,
    ):
        self._pay_template_earning_id = None
        self._rate_per_unit = None
        self._number_of_units = None
        self._fixed_amount = None
        self._earnings_rate_id = None
        self._name = None
        self.discriminator = None
        if pay_template_earning_id is not None:
            self.pay_template_earning_id = pay_template_earning_id
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount
        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        if name is not None:
            self.name = name

    @property
    def pay_template_earning_id(self):
        return self._pay_template_earning_id

    @pay_template_earning_id.setter
    def pay_template_earning_id(self, pay_template_earning_id):
        self._pay_template_earning_id = pay_template_earning_id

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

    @property
    def fixed_amount(self):
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        self._fixed_amount = fixed_amount

    @property
    def earnings_rate_id(self):
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        self._earnings_rate_id = earnings_rate_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
