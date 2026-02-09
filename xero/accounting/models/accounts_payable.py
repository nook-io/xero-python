from xero.models import BaseModel


class AccountsPayable(BaseModel):
    openapi_types = {"outstanding": "float", "overdue": "float"}
    attribute_map = {"outstanding": "Outstanding", "overdue": "Overdue"}

    def __init__(self, outstanding=None, overdue=None):
        self._outstanding = None
        self._overdue = None
        self.discriminator = None
        if outstanding is not None:
            self.outstanding = outstanding
        if overdue is not None:
            self.overdue = overdue

    @property
    def outstanding(self):
        return self._outstanding

    @outstanding.setter
    def outstanding(self, outstanding):
        self._outstanding = outstanding

    @property
    def overdue(self):
        return self._overdue

    @overdue.setter
    def overdue(self, overdue):
        self._overdue = overdue
