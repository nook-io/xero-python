from xero.models import BaseModel


class PayRun(BaseModel):
    openapi_types = {
        "payroll_calendar_id": "str",
        "pay_run_id": "str",
        "pay_run_period_start_date": "date[ms-format]",
        "pay_run_period_end_date": "date[ms-format]",
        "pay_run_status": "PayRunStatus",
        "payment_date": "date[ms-format]",
        "payslip_message": "str",
        "updated_date_utc": "datetime[ms-format]",
        "payslips": "list[PayslipSummary]",
        "wages": "float",
        "deductions": "float",
        "tax": "float",
        "super": "float",
        "reimbursement": "float",
        "net_pay": "float",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "payroll_calendar_id": "PayrollCalendarID",
        "pay_run_id": "PayRunID",
        "pay_run_period_start_date": "PayRunPeriodStartDate",
        "pay_run_period_end_date": "PayRunPeriodEndDate",
        "pay_run_status": "PayRunStatus",
        "payment_date": "PaymentDate",
        "payslip_message": "PayslipMessage",
        "updated_date_utc": "UpdatedDateUTC",
        "payslips": "Payslips",
        "wages": "Wages",
        "deductions": "Deductions",
        "tax": "Tax",
        "super": "Super",
        "reimbursement": "Reimbursement",
        "net_pay": "NetPay",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        payroll_calendar_id=None,
        pay_run_id=None,
        pay_run_period_start_date=None,
        pay_run_period_end_date=None,
        pay_run_status=None,
        payment_date=None,
        payslip_message=None,
        updated_date_utc=None,
        payslips=None,
        wages=None,
        deductions=None,
        tax=None,
        super=None,
        reimbursement=None,
        net_pay=None,
        validation_errors=None,
    ):
        self._payroll_calendar_id = None
        self._pay_run_id = None
        self._pay_run_period_start_date = None
        self._pay_run_period_end_date = None
        self._pay_run_status = None
        self._payment_date = None
        self._payslip_message = None
        self._updated_date_utc = None
        self._payslips = None
        self._wages = None
        self._deductions = None
        self._tax = None
        self._super = None
        self._reimbursement = None
        self._net_pay = None
        self._validation_errors = None
        self.discriminator = None
        self.payroll_calendar_id = payroll_calendar_id
        if pay_run_id is not None:
            self.pay_run_id = pay_run_id
        if pay_run_period_start_date is not None:
            self.pay_run_period_start_date = pay_run_period_start_date
        if pay_run_period_end_date is not None:
            self.pay_run_period_end_date = pay_run_period_end_date
        if pay_run_status is not None:
            self.pay_run_status = pay_run_status
        if payment_date is not None:
            self.payment_date = payment_date
        if payslip_message is not None:
            self.payslip_message = payslip_message
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if payslips is not None:
            self.payslips = payslips
        if wages is not None:
            self.wages = wages
        if deductions is not None:
            self.deductions = deductions
        if tax is not None:
            self.tax = tax
        if super is not None:
            self.super = super
        if reimbursement is not None:
            self.reimbursement = reimbursement
        if net_pay is not None:
            self.net_pay = net_pay
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def payroll_calendar_id(self):
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        if payroll_calendar_id is None:
            raise ValueError(
                "Invalid value for `payroll_calendar_id`, must not be `None`"
            )
        self._payroll_calendar_id = payroll_calendar_id

    @property
    def pay_run_id(self):
        return self._pay_run_id

    @pay_run_id.setter
    def pay_run_id(self, pay_run_id):
        self._pay_run_id = pay_run_id

    @property
    def pay_run_period_start_date(self):
        return self._pay_run_period_start_date

    @pay_run_period_start_date.setter
    def pay_run_period_start_date(self, pay_run_period_start_date):
        self._pay_run_period_start_date = pay_run_period_start_date

    @property
    def pay_run_period_end_date(self):
        return self._pay_run_period_end_date

    @pay_run_period_end_date.setter
    def pay_run_period_end_date(self, pay_run_period_end_date):
        self._pay_run_period_end_date = pay_run_period_end_date

    @property
    def pay_run_status(self):
        return self._pay_run_status

    @pay_run_status.setter
    def pay_run_status(self, pay_run_status):
        self._pay_run_status = pay_run_status

    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        self._payment_date = payment_date

    @property
    def payslip_message(self):
        return self._payslip_message

    @payslip_message.setter
    def payslip_message(self, payslip_message):
        self._payslip_message = payslip_message

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def payslips(self):
        return self._payslips

    @payslips.setter
    def payslips(self, payslips):
        self._payslips = payslips

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
    def reimbursement(self):
        return self._reimbursement

    @reimbursement.setter
    def reimbursement(self, reimbursement):
        self._reimbursement = reimbursement

    @property
    def net_pay(self):
        return self._net_pay

    @net_pay.setter
    def net_pay(self, net_pay):
        self._net_pay = net_pay

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
