from xero.models import BaseModel


class LeaveAccrualLine(BaseModel):
    openapi_types = {"leave_type_id": "str", "number_of_units": "float"}
    attribute_map = {"leave_type_id": "leaveTypeID", "number_of_units": "numberOfUnits"}

    def __init__(self, leave_type_id=None, number_of_units=None):
        self._leave_type_id = None
        self._number_of_units = None
        self.discriminator = None
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if number_of_units is not None:
            self.number_of_units = number_of_units

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
