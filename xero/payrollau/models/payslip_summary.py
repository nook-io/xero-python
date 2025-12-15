from xero.models import BaseModel


class PayslipSummary(BaseModel):
    openapi_types = {
        "employee_id": "str",
        "payslip_id": "str",
        "first_name": "str",
        "last_name": "str",
        "employee_group": "str",
        "wages": "float",
        "deductions": "float",
        "tax": "float",
        "super": "float",
        "reimbursements": "float",
        "net_pay": "float",
        "updated_date_utc": "datetime[ms-format]",
    }
    attribute_map = {
        "employee_id": "EmployeeID",
        "payslip_id": "PayslipID",
        "first_name": "FirstName",
        "last_name": "LastName",
        "employee_group": "EmployeeGroup",
        "wages": "Wages",
        "deductions": "Deductions",
        "tax": "Tax",
        "super": "Super",
        "reimbursements": "Reimbursements",
        "net_pay": "NetPay",
        "updated_date_utc": "UpdatedDateUTC",
    }

    def __init__(
        self,
        employee_id=None,
        payslip_id=None,
        first_name=None,
        last_name=None,
        employee_group=None,
        wages=None,
        deductions=None,
        tax=None,
        super=None,
        reimbursements=None,
        net_pay=None,
        updated_date_utc=None,
    ):
        self._employee_id = None
        self._payslip_id = None
        self._first_name = None
        self._last_name = None
        self._employee_group = None
        self._wages = None
        self._deductions = None
        self._tax = None
        self._super = None
        self._reimbursements = None
        self._net_pay = None
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
        if employee_group is not None:
            self.employee_group = employee_group
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
    def employee_group(self):
        return self._employee_group

    @employee_group.setter
    def employee_group(self, employee_group):
        self._employee_group = employee_group

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
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc
