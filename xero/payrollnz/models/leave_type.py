from xero.models import BaseModel


class LeaveType(BaseModel):
    openapi_types = {
        "leave_type_id": "str",
        "name": "str",
        "is_paid_leave": "bool",
        "show_on_payslip": "bool",
        "updated_date_utc": "datetime",
        "is_active": "bool",
    }
    attribute_map = {
        "leave_type_id": "leaveTypeID",
        "name": "name",
        "is_paid_leave": "isPaidLeave",
        "show_on_payslip": "showOnPayslip",
        "updated_date_utc": "updatedDateUTC",
        "is_active": "isActive",
    }

    def __init__(
        self,
        leave_type_id=None,
        name=None,
        is_paid_leave=None,
        show_on_payslip=None,
        updated_date_utc=None,
        is_active=None,
    ):
        self._leave_type_id = None
        self._name = None
        self._is_paid_leave = None
        self._show_on_payslip = None
        self._updated_date_utc = None
        self._is_active = None
        self.discriminator = None
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        self.name = name
        self.is_paid_leave = is_paid_leave
        self.show_on_payslip = show_on_payslip
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if is_active is not None:
            self.is_active = is_active

    @property
    def leave_type_id(self):
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        self._leave_type_id = leave_type_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def is_paid_leave(self):
        return self._is_paid_leave

    @is_paid_leave.setter
    def is_paid_leave(self, is_paid_leave):
        if is_paid_leave is None:
            raise ValueError("Invalid value for `is_paid_leave`, must not be `None`")
        self._is_paid_leave = is_paid_leave

    @property
    def show_on_payslip(self):
        return self._show_on_payslip

    @show_on_payslip.setter
    def show_on_payslip(self, show_on_payslip):
        if show_on_payslip is None:
            raise ValueError("Invalid value for `show_on_payslip`, must not be `None`")
        self._show_on_payslip = show_on_payslip

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        self._is_active = is_active
