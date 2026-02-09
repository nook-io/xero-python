from xero.models import BaseModel


class Deduction(BaseModel):
    openapi_types = {
        "deduction_id": "str",
        "deduction_name": "str",
        "deduction_category": "str",
        "liability_account_id": "str",
        "current_record": "bool",
        "standard_amount": "float",
    }
    attribute_map = {
        "deduction_id": "deductionId",
        "deduction_name": "deductionName",
        "deduction_category": "deductionCategory",
        "liability_account_id": "liabilityAccountId",
        "current_record": "currentRecord",
        "standard_amount": "standardAmount",
    }

    def __init__(
        self,
        deduction_id=None,
        deduction_name=None,
        deduction_category=None,
        liability_account_id=None,
        current_record=None,
        standard_amount=None,
    ):
        self._deduction_id = None
        self._deduction_name = None
        self._deduction_category = None
        self._liability_account_id = None
        self._current_record = None
        self._standard_amount = None
        self.discriminator = None
        if deduction_id is not None:
            self.deduction_id = deduction_id
        self.deduction_name = deduction_name
        self.deduction_category = deduction_category
        self.liability_account_id = liability_account_id
        if current_record is not None:
            self.current_record = current_record
        if standard_amount is not None:
            self.standard_amount = standard_amount

    @property
    def deduction_id(self):
        return self._deduction_id

    @deduction_id.setter
    def deduction_id(self, deduction_id):
        self._deduction_id = deduction_id

    @property
    def deduction_name(self):
        return self._deduction_name

    @deduction_name.setter
    def deduction_name(self, deduction_name):
        if deduction_name is None:
            raise ValueError("Invalid value for `deduction_name`, must not be `None`")
        self._deduction_name = deduction_name

    @property
    def deduction_category(self):
        return self._deduction_category

    @deduction_category.setter
    def deduction_category(self, deduction_category):
        if deduction_category is None:
            raise ValueError(
                "Invalid value for `deduction_category`, must not be `None`"
            )
        allowed_values = [
            "PayrollGiving",
            "KiwiSaverVoluntaryContributions",
            "Superannuation",
            "NzOther",
            "None",
        ]
        if deduction_category:
            if deduction_category not in allowed_values:
                raise ValueError(
                    "Invalid value for `deduction_category` ({0}), must be one of {1}".format(
                        deduction_category, allowed_values
                    )
                )
        self._deduction_category = deduction_category

    @property
    def liability_account_id(self):
        return self._liability_account_id

    @liability_account_id.setter
    def liability_account_id(self, liability_account_id):
        if liability_account_id is None:
            raise ValueError(
                "Invalid value for `liability_account_id`, must not be `None`"
            )
        self._liability_account_id = liability_account_id

    @property
    def current_record(self):
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        self._current_record = current_record

    @property
    def standard_amount(self):
        return self._standard_amount

    @standard_amount.setter
    def standard_amount(self, standard_amount):
        self._standard_amount = standard_amount
