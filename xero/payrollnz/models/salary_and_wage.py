from xero.models import BaseModel


class SalaryAndWage(BaseModel):
    openapi_types = {
        "salary_and_wages_id": "str",
        "earnings_rate_id": "str",
        "number_of_units_per_week": "float",
        "rate_per_unit": "float",
        "number_of_units_per_day": "float",
        "days_per_week": "float",
        "effective_from": "date",
        "annual_salary": "float",
        "status": "str",
        "payment_type": "str",
        "work_pattern_type": "str",
    }
    attribute_map = {
        "salary_and_wages_id": "salaryAndWagesID",
        "earnings_rate_id": "earningsRateID",
        "number_of_units_per_week": "numberOfUnitsPerWeek",
        "rate_per_unit": "ratePerUnit",
        "number_of_units_per_day": "numberOfUnitsPerDay",
        "days_per_week": "daysPerWeek",
        "effective_from": "effectiveFrom",
        "annual_salary": "annualSalary",
        "status": "status",
        "payment_type": "paymentType",
        "work_pattern_type": "workPatternType",
    }

    def __init__(
        self,
        salary_and_wages_id=None,
        earnings_rate_id=None,
        number_of_units_per_week=None,
        rate_per_unit=None,
        number_of_units_per_day=None,
        days_per_week=None,
        effective_from=None,
        annual_salary=None,
        status=None,
        payment_type=None,
        work_pattern_type=None,
    ):
        self._salary_and_wages_id = None
        self._earnings_rate_id = None
        self._number_of_units_per_week = None
        self._rate_per_unit = None
        self._number_of_units_per_day = None
        self._days_per_week = None
        self._effective_from = None
        self._annual_salary = None
        self._status = None
        self._payment_type = None
        self._work_pattern_type = None
        self.discriminator = None
        if salary_and_wages_id is not None:
            self.salary_and_wages_id = salary_and_wages_id
        self.earnings_rate_id = earnings_rate_id
        self.number_of_units_per_week = number_of_units_per_week
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        self.number_of_units_per_day = number_of_units_per_day
        if days_per_week is not None:
            self.days_per_week = days_per_week
        self.effective_from = effective_from
        self.annual_salary = annual_salary
        self.status = status
        self.payment_type = payment_type
        if work_pattern_type is not None:
            self.work_pattern_type = work_pattern_type

    @property
    def salary_and_wages_id(self):
        return self._salary_and_wages_id

    @salary_and_wages_id.setter
    def salary_and_wages_id(self, salary_and_wages_id):
        self._salary_and_wages_id = salary_and_wages_id

    @property
    def earnings_rate_id(self):
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        if earnings_rate_id is None:
            raise ValueError("Invalid value for `earnings_rate_id`, must not be `None`")
        self._earnings_rate_id = earnings_rate_id

    @property
    def number_of_units_per_week(self):
        return self._number_of_units_per_week

    @number_of_units_per_week.setter
    def number_of_units_per_week(self, number_of_units_per_week):
        if number_of_units_per_week is None:
            raise ValueError(
                "Invalid value for `number_of_units_per_week`, must not be `None`"
            )
        self._number_of_units_per_week = number_of_units_per_week

    @property
    def rate_per_unit(self):
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        self._rate_per_unit = rate_per_unit

    @property
    def number_of_units_per_day(self):
        return self._number_of_units_per_day

    @number_of_units_per_day.setter
    def number_of_units_per_day(self, number_of_units_per_day):
        if number_of_units_per_day is None:
            raise ValueError(
                "Invalid value for `number_of_units_per_day`, must not be `None`"
            )
        self._number_of_units_per_day = number_of_units_per_day

    @property
    def days_per_week(self):
        return self._days_per_week

    @days_per_week.setter
    def days_per_week(self, days_per_week):
        self._days_per_week = days_per_week

    @property
    def effective_from(self):
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        if effective_from is None:
            raise ValueError("Invalid value for `effective_from`, must not be `None`")
        self._effective_from = effective_from

    @property
    def annual_salary(self):
        return self._annual_salary

    @annual_salary.setter
    def annual_salary(self, annual_salary):
        if annual_salary is None:
            raise ValueError("Invalid value for `annual_salary`, must not be `None`")
        self._annual_salary = annual_salary

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        allowed_values = ["Active", "Pending", "History", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        if payment_type is None:
            raise ValueError("Invalid value for `payment_type`, must not be `None`")
        allowed_values = ["Salary", "Hourly", "None"]
        if payment_type:
            if payment_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `payment_type` ({0}), must be one of {1}".format(
                        payment_type, allowed_values
                    )
                )
        self._payment_type = payment_type

    @property
    def work_pattern_type(self):
        return self._work_pattern_type

    @work_pattern_type.setter
    def work_pattern_type(self, work_pattern_type):
        allowed_values = ["DaysAndHours", "RegularWeek", "None"]
        if work_pattern_type:
            if work_pattern_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `work_pattern_type` ({0}), must be one of {1}".format(
                        work_pattern_type, allowed_values
                    )
                )
        self._work_pattern_type = work_pattern_type
