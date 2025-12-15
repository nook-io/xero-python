from xero.models import BaseModel


class TaxSettings(BaseModel):
    openapi_types = {
        "period_units": "float",
        "period_type": "str",
        "tax_code": "TaxCode",
        "special_tax_rate": "str",
        "lump_sum_tax_code": "str",
        "lump_sum_amount": "str",
    }
    attribute_map = {
        "period_units": "periodUnits",
        "period_type": "periodType",
        "tax_code": "taxCode",
        "special_tax_rate": "specialTaxRate",
        "lump_sum_tax_code": "lumpSumTaxCode",
        "lump_sum_amount": "lumpSumAmount",
    }

    def __init__(
        self,
        period_units=None,
        period_type=None,
        tax_code=None,
        special_tax_rate=None,
        lump_sum_tax_code=None,
        lump_sum_amount=None,
    ):
        self._period_units = None
        self._period_type = None
        self._tax_code = None
        self._special_tax_rate = None
        self._lump_sum_tax_code = None
        self._lump_sum_amount = None
        self.discriminator = None
        if period_units is not None:
            self.period_units = period_units
        if period_type is not None:
            self.period_type = period_type
        if tax_code is not None:
            self.tax_code = tax_code
        if special_tax_rate is not None:
            self.special_tax_rate = special_tax_rate
        if lump_sum_tax_code is not None:
            self.lump_sum_tax_code = lump_sum_tax_code
        if lump_sum_amount is not None:
            self.lump_sum_amount = lump_sum_amount

    @property
    def period_units(self):
        return self._period_units

    @period_units.setter
    def period_units(self, period_units):
        self._period_units = period_units

    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        allowed_values = ["weeks", "months", "None"]
        if period_type:
            if period_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `period_type` ({0}), must be one of {1}".format(
                        period_type, allowed_values
                    )
                )
        self._period_type = period_type

    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, tax_code):
        self._tax_code = tax_code

    @property
    def special_tax_rate(self):
        return self._special_tax_rate

    @special_tax_rate.setter
    def special_tax_rate(self, special_tax_rate):
        self._special_tax_rate = special_tax_rate

    @property
    def lump_sum_tax_code(self):
        return self._lump_sum_tax_code

    @lump_sum_tax_code.setter
    def lump_sum_tax_code(self, lump_sum_tax_code):
        self._lump_sum_tax_code = lump_sum_tax_code

    @property
    def lump_sum_amount(self):
        return self._lump_sum_amount

    @lump_sum_amount.setter
    def lump_sum_amount(self, lump_sum_amount):
        self._lump_sum_amount = lump_sum_amount
