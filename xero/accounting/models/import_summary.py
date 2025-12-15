from xero.models import BaseModel


class ImportSummary(BaseModel):
    openapi_types = {
        "accounts": "ImportSummaryAccounts",
        "organisation": "ImportSummaryOrganisation",
    }
    attribute_map = {"accounts": "Accounts", "organisation": "Organisation"}

    def __init__(self, accounts=None, organisation=None):
        self._accounts = None
        self._organisation = None
        self.discriminator = None
        if accounts is not None:
            self.accounts = accounts
        if organisation is not None:
            self.organisation = organisation

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts

    @property
    def organisation(self):
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        self._organisation = organisation
