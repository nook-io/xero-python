from xero.models import BaseModel


class Reimbursement(BaseModel):
    openapi_types = {
        "reimbursement_id": "str",
        "name": "str",
        "account_id": "str",
        "current_record": "bool",
    }
    attribute_map = {
        "reimbursement_id": "reimbursementID",
        "name": "name",
        "account_id": "accountID",
        "current_record": "currentRecord",
    }

    def __init__(
        self, reimbursement_id=None, name=None, account_id=None, current_record=None
    ):
        self._reimbursement_id = None
        self._name = None
        self._account_id = None
        self._current_record = None
        self.discriminator = None
        if reimbursement_id is not None:
            self.reimbursement_id = reimbursement_id
        self.name = name
        self.account_id = account_id
        if current_record is not None:
            self.current_record = current_record

    @property
    def reimbursement_id(self):
        return self._reimbursement_id

    @reimbursement_id.setter
    def reimbursement_id(self, reimbursement_id):
        self._reimbursement_id = reimbursement_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")
        self._account_id = account_id

    @property
    def current_record(self):
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        self._current_record = current_record
