from xero.models import BaseModel


class Employee(BaseModel):
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
    ):
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
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")
        self._last_name = last_name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        if date_of_birth is None:
            raise ValueError("Invalid value for `date_of_birth`, must not be `None`")
        self._date_of_birth = date_of_birth

    @property
    def home_address(self):
        return self._home_address

    @home_address.setter
    def home_address(self, home_address):
        self._home_address = home_address

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def middle_names(self):
        return self._middle_names

    @middle_names.setter
    def middle_names(self, middle_names):
        self._middle_names = middle_names

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        allowed_values = ["N", "M", "F", "I", "None"]
        if gender:
            if gender not in allowed_values:
                raise ValueError(
                    "Invalid value for `gender` ({0}), must be one of {1}".format(
                        gender, allowed_values
                    )
                )
        self._gender = gender

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        self._mobile = mobile

    @property
    def twitter_user_name(self):
        return self._twitter_user_name

    @twitter_user_name.setter
    def twitter_user_name(self, twitter_user_name):
        self._twitter_user_name = twitter_user_name

    @property
    def is_authorised_to_approve_leave(self):
        return self._is_authorised_to_approve_leave

    @is_authorised_to_approve_leave.setter
    def is_authorised_to_approve_leave(self, is_authorised_to_approve_leave):
        self._is_authorised_to_approve_leave = is_authorised_to_approve_leave

    @property
    def is_authorised_to_approve_timesheets(self):
        return self._is_authorised_to_approve_timesheets

    @is_authorised_to_approve_timesheets.setter
    def is_authorised_to_approve_timesheets(self, is_authorised_to_approve_timesheets):
        self._is_authorised_to_approve_timesheets = is_authorised_to_approve_timesheets

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        self._job_title = job_title

    @property
    def classification(self):
        return self._classification

    @classification.setter
    def classification(self, classification):
        self._classification = classification

    @property
    def ordinary_earnings_rate_id(self):
        return self._ordinary_earnings_rate_id

    @ordinary_earnings_rate_id.setter
    def ordinary_earnings_rate_id(self, ordinary_earnings_rate_id):
        self._ordinary_earnings_rate_id = ordinary_earnings_rate_id

    @property
    def payroll_calendar_id(self):
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        self._payroll_calendar_id = payroll_calendar_id

    @property
    def employee_group_name(self):
        return self._employee_group_name

    @employee_group_name.setter
    def employee_group_name(self, employee_group_name):
        self._employee_group_name = employee_group_name

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def termination_date(self):
        return self._termination_date

    @termination_date.setter
    def termination_date(self, termination_date):
        self._termination_date = termination_date

    @property
    def termination_reason(self):
        return self._termination_reason

    @termination_reason.setter
    def termination_reason(self, termination_reason):
        allowed_values = ["V", "I", "D", "R", "F", "C", "T", "None"]
        if termination_reason:
            if termination_reason not in allowed_values:
                raise ValueError(
                    "Invalid value for `termination_reason` ({0}), must be one of {1}".format(
                        termination_reason, allowed_values
                    )
                )
        self._termination_reason = termination_reason

    @property
    def bank_accounts(self):
        return self._bank_accounts

    @bank_accounts.setter
    def bank_accounts(self, bank_accounts):
        self._bank_accounts = bank_accounts

    @property
    def pay_template(self):
        return self._pay_template

    @pay_template.setter
    def pay_template(self, pay_template):
        self._pay_template = pay_template

    @property
    def opening_balances(self):
        return self._opening_balances

    @opening_balances.setter
    def opening_balances(self, opening_balances):
        self._opening_balances = opening_balances

    @property
    def tax_declaration(self):
        return self._tax_declaration

    @tax_declaration.setter
    def tax_declaration(self, tax_declaration):
        self._tax_declaration = tax_declaration

    @property
    def income_type(self):
        return self._income_type

    @income_type.setter
    def income_type(self, income_type):
        self._income_type = income_type

    @property
    def employment_type(self):
        return self._employment_type

    @employment_type.setter
    def employment_type(self, employment_type):
        self._employment_type = employment_type

    @property
    def country_of_residence(self):
        return self._country_of_residence

    @country_of_residence.setter
    def country_of_residence(self, country_of_residence):
        self._country_of_residence = country_of_residence

    @property
    def is_stp2_qualified(self):
        return self._is_stp2_qualified

    @is_stp2_qualified.setter
    def is_stp2_qualified(self, is_stp2_qualified):
        self._is_stp2_qualified = is_stp2_qualified

    @property
    def leave_balances(self):
        return self._leave_balances

    @leave_balances.setter
    def leave_balances(self, leave_balances):
        self._leave_balances = leave_balances

    @property
    def leave_lines(self):
        return self._leave_lines

    @leave_lines.setter
    def leave_lines(self, leave_lines):
        self._leave_lines = leave_lines

    @property
    def super_memberships(self):
        return self._super_memberships

    @super_memberships.setter
    def super_memberships(self, super_memberships):
        self._super_memberships = super_memberships

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
