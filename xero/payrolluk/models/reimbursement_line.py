from xero.models import BaseModel


class ReimbursementLine(BaseModel):
    openapi_types = {
        "reimbursement_type_id": "str",
        "description": "str",
        "amount": "float",
    }
    attribute_map = {
        "reimbursement_type_id": "reimbursementTypeID",
        "description": "description",
        "amount": "amount",
    }

    def __init__(self, reimbursement_type_id=None, description=None, amount=None):
        self._reimbursement_type_id = None
        self._description = None
        self._amount = None
        self.discriminator = None
        if reimbursement_type_id is not None:
            self.reimbursement_type_id = reimbursement_type_id
        if description is not None:
            self.description = description
        if amount is not None:
            self.amount = amount

    @property
    def reimbursement_type_id(self):
        return self._reimbursement_type_id

    @reimbursement_type_id.setter
    def reimbursement_type_id(self, reimbursement_type_id):
        self._reimbursement_type_id = reimbursement_type_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount
