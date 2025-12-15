from xero.models import BaseModel


class Timesheet(BaseModel):
    openapi_types = {
        "timesheet_id": "str",
        "payroll_calendar_id": "str",
        "employee_id": "str",
        "start_date": "date",
        "end_date": "date",
        "status": "str",
        "total_hours": "float",
        "updated_date_utc": "datetime",
        "timesheet_lines": "list[TimesheetLine]",
    }
    attribute_map = {
        "timesheet_id": "timesheetID",
        "payroll_calendar_id": "payrollCalendarID",
        "employee_id": "employeeID",
        "start_date": "startDate",
        "end_date": "endDate",
        "status": "status",
        "total_hours": "totalHours",
        "updated_date_utc": "updatedDateUTC",
        "timesheet_lines": "timesheetLines",
    }

    def __init__(
        self,
        timesheet_id=None,
        payroll_calendar_id=None,
        employee_id=None,
        start_date=None,
        end_date=None,
        status=None,
        total_hours=None,
        updated_date_utc=None,
        timesheet_lines=None,
    ):
        self._timesheet_id = None
        self._payroll_calendar_id = None
        self._employee_id = None
        self._start_date = None
        self._end_date = None
        self._status = None
        self._total_hours = None
        self._updated_date_utc = None
        self._timesheet_lines = None
        self.discriminator = None
        if timesheet_id is not None:
            self.timesheet_id = timesheet_id
        self.payroll_calendar_id = payroll_calendar_id
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        if status is not None:
            self.status = status
        if total_hours is not None:
            self.total_hours = total_hours
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if timesheet_lines is not None:
            self.timesheet_lines = timesheet_lines

    @property
    def timesheet_id(self):
        return self._timesheet_id

    @timesheet_id.setter
    def timesheet_id(self, timesheet_id):
        self._timesheet_id = timesheet_id

    @property
    def payroll_calendar_id(self):
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        if payroll_calendar_id is None:
            raise ValueError(
                "Invalid value for `payroll_calendar_id`, must not be `None`"
            )
        self._payroll_calendar_id = payroll_calendar_id

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        if employee_id is None:
            raise ValueError("Invalid value for `employee_id`, must not be `None`")
        self._employee_id = employee_id

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")
        self._end_date = end_date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = [
            "Draft",
            "Approved",
            "Completed",
            "Requested",
            "None",
        ]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def total_hours(self):
        return self._total_hours

    @total_hours.setter
    def total_hours(self, total_hours):
        self._total_hours = total_hours

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def timesheet_lines(self):
        return self._timesheet_lines

    @timesheet_lines.setter
    def timesheet_lines(self, timesheet_lines):
        self._timesheet_lines = timesheet_lines
