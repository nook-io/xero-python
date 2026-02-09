from xero.models import BaseModel


class Reimbursement(BaseModel):
    openapi_types = {
        "reimbursement_id": "str",
        "name": "str",
        "account_id": "str",
        "current_record": "bool",
        "reimbursement_category": "str",
        "calculation_type": "str",
        "standard_amount": "str",
        "standard_type_of_units": "str",
        "standard_rate_per_unit": "float",
    }
    attribute_map = {
        "reimbursement_id": "reimbursementID",
        "name": "name",
        "account_id": "accountID",
        "current_record": "currentRecord",
        "reimbursement_category": "reimbursementCategory",
        "calculation_type": "calculationType",
        "standard_amount": "standardAmount",
        "standard_type_of_units": "standardTypeOfUnits",
        "standard_rate_per_unit": "standardRatePerUnit",
    }

    def __init__(
        self,
        reimbursement_id=None,
        name=None,
        account_id=None,
        current_record=None,
        reimbursement_category=None,
        calculation_type=None,
        standard_amount=None,
        standard_type_of_units=None,
        standard_rate_per_unit=None,
    ):
        self._reimbursement_id = None
        self._name = None
        self._account_id = None
        self._current_record = None
        self._reimbursement_category = None
        self._calculation_type = None
        self._standard_amount = None
        self._standard_type_of_units = None
        self._standard_rate_per_unit = None
        self.discriminator = None
        if reimbursement_id is not None:
            self.reimbursement_id = reimbursement_id
        self.name = name
        self.account_id = account_id
        if current_record is not None:
            self.current_record = current_record
        if reimbursement_category is not None:
            self.reimbursement_category = reimbursement_category
        if calculation_type is not None:
            self.calculation_type = calculation_type
        if standard_amount is not None:
            self.standard_amount = standard_amount
        if standard_type_of_units is not None:
            self.standard_type_of_units = standard_type_of_units
        if standard_rate_per_unit is not None:
            self.standard_rate_per_unit = standard_rate_per_unit

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

    @property
    def reimbursement_category(self):
        return self._reimbursement_category

    @reimbursement_category.setter
    def reimbursement_category(self, reimbursement_category):
        allowed_values = ["GST", "NoGST", "GSTInclusive", "None"]
        if reimbursement_category:
            if reimbursement_category not in allowed_values:
                raise ValueError(
                    "Invalid value for `reimbursement_category` ({0}), must be one of {1}".format(
                        reimbursement_category, allowed_values
                    )
                )
        self._reimbursement_category = reimbursement_category

    @property
    def calculation_type(self):
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        allowed_values = ["Unknown", "FixedAmount", "RatePerUnit", "None"]
        if calculation_type:
            if calculation_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `calculation_type` ({0}), must be one of {1}".format(
                        calculation_type, allowed_values
                    )
                )
        self._calculation_type = calculation_type

    @property
    def standard_amount(self):
        return self._standard_amount

    @standard_amount.setter
    def standard_amount(self, standard_amount):
        self._standard_amount = standard_amount

    @property
    def standard_type_of_units(self):
        return self._standard_type_of_units

    @standard_type_of_units.setter
    def standard_type_of_units(self, standard_type_of_units):
        allowed_values = ["Hours", "km", "None"]
        if standard_type_of_units:
            if standard_type_of_units not in allowed_values:
                raise ValueError(
                    "Invalid value for `standard_type_of_units` ({0}), must be one of {1}".format(
                        standard_type_of_units, allowed_values
                    )
                )
        self._standard_type_of_units = standard_type_of_units

    @property
    def standard_rate_per_unit(self):
        return self._standard_rate_per_unit

    @standard_rate_per_unit.setter
    def standard_rate_per_unit(self, standard_rate_per_unit):
        self._standard_rate_per_unit = standard_rate_per_unit
