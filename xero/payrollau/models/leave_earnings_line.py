from xero.models import BaseModel


class LeaveEarningsLine(BaseModel):
    openapi_types = {
        "earnings_rate_id": "str",
        "rate_per_unit": "float",
        "number_of_units": "float",
        "pay_out_type": "PayOutType",
    }
    attribute_map = {
        "earnings_rate_id": "EarningsRateID",
        "rate_per_unit": "RatePerUnit",
        "number_of_units": "NumberOfUnits",
        "pay_out_type": "PayOutType",
    }

    def __init__(
        self,
        earnings_rate_id=None,
        rate_per_unit=None,
        number_of_units=None,
        pay_out_type=None,
    ):
        self._earnings_rate_id = None
        self._rate_per_unit = None
        self._number_of_units = None
        self._pay_out_type = None
        self.discriminator = None
        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if pay_out_type is not None:
            self.pay_out_type = pay_out_type

    @property
    def earnings_rate_id(self):
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        self._earnings_rate_id = earnings_rate_id

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
    def pay_out_type(self):
        return self._pay_out_type

    @pay_out_type.setter
    def pay_out_type(self, pay_out_type):
        self._pay_out_type = pay_out_type
