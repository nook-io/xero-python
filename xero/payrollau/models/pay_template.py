from xero.models import BaseModel


class PayTemplate(BaseModel):
    openapi_types = {
        "earnings_lines": "list[EarningsLine]",
        "deduction_lines": "list[DeductionLine]",
        "super_lines": "list[SuperLine]",
        "reimbursement_lines": "list[ReimbursementLine]",
        "leave_lines": "list[LeaveLine]",
    }
    attribute_map = {
        "earnings_lines": "EarningsLines",
        "deduction_lines": "DeductionLines",
        "super_lines": "SuperLines",
        "reimbursement_lines": "ReimbursementLines",
        "leave_lines": "LeaveLines",
    }

    def __init__(
        self,
        earnings_lines=None,
        deduction_lines=None,
        super_lines=None,
        reimbursement_lines=None,
        leave_lines=None,
    ):
        self._earnings_lines = None
        self._deduction_lines = None
        self._super_lines = None
        self._reimbursement_lines = None
        self._leave_lines = None
        self.discriminator = None
        if earnings_lines is not None:
            self.earnings_lines = earnings_lines
        if deduction_lines is not None:
            self.deduction_lines = deduction_lines
        if super_lines is not None:
            self.super_lines = super_lines
        if reimbursement_lines is not None:
            self.reimbursement_lines = reimbursement_lines
        if leave_lines is not None:
            self.leave_lines = leave_lines

    @property
    def earnings_lines(self):
        return self._earnings_lines

    @earnings_lines.setter
    def earnings_lines(self, earnings_lines):
        self._earnings_lines = earnings_lines

    @property
    def deduction_lines(self):
        return self._deduction_lines

    @deduction_lines.setter
    def deduction_lines(self, deduction_lines):
        self._deduction_lines = deduction_lines

    @property
    def super_lines(self):
        return self._super_lines

    @super_lines.setter
    def super_lines(self, super_lines):
        self._super_lines = super_lines

    @property
    def reimbursement_lines(self):
        return self._reimbursement_lines

    @reimbursement_lines.setter
    def reimbursement_lines(self, reimbursement_lines):
        self._reimbursement_lines = reimbursement_lines

    @property
    def leave_lines(self):
        return self._leave_lines

    @leave_lines.setter
    def leave_lines(self, leave_lines):
        self._leave_lines = leave_lines
