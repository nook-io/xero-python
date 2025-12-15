from xero.models import BaseModel


class EmployeeStatutoryLeaveBalance(BaseModel):
    openapi_types = {"leave_type": "str", "balance_remaining": "float", "units": "str"}
    attribute_map = {
        "leave_type": "leaveType",
        "balance_remaining": "balanceRemaining",
        "units": "units",
    }

    def __init__(self, leave_type=None, balance_remaining=None, units=None):
        self._leave_type = None
        self._balance_remaining = None
        self._units = None
        self.discriminator = None
        if leave_type is not None:
            self.leave_type = leave_type
        if balance_remaining is not None:
            self.balance_remaining = balance_remaining
        if units is not None:
            self.units = units

    @property
    def leave_type(self):
        return self._leave_type

    @leave_type.setter
    def leave_type(self, leave_type):
        allowed_values = [
            "Sick",
            "Adoption",
            "Maternity",
            "Paternity",
            "Sharedparental",
            "None",
        ]
        if leave_type:
            if leave_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `leave_type` ({0}), must be one of {1}".format(
                        leave_type, allowed_values
                    )
                )
        self._leave_type = leave_type

    @property
    def balance_remaining(self):
        return self._balance_remaining

    @balance_remaining.setter
    def balance_remaining(self, balance_remaining):
        self._balance_remaining = balance_remaining

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, units):
        allowed_values = ["Hours", "None"]
        if units:
            if units not in allowed_values:
                raise ValueError(
                    "Invalid value for `units` ({0}), must be one of {1}".format(
                        units, allowed_values
                    )
                )
        self._units = units
