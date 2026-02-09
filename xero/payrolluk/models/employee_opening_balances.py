from xero.models import BaseModel


class EmployeeOpeningBalances(BaseModel):
    openapi_types = {
        "statutory_adoption_pay": "float",
        "statutory_maternity_pay": "float",
        "statutory_paternity_pay": "float",
        "statutory_shared_parental_pay": "float",
        "statutory_sick_pay": "float",
        "prior_employee_number": "float",
    }
    attribute_map = {
        "statutory_adoption_pay": "statutoryAdoptionPay",
        "statutory_maternity_pay": "statutoryMaternityPay",
        "statutory_paternity_pay": "statutoryPaternityPay",
        "statutory_shared_parental_pay": "statutorySharedParentalPay",
        "statutory_sick_pay": "statutorySickPay",
        "prior_employee_number": "priorEmployeeNumber",
    }

    def __init__(
        self,
        statutory_adoption_pay=None,
        statutory_maternity_pay=None,
        statutory_paternity_pay=None,
        statutory_shared_parental_pay=None,
        statutory_sick_pay=None,
        prior_employee_number=None,
    ):
        self._statutory_adoption_pay = None
        self._statutory_maternity_pay = None
        self._statutory_paternity_pay = None
        self._statutory_shared_parental_pay = None
        self._statutory_sick_pay = None
        self._prior_employee_number = None
        self.discriminator = None
        if statutory_adoption_pay is not None:
            self.statutory_adoption_pay = statutory_adoption_pay
        if statutory_maternity_pay is not None:
            self.statutory_maternity_pay = statutory_maternity_pay
        if statutory_paternity_pay is not None:
            self.statutory_paternity_pay = statutory_paternity_pay
        if statutory_shared_parental_pay is not None:
            self.statutory_shared_parental_pay = statutory_shared_parental_pay
        if statutory_sick_pay is not None:
            self.statutory_sick_pay = statutory_sick_pay
        if prior_employee_number is not None:
            self.prior_employee_number = prior_employee_number

    @property
    def statutory_adoption_pay(self):
        return self._statutory_adoption_pay

    @statutory_adoption_pay.setter
    def statutory_adoption_pay(self, statutory_adoption_pay):
        self._statutory_adoption_pay = statutory_adoption_pay

    @property
    def statutory_maternity_pay(self):
        return self._statutory_maternity_pay

    @statutory_maternity_pay.setter
    def statutory_maternity_pay(self, statutory_maternity_pay):
        self._statutory_maternity_pay = statutory_maternity_pay

    @property
    def statutory_paternity_pay(self):
        return self._statutory_paternity_pay

    @statutory_paternity_pay.setter
    def statutory_paternity_pay(self, statutory_paternity_pay):
        self._statutory_paternity_pay = statutory_paternity_pay

    @property
    def statutory_shared_parental_pay(self):
        return self._statutory_shared_parental_pay

    @statutory_shared_parental_pay.setter
    def statutory_shared_parental_pay(self, statutory_shared_parental_pay):
        self._statutory_shared_parental_pay = statutory_shared_parental_pay

    @property
    def statutory_sick_pay(self):
        return self._statutory_sick_pay

    @statutory_sick_pay.setter
    def statutory_sick_pay(self, statutory_sick_pay):
        self._statutory_sick_pay = statutory_sick_pay

    @property
    def prior_employee_number(self):
        return self._prior_employee_number

    @prior_employee_number.setter
    def prior_employee_number(self, prior_employee_number):
        self._prior_employee_number = prior_employee_number
