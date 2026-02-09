from xero.models import BaseModel


class TrackingCategory(BaseModel):
    openapi_types = {
        "employee_groups_tracking_category_id": "str",
        "timesheet_tracking_category_id": "str",
    }
    attribute_map = {
        "employee_groups_tracking_category_id": "employeeGroupsTrackingCategoryID",
        "timesheet_tracking_category_id": "timesheetTrackingCategoryID",
    }

    def __init__(
        self,
        employee_groups_tracking_category_id=None,
        timesheet_tracking_category_id=None,
    ):
        self._employee_groups_tracking_category_id = None
        self._timesheet_tracking_category_id = None
        self.discriminator = None
        if employee_groups_tracking_category_id is not None:
            self.employee_groups_tracking_category_id = (
                employee_groups_tracking_category_id
            )
        if timesheet_tracking_category_id is not None:
            self.timesheet_tracking_category_id = timesheet_tracking_category_id

    @property
    def employee_groups_tracking_category_id(self):
        return self._employee_groups_tracking_category_id

    @employee_groups_tracking_category_id.setter
    def employee_groups_tracking_category_id(
        self, employee_groups_tracking_category_id
    ):
        self._employee_groups_tracking_category_id = (
            employee_groups_tracking_category_id
        )

    @property
    def timesheet_tracking_category_id(self):
        return self._timesheet_tracking_category_id

    @timesheet_tracking_category_id.setter
    def timesheet_tracking_category_id(self, timesheet_tracking_category_id):
        self._timesheet_tracking_category_id = timesheet_tracking_category_id
