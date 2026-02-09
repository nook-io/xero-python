from xero.models import BaseModel


class EmployeeStatutoryLeaveSummary(BaseModel):
    openapi_types = {
        "statutory_leave_id": "str",
        "employee_id": "str",
        "type": "str",
        "start_date": "date",
        "end_date": "date",
        "is_entitled": "bool",
        "status": "str",
    }
    attribute_map = {
        "statutory_leave_id": "statutoryLeaveID",
        "employee_id": "employeeID",
        "type": "type",
        "start_date": "startDate",
        "end_date": "endDate",
        "is_entitled": "isEntitled",
        "status": "status",
    }

    def __init__(
        self,
        statutory_leave_id=None,
        employee_id=None,
        type=None,
        start_date=None,
        end_date=None,
        is_entitled=None,
        status=None,
    ):
        self._statutory_leave_id = None
        self._employee_id = None
        self._type = None
        self._start_date = None
        self._end_date = None
        self._is_entitled = None
        self._status = None
        self.discriminator = None
        if statutory_leave_id is not None:
            self.statutory_leave_id = statutory_leave_id
        if employee_id is not None:
            self.employee_id = employee_id
        if type is not None:
            self.type = type
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if is_entitled is not None:
            self.is_entitled = is_entitled
        if status is not None:
            self.status = status

    @property
    def statutory_leave_id(self):
        return self._statutory_leave_id

    @statutory_leave_id.setter
    def statutory_leave_id(self, statutory_leave_id):
        self._statutory_leave_id = statutory_leave_id

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_values = [
            "Sick",
            "Adoption",
            "Maternity",
            "Paternity",
            "Sharedparental",
            "None",
        ]
        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(
                        type, allowed_values
                    )
                )
        self._type = type

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
    def is_entitled(self):
        return self._is_entitled

    @is_entitled.setter
    def is_entitled(self, is_entitled):
        self._is_entitled = is_entitled

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["Pending", "In-Progress", "Completed", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status
