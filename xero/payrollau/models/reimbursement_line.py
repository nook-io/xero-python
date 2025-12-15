from xero.models import BaseModel


class ReimbursementLine(BaseModel):
    openapi_types = {
        "reimbursement_type_id": "str",
        "amount": "float",
        "description": "str",
        "expense_account": "str",
    }
    attribute_map = {
        "reimbursement_type_id": "ReimbursementTypeID",
        "amount": "Amount",
        "description": "Description",
        "expense_account": "ExpenseAccount",
    }

    def __init__(
        self,
        reimbursement_type_id=None,
        amount=None,
        description=None,
        expense_account=None,
    ):
        self._reimbursement_type_id = None
        self._amount = None
        self._description = None
        self._expense_account = None
        self.discriminator = None
        if reimbursement_type_id is not None:
            self.reimbursement_type_id = reimbursement_type_id
        if amount is not None:
            self.amount = amount
        if description is not None:
            self.description = description
        if expense_account is not None:
            self.expense_account = expense_account

    @property
    def reimbursement_type_id(self):
        return self._reimbursement_type_id

    @reimbursement_type_id.setter
    def reimbursement_type_id(self, reimbursement_type_id):
        self._reimbursement_type_id = reimbursement_type_id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if description is not None and len(description) > 50:
            raise ValueError(
                "Invalid value for `description`, "
                "length must be less than or equal to `50`"
            )
        self._description = description

    @property
    def expense_account(self):
        return self._expense_account

    @expense_account.setter
    def expense_account(self, expense_account):
        self._expense_account = expense_account
