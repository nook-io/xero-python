from xero.models import BaseModel


class EmployeePayTemplate(BaseModel):
    openapi_types = {
        "employee_id": "str",
        "earning_templates": "list[EarningsTemplate]",
    }
    attribute_map = {
        "employee_id": "employeeID",
        "earning_templates": "earningTemplates",
    }

    def __init__(self, employee_id=None, earning_templates=None):
        self._employee_id = None
        self._earning_templates = None
        self.discriminator = None
        if employee_id is not None:
            self.employee_id = employee_id
        if earning_templates is not None:
            self.earning_templates = earning_templates

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def earning_templates(self):
        return self._earning_templates

    @earning_templates.setter
    def earning_templates(self, earning_templates):
        self._earning_templates = earning_templates
