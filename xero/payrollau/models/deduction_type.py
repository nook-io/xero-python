from xero.models import BaseModel


class DeductionType(BaseModel):
    openapi_types = {
        "name": "str",
        "account_code": "str",
        "reduces_tax": "bool",
        "reduces_super": "bool",
        "is_exempt_from_w1": "bool",
        "deduction_type_id": "str",
        "updated_date_utc": "datetime[ms-format]",
        "deduction_category": "str",
        "current_record": "bool",
    }
    attribute_map = {
        "name": "Name",
        "account_code": "AccountCode",
        "reduces_tax": "ReducesTax",
        "reduces_super": "ReducesSuper",
        "is_exempt_from_w1": "IsExemptFromW1",
        "deduction_type_id": "DeductionTypeID",
        "updated_date_utc": "UpdatedDateUTC",
        "deduction_category": "DeductionCategory",
        "current_record": "CurrentRecord",
    }

    def __init__(
        self,
        name=None,
        account_code=None,
        reduces_tax=None,
        reduces_super=None,
        is_exempt_from_w1=None,
        deduction_type_id=None,
        updated_date_utc=None,
        deduction_category=None,
        current_record=None,
    ):
        self._name = None
        self._account_code = None
        self._reduces_tax = None
        self._reduces_super = None
        self._is_exempt_from_w1 = None
        self._deduction_type_id = None
        self._updated_date_utc = None
        self._deduction_category = None
        self._current_record = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if account_code is not None:
            self.account_code = account_code
        if reduces_tax is not None:
            self.reduces_tax = reduces_tax
        if reduces_super is not None:
            self.reduces_super = reduces_super
        if is_exempt_from_w1 is not None:
            self.is_exempt_from_w1 = is_exempt_from_w1
        if deduction_type_id is not None:
            self.deduction_type_id = deduction_type_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if deduction_category is not None:
            self.deduction_category = deduction_category
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
    def reduces_tax(self):
        return self._reduces_tax

    @reduces_tax.setter
    def reduces_tax(self, reduces_tax):
        self._reduces_tax = reduces_tax

    @property
    def reduces_super(self):
        return self._reduces_super

    @reduces_super.setter
    def reduces_super(self, reduces_super):
        self._reduces_super = reduces_super

    @property
    def is_exempt_from_w1(self):
        return self._is_exempt_from_w1

    @is_exempt_from_w1.setter
    def is_exempt_from_w1(self, is_exempt_from_w1):
        self._is_exempt_from_w1 = is_exempt_from_w1

    @property
    def deduction_type_id(self):
        return self._deduction_type_id

    @deduction_type_id.setter
    def deduction_type_id(self, deduction_type_id):
        self._deduction_type_id = deduction_type_id

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def deduction_category(self):
        return self._deduction_category

    @deduction_category.setter
    def deduction_category(self, deduction_category):
        allowed_values = ["NONE", "UNIONFEES", "WORKPLACEGIVING", "None"]
        if deduction_category:
            if deduction_category not in allowed_values:
                raise ValueError(
                    "Invalid value for `deduction_category` ({0}), must be one of {1}".format(
                        deduction_category, allowed_values
                    )
                )
        self._deduction_category = deduction_category

    @property
    def current_record(self):
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        self._current_record = current_record
