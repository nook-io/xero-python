from xero.models import BaseModel


class EmployeeLeaveBalance(BaseModel):
    openapi_types = {
        "name": "str",
        "leave_type_id": "str",
        "balance": "float",
        "type_of_units": "str",
    }
    attribute_map = {
        "name": "name",
        "leave_type_id": "leaveTypeID",
        "balance": "balance",
        "type_of_units": "typeOfUnits",
    }

    def __init__(self, name=None, leave_type_id=None, balance=None, type_of_units=None):
        self._name = None
        self._leave_type_id = None
        self._balance = None
        self._type_of_units = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if balance is not None:
            self.balance = balance
        if type_of_units is not None:
            self.type_of_units = type_of_units

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def leave_type_id(self):
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        self._leave_type_id = leave_type_id

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def type_of_units(self):
        return self._type_of_units

    @type_of_units.setter
    def type_of_units(self, type_of_units):
        self._type_of_units = type_of_units
