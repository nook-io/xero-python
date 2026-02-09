from xero.models import BaseModel


class PaymentTerm(BaseModel):
    openapi_types = {"bills": "Bill", "sales": "Bill"}
    attribute_map = {"bills": "Bills", "sales": "Sales"}

    def __init__(self, bills=None, sales=None):
        self._bills = None
        self._sales = None
        self.discriminator = None
        if bills is not None:
            self.bills = bills
        if sales is not None:
            self.sales = sales

    @property
    def bills(self):
        return self._bills

    @bills.setter
    def bills(self, bills):
        self._bills = bills

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales
