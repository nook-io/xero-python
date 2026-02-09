from xero.models import BaseModel


class LeaveType(BaseModel):
    openapi_types = {
        "name": "str",
        "type_of_units": "str",
        "leave_type_id": "str",
        "normal_entitlement": "float",
        "leave_loading_rate": "float",
        "updated_date_utc": "datetime[ms-format]",
        "is_paid_leave": "bool",
        "show_on_payslip": "bool",
        "current_record": "bool",
        "leave_category_code": "LeaveCategoryCode",
        "sgc_exempt": "bool",
    }
    attribute_map = {
        "name": "Name",
        "type_of_units": "TypeOfUnits",
        "leave_type_id": "LeaveTypeID",
        "normal_entitlement": "NormalEntitlement",
        "leave_loading_rate": "LeaveLoadingRate",
        "updated_date_utc": "UpdatedDateUTC",
        "is_paid_leave": "IsPaidLeave",
        "show_on_payslip": "ShowOnPayslip",
        "current_record": "CurrentRecord",
        "leave_category_code": "LeaveCategoryCode",
        "sgc_exempt": "SGCExempt",
    }

    def __init__(
        self,
        name=None,
        type_of_units=None,
        leave_type_id=None,
        normal_entitlement=None,
        leave_loading_rate=None,
        updated_date_utc=None,
        is_paid_leave=None,
        show_on_payslip=None,
        current_record=None,
        leave_category_code=None,
        sgc_exempt=None,
    ):
        self._name = None
        self._type_of_units = None
        self._leave_type_id = None
        self._normal_entitlement = None
        self._leave_loading_rate = None
        self._updated_date_utc = None
        self._is_paid_leave = None
        self._show_on_payslip = None
        self._current_record = None
        self._leave_category_code = None
        self._sgc_exempt = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if type_of_units is not None:
            self.type_of_units = type_of_units
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if normal_entitlement is not None:
            self.normal_entitlement = normal_entitlement
        if leave_loading_rate is not None:
            self.leave_loading_rate = leave_loading_rate
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if is_paid_leave is not None:
            self.is_paid_leave = is_paid_leave
        if show_on_payslip is not None:
            self.show_on_payslip = show_on_payslip
        if current_record is not None:
            self.current_record = current_record
        if leave_category_code is not None:
            self.leave_category_code = leave_category_code
        if sgc_exempt is not None:
            self.sgc_exempt = sgc_exempt

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 100:
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `100`"
            )
        self._name = name

    @property
    def type_of_units(self):
        return self._type_of_units

    @type_of_units.setter
    def type_of_units(self, type_of_units):
        self._type_of_units = type_of_units

    @property
    def leave_type_id(self):
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        self._leave_type_id = leave_type_id

    @property
    def normal_entitlement(self):
        return self._normal_entitlement

    @normal_entitlement.setter
    def normal_entitlement(self, normal_entitlement):
        self._normal_entitlement = normal_entitlement

    @property
    def leave_loading_rate(self):
        return self._leave_loading_rate

    @leave_loading_rate.setter
    def leave_loading_rate(self, leave_loading_rate):
        self._leave_loading_rate = leave_loading_rate

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def is_paid_leave(self):
        return self._is_paid_leave

    @is_paid_leave.setter
    def is_paid_leave(self, is_paid_leave):
        self._is_paid_leave = is_paid_leave

    @property
    def show_on_payslip(self):
        return self._show_on_payslip

    @show_on_payslip.setter
    def show_on_payslip(self, show_on_payslip):
        self._show_on_payslip = show_on_payslip

    @property
    def current_record(self):
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        self._current_record = current_record

    @property
    def leave_category_code(self):
        return self._leave_category_code

    @leave_category_code.setter
    def leave_category_code(self, leave_category_code):
        self._leave_category_code = leave_category_code

    @property
    def sgc_exempt(self):
        return self._sgc_exempt

    @sgc_exempt.setter
    def sgc_exempt(self, sgc_exempt):
        self._sgc_exempt = sgc_exempt
