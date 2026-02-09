from xero.models import BaseModel


class Budgets(BaseModel):
    openapi_types = {"budgets": "list[Budget]"}
    attribute_map = {"budgets": "Budgets"}

    def __init__(self, budgets=None):
        self._budgets = None
        self.discriminator = None
        if budgets is not None:
            self.budgets = budgets

    @property
    def budgets(self):
        return self._budgets

    @budgets.setter
    def budgets(self, budgets):
        self._budgets = budgets
