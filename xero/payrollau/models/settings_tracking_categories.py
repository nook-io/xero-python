from xero.models import BaseModel


class SettingsTrackingCategories(BaseModel):
    openapi_types = {
        "employee_groups": "SettingsTrackingCategoriesEmployeeGroups",
        "timesheet_categories": "SettingsTrackingCategoriesTimesheetCategories",
    }
    attribute_map = {
        "employee_groups": "EmployeeGroups",
        "timesheet_categories": "TimesheetCategories",
    }

    def __init__(self, employee_groups=None, timesheet_categories=None):
        self._employee_groups = None
        self._timesheet_categories = None
        self.discriminator = None
        if employee_groups is not None:
            self.employee_groups = employee_groups
        if timesheet_categories is not None:
            self.timesheet_categories = timesheet_categories

    @property
    def employee_groups(self):
        return self._employee_groups

    @employee_groups.setter
    def employee_groups(self, employee_groups):
        self._employee_groups = employee_groups

    @property
    def timesheet_categories(self):
        return self._timesheet_categories

    @timesheet_categories.setter
    def timesheet_categories(self, timesheet_categories):
        self._timesheet_categories = timesheet_categories
