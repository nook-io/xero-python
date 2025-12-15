from xero.models import BaseModel


class Employees(BaseModel):
    openapi_types = {"employees": "list[Employee]"}
    attribute_map = {"employees": "Employees"}

    def __init__(self, employees=None):
        self._employees = None
        self.discriminator = None
        if employees is not None:
            self.employees = employees

    @property
    def employees(self):
        return self._employees

    @employees.setter
    def employees(self, employees):
        self._employees = employees
