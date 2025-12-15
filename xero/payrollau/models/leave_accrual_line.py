from xero.models import BaseModel


class LeaveAccrualLine(BaseModel):
    openapi_types = {
        "leave_type_id": "str",
        "number_of_units": "float",
        "auto_calculate": "bool",
    }
    attribute_map = {
        "leave_type_id": "LeaveTypeID",
        "number_of_units": "NumberOfUnits",
        "auto_calculate": "AutoCalculate",
    }

    def __init__(self, leave_type_id=None, number_of_units=None, auto_calculate=None):
        self._leave_type_id = None
        self._number_of_units = None
        self._auto_calculate = None
        self.discriminator = None
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if auto_calculate is not None:
            self.auto_calculate = auto_calculate

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
    def auto_calculate(self):
        return self._auto_calculate

    @auto_calculate.setter
    def auto_calculate(self, auto_calculate):
        self._auto_calculate = auto_calculate
