from xero.models import BaseModel


class EarningsRate(BaseModel):
    openapi_types = {
        "earnings_rate_id": "str",
        "name": "str",
        "earnings_type": "str",
        "rate_type": "str",
        "type_of_units": "str",
        "current_record": "bool",
        "expense_account_id": "str",
        "rate_per_unit": "float",
        "multiple_of_ordinary_earnings_rate": "float",
        "fixed_amount": "float",
    }
    attribute_map = {
        "earnings_rate_id": "earningsRateID",
        "name": "name",
        "earnings_type": "earningsType",
        "rate_type": "rateType",
        "type_of_units": "typeOfUnits",
        "current_record": "currentRecord",
        "expense_account_id": "expenseAccountID",
        "rate_per_unit": "ratePerUnit",
        "multiple_of_ordinary_earnings_rate": "multipleOfOrdinaryEarningsRate",
        "fixed_amount": "fixedAmount",
    }

    def __init__(
        self,
        earnings_rate_id=None,
        name=None,
        earnings_type=None,
        rate_type=None,
        type_of_units=None,
        current_record=None,
        expense_account_id=None,
        rate_per_unit=None,
        multiple_of_ordinary_earnings_rate=None,
        fixed_amount=None,
    ):
        self._earnings_rate_id = None
        self._name = None
        self._earnings_type = None
        self._rate_type = None
        self._type_of_units = None
        self._current_record = None
        self._expense_account_id = None
        self._rate_per_unit = None
        self._multiple_of_ordinary_earnings_rate = None
        self._fixed_amount = None
        self.discriminator = None
        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        self.name = name
        self.earnings_type = earnings_type
        self.rate_type = rate_type
        self.type_of_units = type_of_units
        if current_record is not None:
            self.current_record = current_record
        self.expense_account_id = expense_account_id
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if multiple_of_ordinary_earnings_rate is not None:
            self.multiple_of_ordinary_earnings_rate = multiple_of_ordinary_earnings_rate
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount

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
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def earnings_type(self):
        return self._earnings_type

    @earnings_type.setter
    def earnings_type(self, earnings_type):
        if earnings_type is None:
            raise ValueError("Invalid value for `earnings_type`, must not be `None`")
        allowed_values = [
            "Allowance",
            "BackPay",
            "Bonus",
            "Commission",
            "LumpSum",
            "OtherEarnings",
            "OvertimeEarnings",
            "RegularEarnings",
            "StatutoryAdoptionPay",
            "StatutoryAdoptionPayNonPensionable",
            "StatutoryBereavementPay",
            "StatutoryMaternityPay",
            "StatutoryMaternityPayNonPensionable",
            "StatutoryPaternityPay",
            "StatutoryPaternityPayNonPensionable",
            "StatutoryParentalBereavementPayNonPensionable",
            "StatutorySharedParentalPay",
            "StatutorySharedParentalPayNonPensionable",
            "StatutorySickPay",
            "StatutorySickPayNonPensionable",
            "TipsNonDirect",
            "TipsDirect",
            "TerminationPay",
            "None",
        ]
        if earnings_type:
            if earnings_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `earnings_type` ({0}), must be one of {1}".format(
                        earnings_type, allowed_values
                    )
                )
        self._earnings_type = earnings_type

    @property
    def rate_type(self):
        return self._rate_type

    @rate_type.setter
    def rate_type(self, rate_type):
        if rate_type is None:
            raise ValueError("Invalid value for `rate_type`, must not be `None`")
        allowed_values = [
            "RatePerUnit",
            "MultipleOfOrdinaryEarningsRate",
            "FixedAmount",
            "None",
        ]
        if rate_type:
            if rate_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `rate_type` ({0}), must be one of {1}".format(
                        rate_type, allowed_values
                    )
                )
        self._rate_type = rate_type

    @property
    def type_of_units(self):
        return self._type_of_units

    @type_of_units.setter
    def type_of_units(self, type_of_units):
        if type_of_units is None:
            raise ValueError("Invalid value for `type_of_units`, must not be `None`")
        self._type_of_units = type_of_units

    @property
    def current_record(self):
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        self._current_record = current_record

    @property
    def expense_account_id(self):
        return self._expense_account_id

    @expense_account_id.setter
    def expense_account_id(self, expense_account_id):
        if expense_account_id is None:
            raise ValueError(
                "Invalid value for `expense_account_id`, must not be `None`"
            )
        self._expense_account_id = expense_account_id

    @property
    def rate_per_unit(self):
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        self._rate_per_unit = rate_per_unit

    @property
    def multiple_of_ordinary_earnings_rate(self):
        return self._multiple_of_ordinary_earnings_rate

    @multiple_of_ordinary_earnings_rate.setter
    def multiple_of_ordinary_earnings_rate(self, multiple_of_ordinary_earnings_rate):
        self._multiple_of_ordinary_earnings_rate = multiple_of_ordinary_earnings_rate

    @property
    def fixed_amount(self):
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        self._fixed_amount = fixed_amount
