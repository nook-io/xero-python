from xero.models import BaseModel


class Payslip(BaseModel):
    openapi_types = {
        "pay_slip_id": "str",
        "employee_id": "str",
        "pay_run_id": "str",
        "last_edited": "date",
        "first_name": "str",
        "last_name": "str",
        "total_earnings": "float",
        "gross_earnings": "float",
        "total_pay": "float",
        "total_employer_taxes": "float",
        "total_employee_taxes": "float",
        "total_deductions": "float",
        "total_reimbursements": "float",
        "total_court_orders": "float",
        "total_benefits": "float",
        "bacs_hash": "str",
        "payment_method": "str",
        "earnings_lines": "list[EarningsLine]",
        "leave_earnings_lines": "list[LeaveEarningsLine]",
        "timesheet_earnings_lines": "list[TimesheetEarningsLine]",
        "deduction_lines": "list[DeductionLine]",
        "reimbursement_lines": "list[ReimbursementLine]",
        "leave_accrual_lines": "list[LeaveAccrualLine]",
        "benefit_lines": "list[BenefitLine]",
        "payment_lines": "list[PaymentLine]",
        "employee_tax_lines": "list[TaxLine]",
        "employer_tax_lines": "list[TaxLine]",
        "court_order_lines": "list[CourtOrderLine]",
    }
    attribute_map = {
        "pay_slip_id": "paySlipID",
        "employee_id": "employeeID",
        "pay_run_id": "payRunID",
        "last_edited": "lastEdited",
        "first_name": "firstName",
        "last_name": "lastName",
        "total_earnings": "totalEarnings",
        "gross_earnings": "grossEarnings",
        "total_pay": "totalPay",
        "total_employer_taxes": "totalEmployerTaxes",
        "total_employee_taxes": "totalEmployeeTaxes",
        "total_deductions": "totalDeductions",
        "total_reimbursements": "totalReimbursements",
        "total_court_orders": "totalCourtOrders",
        "total_benefits": "totalBenefits",
        "bacs_hash": "bacsHash",
        "payment_method": "paymentMethod",
        "earnings_lines": "earningsLines",
        "leave_earnings_lines": "leaveEarningsLines",
        "timesheet_earnings_lines": "timesheetEarningsLines",
        "deduction_lines": "deductionLines",
        "reimbursement_lines": "reimbursementLines",
        "leave_accrual_lines": "leaveAccrualLines",
        "benefit_lines": "benefitLines",
        "payment_lines": "paymentLines",
        "employee_tax_lines": "employeeTaxLines",
        "employer_tax_lines": "employerTaxLines",
        "court_order_lines": "courtOrderLines",
    }

    def __init__(
        self,
        pay_slip_id=None,
        employee_id=None,
        pay_run_id=None,
        last_edited=None,
        first_name=None,
        last_name=None,
        total_earnings=None,
        gross_earnings=None,
        total_pay=None,
        total_employer_taxes=None,
        total_employee_taxes=None,
        total_deductions=None,
        total_reimbursements=None,
        total_court_orders=None,
        total_benefits=None,
        bacs_hash=None,
        payment_method=None,
        earnings_lines=None,
        leave_earnings_lines=None,
        timesheet_earnings_lines=None,
        deduction_lines=None,
        reimbursement_lines=None,
        leave_accrual_lines=None,
        benefit_lines=None,
        payment_lines=None,
        employee_tax_lines=None,
        employer_tax_lines=None,
        court_order_lines=None,
    ):
        self._pay_slip_id = None
        self._employee_id = None
        self._pay_run_id = None
        self._last_edited = None
        self._first_name = None
        self._last_name = None
        self._total_earnings = None
        self._gross_earnings = None
        self._total_pay = None
        self._total_employer_taxes = None
        self._total_employee_taxes = None
        self._total_deductions = None
        self._total_reimbursements = None
        self._total_court_orders = None
        self._total_benefits = None
        self._bacs_hash = None
        self._payment_method = None
        self._earnings_lines = None
        self._leave_earnings_lines = None
        self._timesheet_earnings_lines = None
        self._deduction_lines = None
        self._reimbursement_lines = None
        self._leave_accrual_lines = None
        self._benefit_lines = None
        self._payment_lines = None
        self._employee_tax_lines = None
        self._employer_tax_lines = None
        self._court_order_lines = None
        self.discriminator = None
        if pay_slip_id is not None:
            self.pay_slip_id = pay_slip_id
        if employee_id is not None:
            self.employee_id = employee_id
        if pay_run_id is not None:
            self.pay_run_id = pay_run_id
        if last_edited is not None:
            self.last_edited = last_edited
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if total_earnings is not None:
            self.total_earnings = total_earnings
        if gross_earnings is not None:
            self.gross_earnings = gross_earnings
        if total_pay is not None:
            self.total_pay = total_pay
        if total_employer_taxes is not None:
            self.total_employer_taxes = total_employer_taxes
        if total_employee_taxes is not None:
            self.total_employee_taxes = total_employee_taxes
        if total_deductions is not None:
            self.total_deductions = total_deductions
        if total_reimbursements is not None:
            self.total_reimbursements = total_reimbursements
        if total_court_orders is not None:
            self.total_court_orders = total_court_orders
        if total_benefits is not None:
            self.total_benefits = total_benefits
        if bacs_hash is not None:
            self.bacs_hash = bacs_hash
        if payment_method is not None:
            self.payment_method = payment_method
        if earnings_lines is not None:
            self.earnings_lines = earnings_lines
        if leave_earnings_lines is not None:
            self.leave_earnings_lines = leave_earnings_lines
        if timesheet_earnings_lines is not None:
            self.timesheet_earnings_lines = timesheet_earnings_lines
        if deduction_lines is not None:
            self.deduction_lines = deduction_lines
        if reimbursement_lines is not None:
            self.reimbursement_lines = reimbursement_lines
        if leave_accrual_lines is not None:
            self.leave_accrual_lines = leave_accrual_lines
        if benefit_lines is not None:
            self.benefit_lines = benefit_lines
        if payment_lines is not None:
            self.payment_lines = payment_lines
        if employee_tax_lines is not None:
            self.employee_tax_lines = employee_tax_lines
        if employer_tax_lines is not None:
            self.employer_tax_lines = employer_tax_lines
        if court_order_lines is not None:
            self.court_order_lines = court_order_lines

    @property
    def pay_slip_id(self):
        return self._pay_slip_id

    @pay_slip_id.setter
    def pay_slip_id(self, pay_slip_id):
        self._pay_slip_id = pay_slip_id

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def pay_run_id(self):
        return self._pay_run_id

    @pay_run_id.setter
    def pay_run_id(self, pay_run_id):
        self._pay_run_id = pay_run_id

    @property
    def last_edited(self):
        return self._last_edited

    @last_edited.setter
    def last_edited(self, last_edited):
        self._last_edited = last_edited

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
    def total_earnings(self):
        return self._total_earnings

    @total_earnings.setter
    def total_earnings(self, total_earnings):
        self._total_earnings = total_earnings

    @property
    def gross_earnings(self):
        return self._gross_earnings

    @gross_earnings.setter
    def gross_earnings(self, gross_earnings):
        self._gross_earnings = gross_earnings

    @property
    def total_pay(self):
        return self._total_pay

    @total_pay.setter
    def total_pay(self, total_pay):
        self._total_pay = total_pay

    @property
    def total_employer_taxes(self):
        return self._total_employer_taxes

    @total_employer_taxes.setter
    def total_employer_taxes(self, total_employer_taxes):
        self._total_employer_taxes = total_employer_taxes

    @property
    def total_employee_taxes(self):
        return self._total_employee_taxes

    @total_employee_taxes.setter
    def total_employee_taxes(self, total_employee_taxes):
        self._total_employee_taxes = total_employee_taxes

    @property
    def total_deductions(self):
        return self._total_deductions

    @total_deductions.setter
    def total_deductions(self, total_deductions):
        self._total_deductions = total_deductions

    @property
    def total_reimbursements(self):
        return self._total_reimbursements

    @total_reimbursements.setter
    def total_reimbursements(self, total_reimbursements):
        self._total_reimbursements = total_reimbursements

    @property
    def total_court_orders(self):
        return self._total_court_orders

    @total_court_orders.setter
    def total_court_orders(self, total_court_orders):
        self._total_court_orders = total_court_orders

    @property
    def total_benefits(self):
        return self._total_benefits

    @total_benefits.setter
    def total_benefits(self, total_benefits):
        self._total_benefits = total_benefits

    @property
    def bacs_hash(self):
        return self._bacs_hash

    @bacs_hash.setter
    def bacs_hash(self, bacs_hash):
        self._bacs_hash = bacs_hash

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        allowed_values = ["Cheque", "Electronically", "Manual", "None"]
        if payment_method:
            if payment_method not in allowed_values:
                raise ValueError(
                    "Invalid value for `payment_method` ({0}), must be one of {1}".format(
                        payment_method, allowed_values
                    )
                )
        self._payment_method = payment_method

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
    def reimbursement_lines(self):
        return self._reimbursement_lines

    @reimbursement_lines.setter
    def reimbursement_lines(self, reimbursement_lines):
        self._reimbursement_lines = reimbursement_lines

    @property
    def leave_accrual_lines(self):
        return self._leave_accrual_lines

    @leave_accrual_lines.setter
    def leave_accrual_lines(self, leave_accrual_lines):
        self._leave_accrual_lines = leave_accrual_lines

    @property
    def benefit_lines(self):
        return self._benefit_lines

    @benefit_lines.setter
    def benefit_lines(self, benefit_lines):
        self._benefit_lines = benefit_lines

    @property
    def payment_lines(self):
        return self._payment_lines

    @payment_lines.setter
    def payment_lines(self, payment_lines):
        self._payment_lines = payment_lines

    @property
    def employee_tax_lines(self):
        return self._employee_tax_lines

    @employee_tax_lines.setter
    def employee_tax_lines(self, employee_tax_lines):
        self._employee_tax_lines = employee_tax_lines

    @property
    def employer_tax_lines(self):
        return self._employer_tax_lines

    @employer_tax_lines.setter
    def employer_tax_lines(self, employer_tax_lines):
        self._employer_tax_lines = employer_tax_lines

    @property
    def court_order_lines(self):
        return self._court_order_lines

    @court_order_lines.setter
    def court_order_lines(self, court_order_lines):
        self._court_order_lines = court_order_lines
