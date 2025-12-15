from xero.models import BaseModel


class ExpenseClaims(BaseModel):
    openapi_types = {"expense_claims": "list[ExpenseClaim]"}
    attribute_map = {"expense_claims": "ExpenseClaims"}

    def __init__(self, expense_claims=None):
        self._expense_claims = None
        self.discriminator = None
        if expense_claims is not None:
            self.expense_claims = expense_claims

    @property
    def expense_claims(self):
        return self._expense_claims

    @expense_claims.setter
    def expense_claims(self, expense_claims):
        self._expense_claims = expense_claims
