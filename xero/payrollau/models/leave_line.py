from xero.models import BaseModel


class LeaveLine(BaseModel):
    openapi_types = {
        "leave_type_id": "str",
        "calculation_type": "LeaveLineCalculationType",
        "entitlement_final_pay_payout_type": "EntitlementFinalPayPayoutType",
        "employment_termination_payment_type": "EmploymentTerminationPaymentType",
        "include_superannuation_guarantee_contribution": "bool",
        "number_of_units": "float",
        "annual_number_of_units": "float",
        "full_time_number_of_units_per_period": "float",
    }
    attribute_map = {
        "leave_type_id": "LeaveTypeID",
        "calculation_type": "CalculationType",
        "entitlement_final_pay_payout_type": "EntitlementFinalPayPayoutType",
        "employment_termination_payment_type": "EmploymentTerminationPaymentType",
        "include_superannuation_guarantee_contribution": "IncludeSuperannuationGuaranteeContribution",
        "number_of_units": "NumberOfUnits",
        "annual_number_of_units": "AnnualNumberOfUnits",
        "full_time_number_of_units_per_period": "FullTimeNumberOfUnitsPerPeriod",
    }

    def __init__(
        self,
        leave_type_id=None,
        calculation_type=None,
        entitlement_final_pay_payout_type=None,
        employment_termination_payment_type=None,
        include_superannuation_guarantee_contribution=None,
        number_of_units=None,
        annual_number_of_units=None,
        full_time_number_of_units_per_period=None,
    ):
        self._leave_type_id = None
        self._calculation_type = None
        self._entitlement_final_pay_payout_type = None
        self._employment_termination_payment_type = None
        self._include_superannuation_guarantee_contribution = None
        self._number_of_units = None
        self._annual_number_of_units = None
        self._full_time_number_of_units_per_period = None
        self.discriminator = None
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if calculation_type is not None:
            self.calculation_type = calculation_type
        if entitlement_final_pay_payout_type is not None:
            self.entitlement_final_pay_payout_type = entitlement_final_pay_payout_type
        if employment_termination_payment_type is not None:
            self.employment_termination_payment_type = (
                employment_termination_payment_type
            )
        if include_superannuation_guarantee_contribution is not None:
            self.include_superannuation_guarantee_contribution = (
                include_superannuation_guarantee_contribution
            )
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if annual_number_of_units is not None:
            self.annual_number_of_units = annual_number_of_units
        if full_time_number_of_units_per_period is not None:
            self.full_time_number_of_units_per_period = (
                full_time_number_of_units_per_period
            )

    @property
    def leave_type_id(self):
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        self._leave_type_id = leave_type_id

    @property
    def calculation_type(self):
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        self._calculation_type = calculation_type

    @property
    def entitlement_final_pay_payout_type(self):
        return self._entitlement_final_pay_payout_type

    @entitlement_final_pay_payout_type.setter
    def entitlement_final_pay_payout_type(self, entitlement_final_pay_payout_type):
        self._entitlement_final_pay_payout_type = entitlement_final_pay_payout_type

    @property
    def employment_termination_payment_type(self):
        return self._employment_termination_payment_type

    @employment_termination_payment_type.setter
    def employment_termination_payment_type(self, employment_termination_payment_type):
        self._employment_termination_payment_type = employment_termination_payment_type

    @property
    def include_superannuation_guarantee_contribution(self):
        return self._include_superannuation_guarantee_contribution

    @include_superannuation_guarantee_contribution.setter
    def include_superannuation_guarantee_contribution(
        self, include_superannuation_guarantee_contribution
    ):
        self._include_superannuation_guarantee_contribution = (
            include_superannuation_guarantee_contribution
        )

    @property
    def number_of_units(self):
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        self._number_of_units = number_of_units

    @property
    def annual_number_of_units(self):
        return self._annual_number_of_units

    @annual_number_of_units.setter
    def annual_number_of_units(self, annual_number_of_units):
        self._annual_number_of_units = annual_number_of_units

    @property
    def full_time_number_of_units_per_period(self):
        return self._full_time_number_of_units_per_period

    @full_time_number_of_units_per_period.setter
    def full_time_number_of_units_per_period(
        self, full_time_number_of_units_per_period
    ):
        self._full_time_number_of_units_per_period = (
            full_time_number_of_units_per_period
        )
