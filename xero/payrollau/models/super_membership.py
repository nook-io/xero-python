from xero.models import BaseModel


class SuperMembership(BaseModel):
    openapi_types = {
        "super_membership_id": "str",
        "super_fund_id": "str",
        "employee_number": "str",
    }
    attribute_map = {
        "super_membership_id": "SuperMembershipID",
        "super_fund_id": "SuperFundID",
        "employee_number": "EmployeeNumber",
    }

    def __init__(
        self, super_membership_id=None, super_fund_id=None, employee_number=None
    ):
        self._super_membership_id = None
        self._super_fund_id = None
        self._employee_number = None
        self.discriminator = None
        if super_membership_id is not None:
            self.super_membership_id = super_membership_id
        self.super_fund_id = super_fund_id
        self.employee_number = employee_number

    @property
    def super_membership_id(self):
        return self._super_membership_id

    @super_membership_id.setter
    def super_membership_id(self, super_membership_id):
        self._super_membership_id = super_membership_id

    @property
    def super_fund_id(self):
        return self._super_fund_id

    @super_fund_id.setter
    def super_fund_id(self, super_fund_id):
        if super_fund_id is None:
            raise ValueError("Invalid value for `super_fund_id`, must not be `None`")
        self._super_fund_id = super_fund_id

    @property
    def employee_number(self):
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        if employee_number is None:
            raise ValueError("Invalid value for `employee_number`, must not be `None`")
        self._employee_number = employee_number
