from xero.models import BaseModel


class Payslips(BaseModel):
    openapi_types = {"payslips": "list[Payslip]"}
    attribute_map = {"payslips": "Payslips"}

    def __init__(self, payslips=None):
        self._payslips = None
        self.discriminator = None
        if payslips is not None:
            self.payslips = payslips

    @property
    def payslips(self):
        return self._payslips

    @payslips.setter
    def payslips(self, payslips):
        self._payslips = payslips
