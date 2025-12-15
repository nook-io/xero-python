from xero.models import BaseModel


class LeaveBalance(BaseModel):
    openapi_types = {
        "leave_name": "str",
        "leave_type_id": "str",
        "number_of_units": "float",
        "type_of_units": "str",
    }
    attribute_map = {
        "leave_name": "LeaveName",
        "leave_type_id": "LeaveTypeID",
        "number_of_units": "NumberOfUnits",
        "type_of_units": "TypeOfUnits",
    }

    def __init__(
        self,
        leave_name=None,
        leave_type_id=None,
        number_of_units=None,
        type_of_units=None,
    ):
        self._leave_name = None
        self._leave_type_id = None
        self._number_of_units = None
        self._type_of_units = None
        self.discriminator = None
        if leave_name is not None:
            self.leave_name = leave_name
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if type_of_units is not None:
            self.type_of_units = type_of_units

    @property
    def leave_name(self):
        return self._leave_name

    @leave_name.setter
    def leave_name(self, leave_name):
        self._leave_name = leave_name

    @property
    def leave_type_id(self):
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        self._leave_type_id = leave_type_id

    @property
    def number_of_units(self):
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        self._number_of_units = number_of_units

    @property
    def type_of_units(self):
        return self._type_of_units

    @type_of_units.setter
    def type_of_units(self, type_of_units):
        self._type_of_units = type_of_units
