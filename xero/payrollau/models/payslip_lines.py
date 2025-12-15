from xero.models import BaseModel


class PayslipLines(BaseModel):
    openapi_types = {
        "earnings_lines": "list[EarningsLine]",
        "leave_earnings_lines": "list[LeaveEarningsLine]",
        "timesheet_earnings_lines": "list[EarningsLine]",
        "deduction_lines": "list[DeductionLine]",
        "leave_accrual_lines": "list[LeaveAccrualLine]",
        "reimbursement_lines": "list[ReimbursementLine]",
        "superannuation_lines": "list[SuperannuationLine]",
        "tax_lines": "list[TaxLine]",
    }
    attribute_map = {
        "earnings_lines": "EarningsLines",
        "leave_earnings_lines": "LeaveEarningsLines",
        "timesheet_earnings_lines": "TimesheetEarningsLines",
        "deduction_lines": "DeductionLines",
        "leave_accrual_lines": "LeaveAccrualLines",
        "reimbursement_lines": "ReimbursementLines",
        "superannuation_lines": "SuperannuationLines",
        "tax_lines": "TaxLines",
    }

    def __init__(
        self,
        earnings_lines=None,
        leave_earnings_lines=None,
        timesheet_earnings_lines=None,
        deduction_lines=None,
        leave_accrual_lines=None,
        reimbursement_lines=None,
        superannuation_lines=None,
        tax_lines=None,
    ):
        self._earnings_lines = None
        self._leave_earnings_lines = None
        self._timesheet_earnings_lines = None
        self._deduction_lines = None
        self._leave_accrual_lines = None
        self._reimbursement_lines = None
        self._superannuation_lines = None
        self._tax_lines = None
        self.discriminator = None
        if earnings_lines is not None:
            self.earnings_lines = earnings_lines
        if leave_earnings_lines is not None:
            self.leave_earnings_lines = leave_earnings_lines
        if timesheet_earnings_lines is not None:
            self.timesheet_earnings_lines = timesheet_earnings_lines
        if deduction_lines is not None:
            self.deduction_lines = deduction_lines
        if leave_accrual_lines is not None:
            self.leave_accrual_lines = leave_accrual_lines
        if reimbursement_lines is not None:
            self.reimbursement_lines = reimbursement_lines
        if superannuation_lines is not None:
            self.superannuation_lines = superannuation_lines
        if tax_lines is not None:
            self.tax_lines = tax_lines

    @property
    def earnings_lines(self):
        return self._earnings_lines

    @earnings_lines.setter
    def earnings_lines(self, earnings_lines):
        self._earnings_lines = earnings_lines

    @property
    def leave_earnings_lines(self):
        return self._leave_earnings_lines

    @leave_earnings_lines.setter
    def leave_earnings_lines(self, leave_earnings_lines):
        self._leave_earnings_lines = leave_earnings_lines

    @property
    def timesheet_earnings_lines(self):
        return self._timesheet_earnings_lines

    @timesheet_earnings_lines.setter
    def timesheet_earnings_lines(self, timesheet_earnings_lines):
        self._timesheet_earnings_lines = timesheet_earnings_lines

    @property
    def deduction_lines(self):
        return self._deduction_lines

    @deduction_lines.setter
    def deduction_lines(self, deduction_lines):
        self._deduction_lines = deduction_lines

    @property
    def leave_accrual_lines(self):
        return self._leave_accrual_lines

    @leave_accrual_lines.setter
    def leave_accrual_lines(self, leave_accrual_lines):
        self._leave_accrual_lines = leave_accrual_lines

    @property
    def reimbursement_lines(self):
        return self._reimbursement_lines

    @reimbursement_lines.setter
    def reimbursement_lines(self, reimbursement_lines):
        self._reimbursement_lines = reimbursement_lines

    @property
    def superannuation_lines(self):
        return self._superannuation_lines

    @superannuation_lines.setter
    def superannuation_lines(self, superannuation_lines):
        self._superannuation_lines = superannuation_lines

    @property
    def tax_lines(self):
        return self._tax_lines

    @tax_lines.setter
    def tax_lines(self, tax_lines):
        self._tax_lines = tax_lines
