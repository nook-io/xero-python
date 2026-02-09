from xero.models import BaseModel


class Employment(BaseModel):
    openapi_types = {
        "payroll_calendar_id": "str",
        "start_date": "date",
        "employee_number": "str",
        "ni_category": "str",
    }
    attribute_map = {
        "payroll_calendar_id": "payrollCalendarID",
        "start_date": "startDate",
        "employee_number": "employeeNumber",
        "ni_category": "niCategory",
    }

    def __init__(
        self,
        payroll_calendar_id=None,
        start_date=None,
        employee_number=None,
        ni_category=None,
    ):
        self._payroll_calendar_id = None
        self._start_date = None
        self._employee_number = None
        self._ni_category = None
        self.discriminator = None
        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        if start_date is not None:
            self.start_date = start_date
        if employee_number is not None:
            self.employee_number = employee_number
        if ni_category is not None:
            self.ni_category = ni_category

    @property
    def payroll_calendar_id(self):
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        self._payroll_calendar_id = payroll_calendar_id

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def employee_number(self):
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        self._employee_number = employee_number

    @property
    def ni_category(self):
        return self._ni_category

    @ni_category.setter
    def ni_category(self, ni_category):
        allowed_values = [
            "A",
            "B",
            "C",
            "F",
            "H",
            "I",
            "J",
            "L",
            "M",
            "S",
            "V",
            "X",
            "Z",
            "None",
        ]
        if ni_category:
            if ni_category not in allowed_values:
                raise ValueError(
                    "Invalid value for `ni_category` ({0}), must be one of {1}".format(
                        ni_category, allowed_values
                    )
                )
        self._ni_category = ni_category
