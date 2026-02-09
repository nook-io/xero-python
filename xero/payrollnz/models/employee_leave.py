from xero.models import BaseModel


class EmployeeLeave(BaseModel):
    openapi_types = {
        "leave_id": "str",
        "leave_type_id": "str",
        "description": "str",
        "start_date": "date",
        "end_date": "date",
        "periods": "list[LeavePeriod]",
        "updated_date_utc": "datetime",
    }
    attribute_map = {
        "leave_id": "leaveID",
        "leave_type_id": "leaveTypeID",
        "description": "description",
        "start_date": "startDate",
        "end_date": "endDate",
        "periods": "periods",
        "updated_date_utc": "updatedDateUTC",
    }

    def __init__(
        self,
        leave_id=None,
        leave_type_id=None,
        description=None,
        start_date=None,
        end_date=None,
        periods=None,
        updated_date_utc=None,
    ):
        self._leave_id = None
        self._leave_type_id = None
        self._description = None
        self._start_date = None
        self._end_date = None
        self._periods = None
        self._updated_date_utc = None
        self.discriminator = None
        if leave_id is not None:
            self.leave_id = leave_id
        self.leave_type_id = leave_type_id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        if periods is not None:
            self.periods = periods
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def leave_id(self):
        return self._leave_id

    @leave_id.setter
    def leave_id(self, leave_id):
        self._leave_id = leave_id

    @property
    def leave_type_id(self):
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        if leave_type_id is None:
            raise ValueError("Invalid value for `leave_type_id`, must not be `None`")
        self._leave_type_id = leave_type_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")
        self._description = description

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
    def periods(self):
        return self._periods

    @periods.setter
    def periods(self, periods):
        self._periods = periods

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc
