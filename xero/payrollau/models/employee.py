# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class Employee(BaseModel):
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
        "first_name": "str",
        "last_name": "str",
        "date_of_birth": "date[ms-format]",
        "home_address": "HomeAddress",
        "start_date": "date[ms-format]",
        "title": "str",
        "middle_names": "str",
        "email": "str",
        "gender": "str",
        "phone": "str",
        "mobile": "str",
        "twitter_user_name": "str",
        "is_authorised_to_approve_leave": "bool",
        "is_authorised_to_approve_timesheets": "bool",
        "job_title": "str",
        "classification": "str",
        "ordinary_earnings_rate_id": "str",
        "payroll_calendar_id": "str",
        "employee_group_name": "str",
        "employee_id": "str",
        "termination_date": "date[ms-format]",
        "termination_reason": "str",
        "bank_accounts": "list[BankAccount]",
        "pay_template": "PayTemplate",
        "opening_balances": "OpeningBalances",
        "tax_declaration": "TaxDeclaration",
        "income_type": "IncomeType",
        "employment_type": "EmploymentType",
        "country_of_residence": "CountryOfResidence",
        "is_stp2_qualified": "bool",
        "leave_balances": "list[LeaveBalance]",
        "leave_lines": "list[LeaveLine]",
        "super_memberships": "list[SuperMembership]",
        "status": "EmployeeStatus",
        "updated_date_utc": "datetime[ms-format]",
        "validation_errors": "list[ValidationError]",
    }

    attribute_map = {
        "first_name": "FirstName",
        "last_name": "LastName",
        "date_of_birth": "DateOfBirth",
        "home_address": "HomeAddress",
        "start_date": "StartDate",
        "title": "Title",
        "middle_names": "MiddleNames",
        "email": "Email",
        "gender": "Gender",
        "phone": "Phone",
        "mobile": "Mobile",
        "twitter_user_name": "TwitterUserName",
        "is_authorised_to_approve_leave": "IsAuthorisedToApproveLeave",
        "is_authorised_to_approve_timesheets": "IsAuthorisedToApproveTimesheets",
        "job_title": "JobTitle",
        "classification": "Classification",
        "ordinary_earnings_rate_id": "OrdinaryEarningsRateID",
        "payroll_calendar_id": "PayrollCalendarID",
        "employee_group_name": "EmployeeGroupName",
        "employee_id": "EmployeeID",
        "termination_date": "TerminationDate",
        "termination_reason": "TerminationReason",
        "bank_accounts": "BankAccounts",
        "pay_template": "PayTemplate",
        "opening_balances": "OpeningBalances",
        "tax_declaration": "TaxDeclaration",
        "income_type": "IncomeType",
        "employment_type": "EmploymentType",
        "country_of_residence": "CountryOfResidence",
        "is_stp2_qualified": "IsSTP2Qualified",
        "leave_balances": "LeaveBalances",
        "leave_lines": "LeaveLines",
        "super_memberships": "SuperMemberships",
        "status": "Status",
        "updated_date_utc": "UpdatedDateUTC",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        first_name=None,
        last_name=None,
        date_of_birth=None,
        home_address=None,
        start_date=None,
        title=None,
        middle_names=None,
        email=None,
        gender=None,
        phone=None,
        mobile=None,
        twitter_user_name=None,
        is_authorised_to_approve_leave=None,
        is_authorised_to_approve_timesheets=None,
        job_title=None,
        classification=None,
        ordinary_earnings_rate_id=None,
        payroll_calendar_id=None,
        employee_group_name=None,
        employee_id=None,
        termination_date=None,
        termination_reason=None,
        bank_accounts=None,
        pay_template=None,
        opening_balances=None,
        tax_declaration=None,
        income_type=None,
        employment_type=None,
        country_of_residence=None,
        is_stp2_qualified=None,
        leave_balances=None,
        leave_lines=None,
        super_memberships=None,
        status=None,
        updated_date_utc=None,
        validation_errors=None,
    ):  # noqa: E501
        """Employee - a model defined in OpenAPI"""  # noqa: E501

        self._first_name = None
        self._last_name = None
        self._date_of_birth = None
        self._home_address = None
        self._start_date = None
        self._title = None
        self._middle_names = None
        self._email = None
        self._gender = None
        self._phone = None
        self._mobile = None
        self._twitter_user_name = None
        self._is_authorised_to_approve_leave = None
        self._is_authorised_to_approve_timesheets = None
        self._job_title = None
        self._classification = None
        self._ordinary_earnings_rate_id = None
        self._payroll_calendar_id = None
        self._employee_group_name = None
        self._employee_id = None
        self._termination_date = None
        self._termination_reason = None
        self._bank_accounts = None
        self._pay_template = None
        self._opening_balances = None
        self._tax_declaration = None
        self._income_type = None
        self._employment_type = None
        self._country_of_residence = None
        self._is_stp2_qualified = None
        self._leave_balances = None
        self._leave_lines = None
        self._super_memberships = None
        self._status = None
        self._updated_date_utc = None
        self._validation_errors = None
        self.discriminator = None

        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        if home_address is not None:
            self.home_address = home_address
        if start_date is not None:
            self.start_date = start_date
        if title is not None:
            self.title = title
        if middle_names is not None:
            self.middle_names = middle_names
        if email is not None:
            self.email = email
        if gender is not None:
            self.gender = gender
        if phone is not None:
            self.phone = phone
        if mobile is not None:
            self.mobile = mobile
        if twitter_user_name is not None:
            self.twitter_user_name = twitter_user_name
        if is_authorised_to_approve_leave is not None:
            self.is_authorised_to_approve_leave = is_authorised_to_approve_leave
        if is_authorised_to_approve_timesheets is not None:
            self.is_authorised_to_approve_timesheets = (
                is_authorised_to_approve_timesheets
            )
        if job_title is not None:
            self.job_title = job_title
        if classification is not None:
            self.classification = classification
        if ordinary_earnings_rate_id is not None:
            self.ordinary_earnings_rate_id = ordinary_earnings_rate_id
        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        if employee_group_name is not None:
            self.employee_group_name = employee_group_name
        if employee_id is not None:
            self.employee_id = employee_id
        if termination_date is not None:
            self.termination_date = termination_date
        if termination_reason is not None:
            self.termination_reason = termination_reason
        if bank_accounts is not None:
            self.bank_accounts = bank_accounts
        if pay_template is not None:
            self.pay_template = pay_template
        if opening_balances is not None:
            self.opening_balances = opening_balances
        if tax_declaration is not None:
            self.tax_declaration = tax_declaration
        if income_type is not None:
            self.income_type = income_type
        if employment_type is not None:
            self.employment_type = employment_type
        if country_of_residence is not None:
            self.country_of_residence = country_of_residence
        if is_stp2_qualified is not None:
            self.is_stp2_qualified = is_stp2_qualified
        if leave_balances is not None:
            self.leave_balances = leave_balances
        if leave_lines is not None:
            self.leave_lines = leave_lines
        if super_memberships is not None:
            self.super_memberships = super_memberships
        if status is not None:
            self.status = status
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def first_name(self):
        """Gets the first_name of this Employee.  # noqa: E501

        First name of employee  # noqa: E501

        :return: The first_name of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Employee.

        First name of employee  # noqa: E501

        :param first_name: The first_name of this Employee.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError(
                "Invalid value for `first_name`, must not be `None`"
            )  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Employee.  # noqa: E501

        Last name of employee  # noqa: E501

        :return: The last_name of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Employee.

        Last name of employee  # noqa: E501

        :param last_name: The last_name of this Employee.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError(
                "Invalid value for `last_name`, must not be `None`"
            )  # noqa: E501

        self._last_name = last_name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this Employee.  # noqa: E501

        Date of birth of the employee (YYYY-MM-DD)  # noqa: E501

        :return: The date_of_birth of this Employee.  # noqa: E501
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this Employee.

        Date of birth of the employee (YYYY-MM-DD)  # noqa: E501

        :param date_of_birth: The date_of_birth of this Employee.  # noqa: E501
        :type: date
        """
        if date_of_birth is None:
            raise ValueError(
                "Invalid value for `date_of_birth`, must not be `None`"
            )  # noqa: E501

        self._date_of_birth = date_of_birth

    @property
    def home_address(self):
        """Gets the home_address of this Employee.  # noqa: E501


        :return: The home_address of this Employee.  # noqa: E501
        :rtype: HomeAddress
        """
        return self._home_address

    @home_address.setter
    def home_address(self, home_address):
        """Sets the home_address of this Employee.


        :param home_address: The home_address of this Employee.  # noqa: E501
        :type: HomeAddress
        """

        self._home_address = home_address

    @property
    def start_date(self):
        """Gets the start_date of this Employee.  # noqa: E501

        Start date for an employee (YYYY-MM-DD)  # noqa: E501

        :return: The start_date of this Employee.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Employee.

        Start date for an employee (YYYY-MM-DD)  # noqa: E501

        :param start_date: The start_date of this Employee.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def title(self):
        """Gets the title of this Employee.  # noqa: E501

        Title of the employee  # noqa: E501

        :return: The title of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Employee.

        Title of the employee  # noqa: E501

        :param title: The title of this Employee.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def middle_names(self):
        """Gets the middle_names of this Employee.  # noqa: E501

        Middle name(s) of the employee  # noqa: E501

        :return: The middle_names of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._middle_names

    @middle_names.setter
    def middle_names(self, middle_names):
        """Sets the middle_names of this Employee.

        Middle name(s) of the employee  # noqa: E501

        :param middle_names: The middle_names of this Employee.  # noqa: E501
        :type: str
        """

        self._middle_names = middle_names

    @property
    def email(self):
        """Gets the email of this Employee.  # noqa: E501

        The email address for the employee  # noqa: E501

        :return: The email of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Employee.

        The email address for the employee  # noqa: E501

        :param email: The email of this Employee.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def gender(self):
        """Gets the gender of this Employee.  # noqa: E501

        The employee’s gender. See Employee Gender  # noqa: E501

        :return: The gender of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Employee.

        The employee’s gender. See Employee Gender  # noqa: E501

        :param gender: The gender of this Employee.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "M", "F", "I", "None"]  # noqa: E501

        if gender:
            if gender not in allowed_values:
                raise ValueError(
                    "Invalid value for `gender` ({0}), must be one of {1}".format(  # noqa: E501
                        gender, allowed_values
                    )
                )

        self._gender = gender

    @property
    def phone(self):
        """Gets the phone of this Employee.  # noqa: E501

        Employee phone number  # noqa: E501

        :return: The phone of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Employee.

        Employee phone number  # noqa: E501

        :param phone: The phone of this Employee.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def mobile(self):
        """Gets the mobile of this Employee.  # noqa: E501

        Employee mobile number  # noqa: E501

        :return: The mobile of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this Employee.

        Employee mobile number  # noqa: E501

        :param mobile: The mobile of this Employee.  # noqa: E501
        :type: str
        """

        self._mobile = mobile

    @property
    def twitter_user_name(self):
        """Gets the twitter_user_name of this Employee.  # noqa: E501

        Employee’s twitter name  # noqa: E501

        :return: The twitter_user_name of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._twitter_user_name

    @twitter_user_name.setter
    def twitter_user_name(self, twitter_user_name):
        """Sets the twitter_user_name of this Employee.

        Employee’s twitter name  # noqa: E501

        :param twitter_user_name: The twitter_user_name of this Employee.  # noqa: E501
        :type: str
        """

        self._twitter_user_name = twitter_user_name

    @property
    def is_authorised_to_approve_leave(self):
        """Gets the is_authorised_to_approve_leave of this Employee.  # noqa: E501

        Authorised to approve other employees' leave requests  # noqa: E501

        :return: The is_authorised_to_approve_leave of this Employee.  # noqa: E501
        :rtype: bool
        """
        return self._is_authorised_to_approve_leave

    @is_authorised_to_approve_leave.setter
    def is_authorised_to_approve_leave(self, is_authorised_to_approve_leave):
        """Sets the is_authorised_to_approve_leave of this Employee.

        Authorised to approve other employees' leave requests  # noqa: E501

        :param is_authorised_to_approve_leave: The is_authorised_to_approve_leave of this Employee.  # noqa: E501
        :type: bool
        """

        self._is_authorised_to_approve_leave = is_authorised_to_approve_leave

    @property
    def is_authorised_to_approve_timesheets(self):
        """Gets the is_authorised_to_approve_timesheets of this Employee.  # noqa: E501

        Authorised to approve timesheets  # noqa: E501

        :return: The is_authorised_to_approve_timesheets of this Employee.  # noqa: E501
        :rtype: bool
        """
        return self._is_authorised_to_approve_timesheets

    @is_authorised_to_approve_timesheets.setter
    def is_authorised_to_approve_timesheets(self, is_authorised_to_approve_timesheets):
        """Sets the is_authorised_to_approve_timesheets of this Employee.

        Authorised to approve timesheets  # noqa: E501

        :param is_authorised_to_approve_timesheets: The is_authorised_to_approve_timesheets of this Employee.  # noqa: E501
        :type: bool
        """

        self._is_authorised_to_approve_timesheets = is_authorised_to_approve_timesheets

    @property
    def job_title(self):
        """Gets the job_title of this Employee.  # noqa: E501

        JobTitle of the employee  # noqa: E501

        :return: The job_title of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this Employee.

        JobTitle of the employee  # noqa: E501

        :param job_title: The job_title of this Employee.  # noqa: E501
        :type: str
        """

        self._job_title = job_title

    @property
    def classification(self):
        """Gets the classification of this Employee.  # noqa: E501

        Employees classification  # noqa: E501

        :return: The classification of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this Employee.

        Employees classification  # noqa: E501

        :param classification: The classification of this Employee.  # noqa: E501
        :type: str
        """

        self._classification = classification

    @property
    def ordinary_earnings_rate_id(self):
        """Gets the ordinary_earnings_rate_id of this Employee.  # noqa: E501

        Xero unique identifier for earnings rate  # noqa: E501

        :return: The ordinary_earnings_rate_id of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._ordinary_earnings_rate_id

    @ordinary_earnings_rate_id.setter
    def ordinary_earnings_rate_id(self, ordinary_earnings_rate_id):
        """Sets the ordinary_earnings_rate_id of this Employee.

        Xero unique identifier for earnings rate  # noqa: E501

        :param ordinary_earnings_rate_id: The ordinary_earnings_rate_id of this Employee.  # noqa: E501
        :type: str
        """

        self._ordinary_earnings_rate_id = ordinary_earnings_rate_id

    @property
    def payroll_calendar_id(self):
        """Gets the payroll_calendar_id of this Employee.  # noqa: E501

        Xero unique identifier for payroll calendar for the employee  # noqa: E501

        :return: The payroll_calendar_id of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        """Sets the payroll_calendar_id of this Employee.

        Xero unique identifier for payroll calendar for the employee  # noqa: E501

        :param payroll_calendar_id: The payroll_calendar_id of this Employee.  # noqa: E501
        :type: str
        """

        self._payroll_calendar_id = payroll_calendar_id

    @property
    def employee_group_name(self):
        """Gets the employee_group_name of this Employee.  # noqa: E501

        The Employee Group allows you to report on payroll expenses and liabilities for each group of employees  # noqa: E501

        :return: The employee_group_name of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._employee_group_name

    @employee_group_name.setter
    def employee_group_name(self, employee_group_name):
        """Sets the employee_group_name of this Employee.

        The Employee Group allows you to report on payroll expenses and liabilities for each group of employees  # noqa: E501

        :param employee_group_name: The employee_group_name of this Employee.  # noqa: E501
        :type: str
        """

        self._employee_group_name = employee_group_name

    @property
    def employee_id(self):
        """Gets the employee_id of this Employee.  # noqa: E501

        Xero unique identifier for an Employee  # noqa: E501

        :return: The employee_id of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this Employee.

        Xero unique identifier for an Employee  # noqa: E501

        :param employee_id: The employee_id of this Employee.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def termination_date(self):
        """Gets the termination_date of this Employee.  # noqa: E501

        Employee Termination Date (YYYY-MM-DD)  # noqa: E501

        :return: The termination_date of this Employee.  # noqa: E501
        :rtype: date
        """
        return self._termination_date

    @termination_date.setter
    def termination_date(self, termination_date):
        """Sets the termination_date of this Employee.

        Employee Termination Date (YYYY-MM-DD)  # noqa: E501

        :param termination_date: The termination_date of this Employee.  # noqa: E501
        :type: date
        """

        self._termination_date = termination_date

    @property
    def termination_reason(self):
        """Gets the termination_reason of this Employee.  # noqa: E501

        * `V` Voluntary cessation - An employee resignation, retirement, domestic or pressing necessity or abandonment of employment * `I` Ill health - An employee resignation due to medical condition that prevents the continuation of employment, such as for illness, ill-health, medical unfitness or total permanent disability * `D` Deceased - The death of an employee * `R` Redundancy - An employer-initiated termination of employment due to a genuine redundancy or approved early retirement scheme * `F` Dismissal - An employer-initiated termination of employment due to dismissal, inability to perform the required work, misconduct or inefficiency * `C` Contract cessation - The natural conclusion of a limited employment relationship due to contract/engagement duration or task completion, seasonal work completion, or to cease casuals that are no longer required * `T` Transfer - The administrative arrangements performed to transfer employees across payroll systems, move them temporarily to another employer (machinery of government for public servants), transfer of business, move them to outsourcing arrangements or other such technical activities.   # noqa: E501

        :return: The termination_reason of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._termination_reason

    @termination_reason.setter
    def termination_reason(self, termination_reason):
        """Sets the termination_reason of this Employee.

        * `V` Voluntary cessation - An employee resignation, retirement, domestic or pressing necessity or abandonment of employment * `I` Ill health - An employee resignation due to medical condition that prevents the continuation of employment, such as for illness, ill-health, medical unfitness or total permanent disability * `D` Deceased - The death of an employee * `R` Redundancy - An employer-initiated termination of employment due to a genuine redundancy or approved early retirement scheme * `F` Dismissal - An employer-initiated termination of employment due to dismissal, inability to perform the required work, misconduct or inefficiency * `C` Contract cessation - The natural conclusion of a limited employment relationship due to contract/engagement duration or task completion, seasonal work completion, or to cease casuals that are no longer required * `T` Transfer - The administrative arrangements performed to transfer employees across payroll systems, move them temporarily to another employer (machinery of government for public servants), transfer of business, move them to outsourcing arrangements or other such technical activities.   # noqa: E501

        :param termination_reason: The termination_reason of this Employee.  # noqa: E501
        :type: str
        """
        allowed_values = ["V", "I", "D", "R", "F", "C", "T", "None"]  # noqa: E501

        if termination_reason:
            if termination_reason not in allowed_values:
                raise ValueError(
                    "Invalid value for `termination_reason` ({0}), must be one of {1}".format(  # noqa: E501
                        termination_reason, allowed_values
                    )
                )

        self._termination_reason = termination_reason

    @property
    def bank_accounts(self):
        """Gets the bank_accounts of this Employee.  # noqa: E501


        :return: The bank_accounts of this Employee.  # noqa: E501
        :rtype: list[BankAccount]
        """
        return self._bank_accounts

    @bank_accounts.setter
    def bank_accounts(self, bank_accounts):
        """Sets the bank_accounts of this Employee.


        :param bank_accounts: The bank_accounts of this Employee.  # noqa: E501
        :type: list[BankAccount]
        """

        self._bank_accounts = bank_accounts

    @property
    def pay_template(self):
        """Gets the pay_template of this Employee.  # noqa: E501


        :return: The pay_template of this Employee.  # noqa: E501
        :rtype: PayTemplate
        """
        return self._pay_template

    @pay_template.setter
    def pay_template(self, pay_template):
        """Sets the pay_template of this Employee.


        :param pay_template: The pay_template of this Employee.  # noqa: E501
        :type: PayTemplate
        """

        self._pay_template = pay_template

    @property
    def opening_balances(self):
        """Gets the opening_balances of this Employee.  # noqa: E501


        :return: The opening_balances of this Employee.  # noqa: E501
        :rtype: OpeningBalances
        """
        return self._opening_balances

    @opening_balances.setter
    def opening_balances(self, opening_balances):
        """Sets the opening_balances of this Employee.


        :param opening_balances: The opening_balances of this Employee.  # noqa: E501
        :type: OpeningBalances
        """

        self._opening_balances = opening_balances

    @property
    def tax_declaration(self):
        """Gets the tax_declaration of this Employee.  # noqa: E501


        :return: The tax_declaration of this Employee.  # noqa: E501
        :rtype: TaxDeclaration
        """
        return self._tax_declaration

    @tax_declaration.setter
    def tax_declaration(self, tax_declaration):
        """Sets the tax_declaration of this Employee.


        :param tax_declaration: The tax_declaration of this Employee.  # noqa: E501
        :type: TaxDeclaration
        """

        self._tax_declaration = tax_declaration

    @property
    def income_type(self):
        """Gets the income_type of this Employee.  # noqa: E501


        :return: The income_type of this Employee.  # noqa: E501
        :rtype: IncomeType
        """
        return self._income_type

    @income_type.setter
    def income_type(self, income_type):
        """Sets the income_type of this Employee.


        :param income_type: The income_type of this Employee.  # noqa: E501
        :type: IncomeType
        """

        self._income_type = income_type

    @property
    def employment_type(self):
        """Gets the employment_type of this Employee.  # noqa: E501


        :return: The employment_type of this Employee.  # noqa: E501
        :rtype: EmploymentType
        """
        return self._employment_type

    @employment_type.setter
    def employment_type(self, employment_type):
        """Sets the employment_type of this Employee.


        :param employment_type: The employment_type of this Employee.  # noqa: E501
        :type: EmploymentType
        """

        self._employment_type = employment_type

    @property
    def country_of_residence(self):
        """Gets the country_of_residence of this Employee.  # noqa: E501


        :return: The country_of_residence of this Employee.  # noqa: E501
        :rtype: CountryOfResidence
        """
        return self._country_of_residence

    @country_of_residence.setter
    def country_of_residence(self, country_of_residence):
        """Sets the country_of_residence of this Employee.


        :param country_of_residence: The country_of_residence of this Employee.  # noqa: E501
        :type: CountryOfResidence
        """

        self._country_of_residence = country_of_residence

    @property
    def is_stp2_qualified(self):
        """Gets the is_stp2_qualified of this Employee.  # noqa: E501

        Indicates if the employee has been updated for STP Phase 2 compliance. Doesn't indicate that the employee is payable.  # noqa: E501

        :return: The is_stp2_qualified of this Employee.  # noqa: E501
        :rtype: bool
        """
        return self._is_stp2_qualified

    @is_stp2_qualified.setter
    def is_stp2_qualified(self, is_stp2_qualified):
        """Sets the is_stp2_qualified of this Employee.

        Indicates if the employee has been updated for STP Phase 2 compliance. Doesn't indicate that the employee is payable.  # noqa: E501

        :param is_stp2_qualified: The is_stp2_qualified of this Employee.  # noqa: E501
        :type: bool
        """

        self._is_stp2_qualified = is_stp2_qualified

    @property
    def leave_balances(self):
        """Gets the leave_balances of this Employee.  # noqa: E501


        :return: The leave_balances of this Employee.  # noqa: E501
        :rtype: list[LeaveBalance]
        """
        return self._leave_balances

    @leave_balances.setter
    def leave_balances(self, leave_balances):
        """Sets the leave_balances of this Employee.


        :param leave_balances: The leave_balances of this Employee.  # noqa: E501
        :type: list[LeaveBalance]
        """

        self._leave_balances = leave_balances

    @property
    def leave_lines(self):
        """Gets the leave_lines of this Employee.  # noqa: E501


        :return: The leave_lines of this Employee.  # noqa: E501
        :rtype: list[LeaveLine]
        """
        return self._leave_lines

    @leave_lines.setter
    def leave_lines(self, leave_lines):
        """Sets the leave_lines of this Employee.


        :param leave_lines: The leave_lines of this Employee.  # noqa: E501
        :type: list[LeaveLine]
        """

        self._leave_lines = leave_lines

    @property
    def super_memberships(self):
        """Gets the super_memberships of this Employee.  # noqa: E501


        :return: The super_memberships of this Employee.  # noqa: E501
        :rtype: list[SuperMembership]
        """
        return self._super_memberships

    @super_memberships.setter
    def super_memberships(self, super_memberships):
        """Sets the super_memberships of this Employee.


        :param super_memberships: The super_memberships of this Employee.  # noqa: E501
        :type: list[SuperMembership]
        """

        self._super_memberships = super_memberships

    @property
    def status(self):
        """Gets the status of this Employee.  # noqa: E501


        :return: The status of this Employee.  # noqa: E501
        :rtype: EmployeeStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Employee.


        :param status: The status of this Employee.  # noqa: E501
        :type: EmployeeStatus
        """

        self._status = status

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Employee.  # noqa: E501

        Last modified timestamp  # noqa: E501

        :return: The updated_date_utc of this Employee.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Employee.

        Last modified timestamp  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Employee.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def validation_errors(self):
        """Gets the validation_errors of this Employee.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this Employee.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this Employee.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this Employee.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors
