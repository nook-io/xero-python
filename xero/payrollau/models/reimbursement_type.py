from xero.models import BaseModel


class ReimbursementType(BaseModel):
    openapi_types = {
        "name": "str",
        "account_code": "str",
        "reimbursement_type_id": "str",
        "updated_date_utc": "datetime[ms-format]",
        "current_record": "bool",
    }
    attribute_map = {
        "name": "Name",
        "account_code": "AccountCode",
        "reimbursement_type_id": "ReimbursementTypeID",
        "updated_date_utc": "UpdatedDateUTC",
        "current_record": "CurrentRecord",
    }

    def __init__(
        self,
        name=None,
        account_code=None,
        reimbursement_type_id=None,
        updated_date_utc=None,
        current_record=None,
    ):
        self._name = None
        self._account_code = None
        self._reimbursement_type_id = None
        self._updated_date_utc = None
        self._current_record = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if account_code is not None:
            self.account_code = account_code
        if reimbursement_type_id is not None:
            self.reimbursement_type_id = reimbursement_type_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if current_record is not None:
            self.current_record = current_record

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 100:
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `100`"
            )
        self._name = name

    @property
    def account_code(self):
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        self._account_code = account_code

    @property
    def reimbursement_type_id(self):
        return self._reimbursement_type_id

    @reimbursement_type_id.setter
    def reimbursement_type_id(self, reimbursement_type_id):
        self._reimbursement_type_id = reimbursement_type_id

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def current_record(self):
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        self._current_record = current_record
