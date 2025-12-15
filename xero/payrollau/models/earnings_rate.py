from xero.models import BaseModel


class EarningsRate(BaseModel):
    openapi_types = {
        "name": "str",
        "account_code": "str",
        "type_of_units": "str",
        "is_exempt_from_tax": "bool",
        "is_exempt_from_super": "bool",
        "is_reportable_as_w1": "bool",
        "allowance_contributes_to_annual_leave_rate": "bool",
        "allowance_contributes_to_overtime_rate": "bool",
        "earnings_type": "EarningsType",
        "earnings_rate_id": "str",
        "rate_type": "RateType",
        "rate_per_unit": "str",
        "multiplier": "float",
        "accrue_leave": "bool",
        "amount": "float",
        "employment_termination_payment_type": "EmploymentTerminationPaymentType",
        "updated_date_utc": "datetime[ms-format]",
        "current_record": "bool",
        "allowance_type": "AllowanceType",
        "allowance_category": "AllowanceCategory",
    }
    attribute_map = {
        "name": "Name",
        "account_code": "AccountCode",
        "type_of_units": "TypeOfUnits",
        "is_exempt_from_tax": "IsExemptFromTax",
        "is_exempt_from_super": "IsExemptFromSuper",
        "is_reportable_as_w1": "IsReportableAsW1",
        "allowance_contributes_to_annual_leave_rate": "AllowanceContributesToAnnualLeaveRate",
        "allowance_contributes_to_overtime_rate": "AllowanceContributesToOvertimeRate",
        "earnings_type": "EarningsType",
        "earnings_rate_id": "EarningsRateID",
        "rate_type": "RateType",
        "rate_per_unit": "RatePerUnit",
        "multiplier": "Multiplier",
        "accrue_leave": "AccrueLeave",
        "amount": "Amount",
        "employment_termination_payment_type": "EmploymentTerminationPaymentType",
        "updated_date_utc": "UpdatedDateUTC",
        "current_record": "CurrentRecord",
        "allowance_type": "AllowanceType",
        "allowance_category": "AllowanceCategory",
    }

    def __init__(
        self,
        name=None,
        account_code=None,
        type_of_units=None,
        is_exempt_from_tax=None,
        is_exempt_from_super=None,
        is_reportable_as_w1=None,
        allowance_contributes_to_annual_leave_rate=None,
        allowance_contributes_to_overtime_rate=None,
        earnings_type=None,
        earnings_rate_id=None,
        rate_type=None,
        rate_per_unit=None,
        multiplier=None,
        accrue_leave=None,
        amount=None,
        employment_termination_payment_type=None,
        updated_date_utc=None,
        current_record=None,
        allowance_type=None,
        allowance_category=None,
    ):
        self._name = None
        self._account_code = None
        self._type_of_units = None
        self._is_exempt_from_tax = None
        self._is_exempt_from_super = None
        self._is_reportable_as_w1 = None
        self._allowance_contributes_to_annual_leave_rate = None
        self._allowance_contributes_to_overtime_rate = None
        self._earnings_type = None
        self._earnings_rate_id = None
        self._rate_type = None
        self._rate_per_unit = None
        self._multiplier = None
        self._accrue_leave = None
        self._amount = None
        self._employment_termination_payment_type = None
        self._updated_date_utc = None
        self._current_record = None
        self._allowance_type = None
        self._allowance_category = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if account_code is not None:
            self.account_code = account_code
        if type_of_units is not None:
            self.type_of_units = type_of_units
        if is_exempt_from_tax is not None:
            self.is_exempt_from_tax = is_exempt_from_tax
        if is_exempt_from_super is not None:
            self.is_exempt_from_super = is_exempt_from_super
        if is_reportable_as_w1 is not None:
            self.is_reportable_as_w1 = is_reportable_as_w1
        if allowance_contributes_to_annual_leave_rate is not None:
            self.allowance_contributes_to_annual_leave_rate = (
                allowance_contributes_to_annual_leave_rate
            )
        if allowance_contributes_to_overtime_rate is not None:
            self.allowance_contributes_to_overtime_rate = (
                allowance_contributes_to_overtime_rate
            )
        if earnings_type is not None:
            self.earnings_type = earnings_type
        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        if rate_type is not None:
            self.rate_type = rate_type
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if multiplier is not None:
            self.multiplier = multiplier
        if accrue_leave is not None:
            self.accrue_leave = accrue_leave
        if amount is not None:
            self.amount = amount
        if employment_termination_payment_type is not None:
            self.employment_termination_payment_type = (
                employment_termination_payment_type
            )
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if current_record is not None:
            self.current_record = current_record
        if allowance_type is not None:
            self.allowance_type = allowance_type
        if allowance_category is not None:
            self.allowance_category = allowance_category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 100:
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `100`"
            )
        self._name = name

    @property
    def account_code(self):
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        self._account_code = account_code

    @property
    def type_of_units(self):
        return self._type_of_units

    @type_of_units.setter
    def type_of_units(self, type_of_units):
        if type_of_units is not None and len(type_of_units) > 50:
            raise ValueError(
                "Invalid value for `type_of_units`, "
                "length must be less than or equal to `50`"
            )
        self._type_of_units = type_of_units

    @property
    def is_exempt_from_tax(self):
        return self._is_exempt_from_tax

    @is_exempt_from_tax.setter
    def is_exempt_from_tax(self, is_exempt_from_tax):
        self._is_exempt_from_tax = is_exempt_from_tax

    @property
    def is_exempt_from_super(self):
        return self._is_exempt_from_super

    @is_exempt_from_super.setter
    def is_exempt_from_super(self, is_exempt_from_super):
        self._is_exempt_from_super = is_exempt_from_super

    @property
    def is_reportable_as_w1(self):
        return self._is_reportable_as_w1

    @is_reportable_as_w1.setter
    def is_reportable_as_w1(self, is_reportable_as_w1):
        self._is_reportable_as_w1 = is_reportable_as_w1

    @property
    def allowance_contributes_to_annual_leave_rate(self):
        return self._allowance_contributes_to_annual_leave_rate

    @allowance_contributes_to_annual_leave_rate.setter
    def allowance_contributes_to_annual_leave_rate(
        self, allowance_contributes_to_annual_leave_rate
    ):
        self._allowance_contributes_to_annual_leave_rate = (
            allowance_contributes_to_annual_leave_rate
        )

    @property
    def allowance_contributes_to_overtime_rate(self):
        return self._allowance_contributes_to_overtime_rate

    @allowance_contributes_to_overtime_rate.setter
    def allowance_contributes_to_overtime_rate(
        self, allowance_contributes_to_overtime_rate
    ):
        self._allowance_contributes_to_overtime_rate = (
            allowance_contributes_to_overtime_rate
        )

    @property
    def earnings_type(self):
        return self._earnings_type

    @earnings_type.setter
    def earnings_type(self, earnings_type):
        self._earnings_type = earnings_type

    @property
    def earnings_rate_id(self):
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        self._earnings_rate_id = earnings_rate_id

    @property
    def rate_type(self):
        return self._rate_type

    @rate_type.setter
    def rate_type(self, rate_type):
        self._rate_type = rate_type

    @property
    def rate_per_unit(self):
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        self._rate_per_unit = rate_per_unit

    @property
    def multiplier(self):
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        self._multiplier = multiplier

    @property
    def accrue_leave(self):
        return self._accrue_leave

    @accrue_leave.setter
    def accrue_leave(self, accrue_leave):
        self._accrue_leave = accrue_leave

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def employment_termination_payment_type(self):
        return self._employment_termination_payment_type

    @employment_termination_payment_type.setter
    def employment_termination_payment_type(self, employment_termination_payment_type):
        self._employment_termination_payment_type = employment_termination_payment_type

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def current_record(self):
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        self._current_record = current_record

    @property
    def allowance_type(self):
        return self._allowance_type

    @allowance_type.setter
    def allowance_type(self, allowance_type):
        self._allowance_type = allowance_type

    @property
    def allowance_category(self):
        return self._allowance_category

    @allowance_category.setter
    def allowance_category(self, allowance_category):
        self._allowance_category = allowance_category
