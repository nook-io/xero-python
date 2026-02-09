from xero.models import BaseModel


class OpeningBalances(BaseModel):
    openapi_types = {
        "opening_balance_date": "date[ms-format]",
        "tax": "str",
        "earnings_lines": "list[EarningsLine]",
        "deduction_lines": "list[DeductionLine]",
        "super_lines": "list[SuperLine]",
        "reimbursement_lines": "list[ReimbursementLine]",
        "leave_lines": "list[LeaveLine]",
        "paid_leave_earnings_lines": "list[PaidLeaveEarningsLine]",
    }
    attribute_map = {
        "opening_balance_date": "OpeningBalanceDate",
        "tax": "Tax",
        "earnings_lines": "EarningsLines",
        "deduction_lines": "DeductionLines",
        "super_lines": "SuperLines",
        "reimbursement_lines": "ReimbursementLines",
        "leave_lines": "LeaveLines",
        "paid_leave_earnings_lines": "PaidLeaveEarningsLines",
    }

    def __init__(
        self,
        opening_balance_date=None,
        tax=None,
        earnings_lines=None,
        deduction_lines=None,
        super_lines=None,
        reimbursement_lines=None,
        leave_lines=None,
        paid_leave_earnings_lines=None,
    ):
        self._opening_balance_date = None
        self._tax = None
        self._earnings_lines = None
        self._deduction_lines = None
        self._super_lines = None
        self._reimbursement_lines = None
        self._leave_lines = None
        self._paid_leave_earnings_lines = None
        self.discriminator = None
        if opening_balance_date is not None:
            self.opening_balance_date = opening_balance_date
        if tax is not None:
            self.tax = tax
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
        if paid_leave_earnings_lines is not None:
            self.paid_leave_earnings_lines = paid_leave_earnings_lines

    @property
    def opening_balance_date(self):
        return self._opening_balance_date

    @opening_balance_date.setter
    def opening_balance_date(self, opening_balance_date):
        self._opening_balance_date = opening_balance_date

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, tax):
        self._tax = tax

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

    @property
    def paid_leave_earnings_lines(self):
        return self._paid_leave_earnings_lines

    @paid_leave_earnings_lines.setter
    def paid_leave_earnings_lines(self, paid_leave_earnings_lines):
        self._paid_leave_earnings_lines = paid_leave_earnings_lines
