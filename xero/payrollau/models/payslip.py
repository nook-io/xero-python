# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class Payslip(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
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
    ):  # noqa: E501
        """Payslip - a model defined in OpenAPI"""  # noqa: E501

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
        """Gets the employee_id of this Payslip.  # noqa: E501

        The Xero identifier for an employee  # noqa: E501

        :return: The employee_id of this Payslip.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this Payslip.

        The Xero identifier for an employee  # noqa: E501

        :param employee_id: The employee_id of this Payslip.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def payslip_id(self):
        """Gets the payslip_id of this Payslip.  # noqa: E501

        Xero identifier for the payslip  # noqa: E501

        :return: The payslip_id of this Payslip.  # noqa: E501
        :rtype: str
        """
        return self._payslip_id

    @payslip_id.setter
    def payslip_id(self, payslip_id):
        """Sets the payslip_id of this Payslip.

        Xero identifier for the payslip  # noqa: E501

        :param payslip_id: The payslip_id of this Payslip.  # noqa: E501
        :type: str
        """

        self._payslip_id = payslip_id

    @property
    def first_name(self):
        """Gets the first_name of this Payslip.  # noqa: E501

        First name of employee  # noqa: E501

        :return: The first_name of this Payslip.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Payslip.

        First name of employee  # noqa: E501

        :param first_name: The first_name of this Payslip.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Payslip.  # noqa: E501

        Last name of employee  # noqa: E501

        :return: The last_name of this Payslip.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Payslip.

        Last name of employee  # noqa: E501

        :param last_name: The last_name of this Payslip.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def wages(self):
        """Gets the wages of this Payslip.  # noqa: E501

        The Wages for the Payslip  # noqa: E501

        :return: The wages of this Payslip.  # noqa: E501
        :rtype: float
        """
        return self._wages

    @wages.setter
    def wages(self, wages):
        """Sets the wages of this Payslip.

        The Wages for the Payslip  # noqa: E501

        :param wages: The wages of this Payslip.  # noqa: E501
        :type: float
        """

        self._wages = wages

    @property
    def deductions(self):
        """Gets the deductions of this Payslip.  # noqa: E501

        The Deductions for the Payslip  # noqa: E501

        :return: The deductions of this Payslip.  # noqa: E501
        :rtype: float
        """
        return self._deductions

    @deductions.setter
    def deductions(self, deductions):
        """Sets the deductions of this Payslip.

        The Deductions for the Payslip  # noqa: E501

        :param deductions: The deductions of this Payslip.  # noqa: E501
        :type: float
        """

        self._deductions = deductions

    @property
    def tax(self):
        """Gets the tax of this Payslip.  # noqa: E501

        The Tax for the Payslip  # noqa: E501

        :return: The tax of this Payslip.  # noqa: E501
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this Payslip.

        The Tax for the Payslip  # noqa: E501

        :param tax: The tax of this Payslip.  # noqa: E501
        :type: float
        """

        self._tax = tax

    @property
    def super(self):
        """Gets the super of this Payslip.  # noqa: E501

        The Super for the Payslip  # noqa: E501

        :return: The super of this Payslip.  # noqa: E501
        :rtype: float
        """
        return self._super

    @super.setter
    def super(self, super):
        """Sets the super of this Payslip.

        The Super for the Payslip  # noqa: E501

        :param super: The super of this Payslip.  # noqa: E501
        :type: float
        """

        self._super = super

    @property
    def reimbursements(self):
        """Gets the reimbursements of this Payslip.  # noqa: E501

        The Reimbursements for the Payslip  # noqa: E501

        :return: The reimbursements of this Payslip.  # noqa: E501
        :rtype: float
        """
        return self._reimbursements

    @reimbursements.setter
    def reimbursements(self, reimbursements):
        """Sets the reimbursements of this Payslip.

        The Reimbursements for the Payslip  # noqa: E501

        :param reimbursements: The reimbursements of this Payslip.  # noqa: E501
        :type: float
        """

        self._reimbursements = reimbursements

    @property
    def net_pay(self):
        """Gets the net_pay of this Payslip.  # noqa: E501

        The NetPay for the Payslip  # noqa: E501

        :return: The net_pay of this Payslip.  # noqa: E501
        :rtype: float
        """
        return self._net_pay

    @net_pay.setter
    def net_pay(self, net_pay):
        """Sets the net_pay of this Payslip.

        The NetPay for the Payslip  # noqa: E501

        :param net_pay: The net_pay of this Payslip.  # noqa: E501
        :type: float
        """

        self._net_pay = net_pay

    @property
    def earnings_lines(self):
        """Gets the earnings_lines of this Payslip.  # noqa: E501


        :return: The earnings_lines of this Payslip.  # noqa: E501
        :rtype: list[EarningsLine]
        """
        return self._earnings_lines

    @earnings_lines.setter
    def earnings_lines(self, earnings_lines):
        """Sets the earnings_lines of this Payslip.


        :param earnings_lines: The earnings_lines of this Payslip.  # noqa: E501
        :type: list[EarningsLine]
        """

        self._earnings_lines = earnings_lines

    @property
    def leave_earnings_lines(self):
        """Gets the leave_earnings_lines of this Payslip.  # noqa: E501


        :return: The leave_earnings_lines of this Payslip.  # noqa: E501
        :rtype: list[LeaveEarningsLine]
        """
        return self._leave_earnings_lines

    @leave_earnings_lines.setter
    def leave_earnings_lines(self, leave_earnings_lines):
        """Sets the leave_earnings_lines of this Payslip.


        :param leave_earnings_lines: The leave_earnings_lines of this Payslip.  # noqa: E501
        :type: list[LeaveEarningsLine]
        """

        self._leave_earnings_lines = leave_earnings_lines

    @property
    def timesheet_earnings_lines(self):
        """Gets the timesheet_earnings_lines of this Payslip.  # noqa: E501


        :return: The timesheet_earnings_lines of this Payslip.  # noqa: E501
        :rtype: list[EarningsLine]
        """
        return self._timesheet_earnings_lines

    @timesheet_earnings_lines.setter
    def timesheet_earnings_lines(self, timesheet_earnings_lines):
        """Sets the timesheet_earnings_lines of this Payslip.


        :param timesheet_earnings_lines: The timesheet_earnings_lines of this Payslip.  # noqa: E501
        :type: list[EarningsLine]
        """

        self._timesheet_earnings_lines = timesheet_earnings_lines

    @property
    def deduction_lines(self):
        """Gets the deduction_lines of this Payslip.  # noqa: E501


        :return: The deduction_lines of this Payslip.  # noqa: E501
        :rtype: list[DeductionLine]
        """
        return self._deduction_lines

    @deduction_lines.setter
    def deduction_lines(self, deduction_lines):
        """Sets the deduction_lines of this Payslip.


        :param deduction_lines: The deduction_lines of this Payslip.  # noqa: E501
        :type: list[DeductionLine]
        """

        self._deduction_lines = deduction_lines

    @property
    def leave_accrual_lines(self):
        """Gets the leave_accrual_lines of this Payslip.  # noqa: E501


        :return: The leave_accrual_lines of this Payslip.  # noqa: E501
        :rtype: list[LeaveAccrualLine]
        """
        return self._leave_accrual_lines

    @leave_accrual_lines.setter
    def leave_accrual_lines(self, leave_accrual_lines):
        """Sets the leave_accrual_lines of this Payslip.


        :param leave_accrual_lines: The leave_accrual_lines of this Payslip.  # noqa: E501
        :type: list[LeaveAccrualLine]
        """

        self._leave_accrual_lines = leave_accrual_lines

    @property
    def reimbursement_lines(self):
        """Gets the reimbursement_lines of this Payslip.  # noqa: E501


        :return: The reimbursement_lines of this Payslip.  # noqa: E501
        :rtype: list[ReimbursementLine]
        """
        return self._reimbursement_lines

    @reimbursement_lines.setter
    def reimbursement_lines(self, reimbursement_lines):
        """Sets the reimbursement_lines of this Payslip.


        :param reimbursement_lines: The reimbursement_lines of this Payslip.  # noqa: E501
        :type: list[ReimbursementLine]
        """

        self._reimbursement_lines = reimbursement_lines

    @property
    def superannuation_lines(self):
        """Gets the superannuation_lines of this Payslip.  # noqa: E501


        :return: The superannuation_lines of this Payslip.  # noqa: E501
        :rtype: list[SuperannuationLine]
        """
        return self._superannuation_lines

    @superannuation_lines.setter
    def superannuation_lines(self, superannuation_lines):
        """Sets the superannuation_lines of this Payslip.


        :param superannuation_lines: The superannuation_lines of this Payslip.  # noqa: E501
        :type: list[SuperannuationLine]
        """

        self._superannuation_lines = superannuation_lines

    @property
    def tax_lines(self):
        """Gets the tax_lines of this Payslip.  # noqa: E501


        :return: The tax_lines of this Payslip.  # noqa: E501
        :rtype: list[TaxLine]
        """
        return self._tax_lines

    @tax_lines.setter
    def tax_lines(self, tax_lines):
        """Sets the tax_lines of this Payslip.


        :param tax_lines: The tax_lines of this Payslip.  # noqa: E501
        :type: list[TaxLine]
        """

        self._tax_lines = tax_lines

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Payslip.  # noqa: E501

        Last modified timestamp  # noqa: E501

        :return: The updated_date_utc of this Payslip.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Payslip.

        Last modified timestamp  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Payslip.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc
