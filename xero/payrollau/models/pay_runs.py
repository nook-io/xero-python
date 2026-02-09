from xero.models import BaseModel


class PayRuns(BaseModel):
    openapi_types = {"pay_runs": "list[PayRun]"}
    attribute_map = {"pay_runs": "PayRuns"}

    def __init__(self, pay_runs=None):
        self._pay_runs = None
        self.discriminator = None
        if pay_runs is not None:
            self.pay_runs = pay_runs

    @property
    def pay_runs(self):
        return self._pay_runs

    @pay_runs.setter
    def pay_runs(self, pay_runs):
        self._pay_runs = pay_runs
