from xero.models import BaseModel


class LeaveApplication(BaseModel):
    openapi_types = {
        "leave_application_id": "str",
        "employee_id": "str",
        "leave_type_id": "str",
        "title": "str",
        "start_date": "date[ms-format]",
        "end_date": "date[ms-format]",
        "description": "str",
        "pay_out_type": "PayOutType",
        "leave_periods": "list[LeavePeriod]",
        "updated_date_utc": "datetime[ms-format]",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "leave_application_id": "LeaveApplicationID",
        "employee_id": "EmployeeID",
        "leave_type_id": "LeaveTypeID",
        "title": "Title",
        "start_date": "StartDate",
        "end_date": "EndDate",
        "description": "Description",
        "pay_out_type": "PayOutType",
        "leave_periods": "LeavePeriods",
        "updated_date_utc": "UpdatedDateUTC",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        leave_application_id=None,
        employee_id=None,
        leave_type_id=None,
        title=None,
        start_date=None,
        end_date=None,
        description=None,
        pay_out_type=None,
        leave_periods=None,
        updated_date_utc=None,
        validation_errors=None,
    ):
        self._leave_application_id = None
        self._employee_id = None
        self._leave_type_id = None
        self._title = None
        self._start_date = None
        self._end_date = None
        self._description = None
        self._pay_out_type = None
        self._leave_periods = None
        self._updated_date_utc = None
        self._validation_errors = None
        self.discriminator = None
        if leave_application_id is not None:
            self.leave_application_id = leave_application_id
        if employee_id is not None:
            self.employee_id = employee_id
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if title is not None:
            self.title = title
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if description is not None:
            self.description = description
        if pay_out_type is not None:
            self.pay_out_type = pay_out_type
        if leave_periods is not None:
            self.leave_periods = leave_periods
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def leave_application_id(self):
        return self._leave_application_id

    @leave_application_id.setter
    def leave_application_id(self, leave_application_id):
        self._leave_application_id = leave_application_id

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def leave_type_id(self):
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        self._leave_type_id = leave_type_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

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
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def pay_out_type(self):
        return self._pay_out_type

    @pay_out_type.setter
    def pay_out_type(self, pay_out_type):
        self._pay_out_type = pay_out_type

    @property
    def leave_periods(self):
        return self._leave_periods

    @leave_periods.setter
    def leave_periods(self, leave_periods):
        self._leave_periods = leave_periods

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
