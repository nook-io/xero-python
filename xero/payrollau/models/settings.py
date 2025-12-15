from xero.models import BaseModel


class Settings(BaseModel):
    openapi_types = {
        "accounts": "list[Account]",
        "tracking_categories": "SettingsTrackingCategories",
        "days_in_payroll_year": "int",
        "employees_are_stp2": "bool",
    }
    attribute_map = {
        "accounts": "Accounts",
        "tracking_categories": "TrackingCategories",
        "days_in_payroll_year": "DaysInPayrollYear",
        "employees_are_stp2": "EmployeesAreSTP2",
    }

    def __init__(
        self,
        accounts=None,
        tracking_categories=None,
        days_in_payroll_year=None,
        employees_are_stp2=None,
    ):
        self._accounts = None
        self._tracking_categories = None
        self._days_in_payroll_year = None
        self._employees_are_stp2 = None
        self.discriminator = None
        if accounts is not None:
            self.accounts = accounts
        if tracking_categories is not None:
            self.tracking_categories = tracking_categories
        if days_in_payroll_year is not None:
            self.days_in_payroll_year = days_in_payroll_year
        if employees_are_stp2 is not None:
            self.employees_are_stp2 = employees_are_stp2

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts

    @property
    def tracking_categories(self):
        return self._tracking_categories

    @tracking_categories.setter
    def tracking_categories(self, tracking_categories):
        self._tracking_categories = tracking_categories

    @property
    def days_in_payroll_year(self):
        return self._days_in_payroll_year

    @days_in_payroll_year.setter
    def days_in_payroll_year(self, days_in_payroll_year):
        self._days_in_payroll_year = days_in_payroll_year

    @property
    def employees_are_stp2(self):
        return self._employees_are_stp2

    @employees_are_stp2.setter
    def employees_are_stp2(self, employees_are_stp2):
        self._employees_are_stp2 = employees_are_stp2
