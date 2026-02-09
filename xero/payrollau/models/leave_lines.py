from xero.models import BaseModel


class LeaveLines(BaseModel):
    openapi_types = {"employee": "list[LeaveLine]"}
    attribute_map = {"employee": "Employee"}

    def __init__(self, employee=None):
        self._employee = None
        self.discriminator = None
        if employee is not None:
            self.employee = employee

    @property
    def employee(self):
        return self._employee

    @employee.setter
    def employee(self, employee):
        self._employee = employee
