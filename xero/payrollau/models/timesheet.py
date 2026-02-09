from xero.models import BaseModel


class Timesheet(BaseModel):
    openapi_types = {
        "employee_id": "str",
        "start_date": "date[ms-format]",
        "end_date": "date[ms-format]",
        "status": "TimesheetStatus",
        "hours": "float",
        "timesheet_id": "str",
        "timesheet_lines": "list[TimesheetLine]",
        "updated_date_utc": "datetime[ms-format]",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "employee_id": "EmployeeID",
        "start_date": "StartDate",
        "end_date": "EndDate",
        "status": "Status",
        "hours": "Hours",
        "timesheet_id": "TimesheetID",
        "timesheet_lines": "TimesheetLines",
        "updated_date_utc": "UpdatedDateUTC",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        employee_id=None,
        start_date=None,
        end_date=None,
        status=None,
        hours=None,
        timesheet_id=None,
        timesheet_lines=None,
        updated_date_utc=None,
        validation_errors=None,
    ):
        self._employee_id = None
        self._start_date = None
        self._end_date = None
        self._status = None
        self._hours = None
        self._timesheet_id = None
        self._timesheet_lines = None
        self._updated_date_utc = None
        self._validation_errors = None
        self.discriminator = None
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        if status is not None:
            self.status = status
        if hours is not None:
            self.hours = hours
        if timesheet_id is not None:
            self.timesheet_id = timesheet_id
        if timesheet_lines is not None:
            self.timesheet_lines = timesheet_lines
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if validation_errors is not None:
            self.validation_errors = validation_errors

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
        self._status = status

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        self._hours = hours

    @property
    def timesheet_id(self):
        return self._timesheet_id

    @timesheet_id.setter
    def timesheet_id(self, timesheet_id):
        self._timesheet_id = timesheet_id

    @property
    def timesheet_lines(self):
        return self._timesheet_lines

    @timesheet_lines.setter
    def timesheet_lines(self, timesheet_lines):
        self._timesheet_lines = timesheet_lines

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
