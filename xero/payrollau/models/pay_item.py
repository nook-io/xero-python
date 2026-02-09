from xero.models import BaseModel


class PayItem(BaseModel):
    openapi_types = {
        "earnings_rates": "list[EarningsRate]",
        "deduction_types": "list[DeductionType]",
        "leave_types": "list[LeaveType]",
        "reimbursement_types": "list[ReimbursementType]",
    }
    attribute_map = {
        "earnings_rates": "EarningsRates",
        "deduction_types": "DeductionTypes",
        "leave_types": "LeaveTypes",
        "reimbursement_types": "ReimbursementTypes",
    }

    def __init__(
        self,
        earnings_rates=None,
        deduction_types=None,
        leave_types=None,
        reimbursement_types=None,
    ):
        self._earnings_rates = None
        self._deduction_types = None
        self._leave_types = None
        self._reimbursement_types = None
        self.discriminator = None
        if earnings_rates is not None:
            self.earnings_rates = earnings_rates
        if deduction_types is not None:
            self.deduction_types = deduction_types
        if leave_types is not None:
            self.leave_types = leave_types
        if reimbursement_types is not None:
            self.reimbursement_types = reimbursement_types

    @property
    def earnings_rates(self):
        return self._earnings_rates

    @earnings_rates.setter
    def earnings_rates(self, earnings_rates):
        self._earnings_rates = earnings_rates

    @property
    def deduction_types(self):
        return self._deduction_types

    @deduction_types.setter
    def deduction_types(self, deduction_types):
        self._deduction_types = deduction_types

    @property
    def leave_types(self):
        return self._leave_types

    @leave_types.setter
    def leave_types(self, leave_types):
        self._leave_types = leave_types

    @property
    def reimbursement_types(self):
        return self._reimbursement_types

    @reimbursement_types.setter
    def reimbursement_types(self, reimbursement_types):
        self._reimbursement_types = reimbursement_types
