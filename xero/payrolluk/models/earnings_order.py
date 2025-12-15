from xero.models import BaseModel


class EarningsOrder(BaseModel):
    openapi_types = {
        "id": "str",
        "name": "str",
        "statutory_deduction_category": "StatutoryDeductionCategory",
        "liability_account_id": "str",
        "current_record": "bool",
    }
    attribute_map = {
        "id": "id",
        "name": "name",
        "statutory_deduction_category": "statutoryDeductionCategory",
        "liability_account_id": "liabilityAccountId",
        "current_record": "currentRecord",
    }

    def __init__(
        self,
        id=None,
        name=None,
        statutory_deduction_category=None,
        liability_account_id=None,
        current_record=True,
    ):
        self._id = None
        self._name = None
        self._statutory_deduction_category = None
        self._liability_account_id = None
        self._current_record = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if statutory_deduction_category is not None:
            self.statutory_deduction_category = statutory_deduction_category
        if liability_account_id is not None:
            self.liability_account_id = liability_account_id
        if current_record is not None:
            self.current_record = current_record

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def statutory_deduction_category(self):
        return self._statutory_deduction_category

    @statutory_deduction_category.setter
    def statutory_deduction_category(self, statutory_deduction_category):
        self._statutory_deduction_category = statutory_deduction_category

    @property
    def liability_account_id(self):
        return self._liability_account_id

    @liability_account_id.setter
    def liability_account_id(self, liability_account_id):
        self._liability_account_id = liability_account_id

    @property
    def current_record(self):
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        self._current_record = current_record
