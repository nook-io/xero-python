from xero.models import BaseModel


class Benefit(BaseModel):
    openapi_types = {
        "id": "str",
        "name": "str",
        "category": "str",
        "liability_account_id": "str",
        "expense_account_id": "str",
        "calculation_type_nz": "str",
        "standard_amount": "float",
        "percentage": "float",
        "company_max": "float",
        "current_record": "bool",
    }
    attribute_map = {
        "id": "id",
        "name": "name",
        "category": "category",
        "liability_account_id": "liabilityAccountId",
        "expense_account_id": "expenseAccountId",
        "calculation_type_nz": "calculationTypeNZ",
        "standard_amount": "standardAmount",
        "percentage": "percentage",
        "company_max": "companyMax",
        "current_record": "currentRecord",
    }

    def __init__(
        self,
        id=None,
        name=None,
        category=None,
        liability_account_id=None,
        expense_account_id=None,
        calculation_type_nz=None,
        standard_amount=None,
        percentage=None,
        company_max=None,
        current_record=None,
    ):
        self._id = None
        self._name = None
        self._category = None
        self._liability_account_id = None
        self._expense_account_id = None
        self._calculation_type_nz = None
        self._standard_amount = None
        self._percentage = None
        self._company_max = None
        self._current_record = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.category = category
        self.liability_account_id = liability_account_id
        self.expense_account_id = expense_account_id
        if calculation_type_nz is not None:
            self.calculation_type_nz = calculation_type_nz
        if standard_amount is not None:
            self.standard_amount = standard_amount
        if percentage is not None:
            self.percentage = percentage
        if company_max is not None:
            self.company_max = company_max
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
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")
        allowed_values = ["KiwiSaver", "ComplyingFund", "Other", "None"]
        if category:
            if category not in allowed_values:
                raise ValueError(
                    "Invalid value for `category` ({0}), must be one of {1}".format(
                        category, allowed_values
                    )
                )
        self._category = category

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
    def expense_account_id(self):
        return self._expense_account_id

    @expense_account_id.setter
    def expense_account_id(self, expense_account_id):
        if expense_account_id is None:
            raise ValueError(
                "Invalid value for `expense_account_id`, must not be `None`"
            )
        self._expense_account_id = expense_account_id

    @property
    def calculation_type_nz(self):
        return self._calculation_type_nz

    @calculation_type_nz.setter
    def calculation_type_nz(self, calculation_type_nz):
        allowed_values = [
            "FixedAmount",
            "PercentageOfTaxableEarnings",
            "None",
        ]
        if calculation_type_nz:
            if calculation_type_nz not in allowed_values:
                raise ValueError(
                    "Invalid value for `calculation_type_nz` ({0}), must be one of {1}".format(
                        calculation_type_nz, allowed_values
                    )
                )
        self._calculation_type_nz = calculation_type_nz

    @property
    def standard_amount(self):
        return self._standard_amount

    @standard_amount.setter
    def standard_amount(self, standard_amount):
        self._standard_amount = standard_amount

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage

    @property
    def company_max(self):
        return self._company_max

    @company_max.setter
    def company_max(self, company_max):
        self._company_max = company_max

    @property
    def current_record(self):
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        self._current_record = current_record
