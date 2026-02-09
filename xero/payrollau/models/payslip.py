from xero.models import BaseModel


class Payslip(BaseModel):
    openapi_types = {
        "employee_id": "str",
        "payslip_id": "str",
        "first_name": "str",
        "last_name": "str",
        "wages": "float",
        "deductions": "float",
        "tax": "float",
        "super": "float",
        "reimbursements": "float",
        "net_pay": "float",
        "earnings_lines": "list[EarningsLine]",
        "leave_earnings_lines": "list[LeaveEarningsLine]",
        "timesheet_earnings_lines": "list[EarningsLine]",
        "deduction_lines": "list[DeductionLine]",
        "leave_accrual_lines": "list[LeaveAccrualLine]",
        "reimbursement_lines": "list[ReimbursementLine]",
        "superannuation_lines": "list[SuperannuationLine]",
        "tax_lines": "list[TaxLine]",
        "updated_date_utc": "datetime[ms-format]",
    }
    attribute_map = {
        "employee_id": "EmployeeID",
        "payslip_id": "PayslipID",
        "first_name": "FirstName",
        "last_name": "LastName",
        "wages": "Wages",
        "deductions": "Deductions",
        "tax": "Tax",
        "super": "Super",
        "reimbursements": "Reimbursements",
        "net_pay": "NetPay",
        "earnings_lines": "EarningsLines",
        "leave_earnings_lines": "LeaveEarningsLines",
        "timesheet_earnings_lines": "TimesheetEarningsLines",
        "deduction_lines": "DeductionLines",
        "leave_accrual_lines": "LeaveAccrualLines",
        "reimbursement_lines": "ReimbursementLines",
        "superannuation_lines": "SuperannuationLines",
        "tax_lines": "TaxLines",
        "updated_date_utc": "UpdatedDateUTC",
    }

    def __init__(
        self,
        employee_id=None,
        payslip_id=None,
        first_name=None,
        last_name=None,
        wages=None,
        deductions=None,
        tax=None,
        super=None,
        reimbursements=None,
        net_pay=None,
        earnings_lines=None,
        leave_earnings_lines=None,
        timesheet_earnings_lines=None,
        deduction_lines=None,
        leave_accrual_lines=None,
        reimbursement_lines=None,
        superannuation_lines=None,
        tax_lines=None,
        updated_date_utc=None,
    ):
        self._employee_id = None
        self._payslip_id = None
        self._first_name = None
        self._last_name = None
        self._wages = None
        self._deductions = None
        self._tax = None
        self._super = None
        self._reimbursements = None
        self._net_pay = None
        self._earnings_lines = None
        self._leave_earnings_lines = None
        self._timesheet_earnings_lines = None
        self._deduction_lines = None
        self._leave_accrual_lines = None
        self._reimbursement_lines = None
        self._superannuation_lines = None
        self._tax_lines = None
        self._updated_date_utc = None
        self.discriminator = None
        if employee_id is not None:
            self.employee_id = employee_id
        if payslip_id is not None:
            self.payslip_id = payslip_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if wages is not None:
            self.wages = wages
        if deductions is not None:
            self.deductions = deductions
        if tax is not None:
            self.tax = tax
        if super is not None:
            self.super = super
        if reimbursements is not None:
            self.reimbursements = reimbursements
        if net_pay is not None:
            self.net_pay = net_pay
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
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def payslip_id(self):
        return self._payslip_id

    @payslip_id.setter
    def payslip_id(self, payslip_id):
        self._payslip_id = payslip_id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def wages(self):
        return self._wages

    @wages.setter
    def wages(self, wages):
        self._wages = wages

    @property
    def deductions(self):
        return self._deductions

    @deductions.setter
    def deductions(self, deductions):
        self._deductions = deductions

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, tax):
        self._tax = tax

    @property
    def super(self):
        return self._super

    @super.setter
    def super(self, super):
        self._super = super

    @property
    def reimbursements(self):
        return self._reimbursements

    @reimbursements.setter
    def reimbursements(self, reimbursements):
        self._reimbursements = reimbursements

    @property
    def net_pay(self):
        return self._net_pay

    @net_pay.setter
    def net_pay(self, net_pay):
        self._net_pay = net_pay

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

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc
