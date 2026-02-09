from xero.models import BaseModel


class PayslipObject(BaseModel):
    openapi_types = {"payslip": "Payslip"}
    attribute_map = {"payslip": "Payslip"}

    def __init__(self, payslip=None):
        self._payslip = None
        self.discriminator = None
        if payslip is not None:
            self.payslip = payslip

    @property
    def payslip(self):
        return self._payslip

    @payslip.setter
    def payslip(self, payslip):
        self._payslip = payslip
