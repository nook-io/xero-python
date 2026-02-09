from xero.models import BaseModel


class Employee(BaseModel):
    openapi_types = {
        "employee_id": "str",
        "title": "str",
        "first_name": "str",
        "last_name": "str",
        "date_of_birth": "date",
        "address": "Address",
        "email": "str",
        "gender": "str",
        "phone_number": "str",
        "start_date": "date",
        "end_date": "date",
        "payroll_calendar_id": "str",
        "updated_date_utc": "datetime",
        "created_date_utc": "datetime",
        "national_insurance_number": "str",
        "is_off_payroll_worker": "bool",
    }
    attribute_map = {
        "employee_id": "employeeID",
        "title": "title",
        "first_name": "firstName",
        "last_name": "lastName",
        "date_of_birth": "dateOfBirth",
        "address": "address",
        "email": "email",
        "gender": "gender",
        "phone_number": "phoneNumber",
        "start_date": "startDate",
        "end_date": "endDate",
        "payroll_calendar_id": "payrollCalendarID",
        "updated_date_utc": "updatedDateUTC",
        "created_date_utc": "createdDateUTC",
        "national_insurance_number": "nationalInsuranceNumber",
        "is_off_payroll_worker": "isOffPayrollWorker",
    }

    def __init__(
        self,
        employee_id=None,
        title=None,
        first_name=None,
        last_name=None,
        date_of_birth=None,
        address=None,
        email=None,
        gender=None,
        phone_number=None,
        start_date=None,
        end_date=None,
        payroll_calendar_id=None,
        updated_date_utc=None,
        created_date_utc=None,
        national_insurance_number=None,
        is_off_payroll_worker=None,
    ):
        self._employee_id = None
        self._title = None
        self._first_name = None
        self._last_name = None
        self._date_of_birth = None
        self._address = None
        self._email = None
        self._gender = None
        self._phone_number = None
        self._start_date = None
        self._end_date = None
        self._payroll_calendar_id = None
        self._updated_date_utc = None
        self._created_date_utc = None
        self._national_insurance_number = None
        self._is_off_payroll_worker = None
        self.discriminator = None
        if employee_id is not None:
            self.employee_id = employee_id
        if title is not None:
            self.title = title
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if address is not None:
            self.address = address
        if email is not None:
            self.email = email
        if gender is not None:
            self.gender = gender
        if phone_number is not None:
            self.phone_number = phone_number
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc
        if national_insurance_number is not None:
            self.national_insurance_number = national_insurance_number
        if is_off_payroll_worker is not None:
            self.is_off_payroll_worker = is_off_payroll_worker

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

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
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

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
        allowed_values = ["M", "F", "None"]
        if gender:
            if gender not in allowed_values:
                raise ValueError(
                    "Invalid value for `gender` ({0}), must be one of {1}".format(
                        gender, allowed_values
                    )
                )
        self._gender = gender

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @property
    def payroll_calendar_id(self):
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        self._payroll_calendar_id = payroll_calendar_id

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def created_date_utc(self):
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        self._created_date_utc = created_date_utc

    @property
    def national_insurance_number(self):
        return self._national_insurance_number

    @national_insurance_number.setter
    def national_insurance_number(self, national_insurance_number):
        self._national_insurance_number = national_insurance_number

    @property
    def is_off_payroll_worker(self):
        return self._is_off_payroll_worker

    @is_off_payroll_worker.setter
    def is_off_payroll_worker(self, is_off_payroll_worker):
        self._is_off_payroll_worker = is_off_payroll_worker
