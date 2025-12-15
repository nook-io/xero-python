from xero.models import BaseModel


class Benefit(BaseModel):
    openapi_types = {
        "id": "str",
        "name": "str",
        "category": "str",
        "liability_account_id": "str",
        "expense_account_id": "str",
        "standard_amount": "float",
        "percentage": "float",
        "calculation_type": "str",
        "current_record": "bool",
        "subject_to_nic": "bool",
        "subject_to_pension": "bool",
        "subject_to_tax": "bool",
        "is_calculating_on_qualifying_earnings": "bool",
        "show_balance_to_employee": "bool",
    }
    attribute_map = {
        "id": "id",
        "name": "name",
        "category": "category",
        "liability_account_id": "liabilityAccountId",
        "expense_account_id": "expenseAccountId",
        "standard_amount": "standardAmount",
        "percentage": "percentage",
        "calculation_type": "calculationType",
        "current_record": "currentRecord",
        "subject_to_nic": "subjectToNIC",
        "subject_to_pension": "subjectToPension",
        "subject_to_tax": "subjectToTax",
        "is_calculating_on_qualifying_earnings": "isCalculatingOnQualifyingEarnings",
        "show_balance_to_employee": "showBalanceToEmployee",
    }

    def __init__(
        self,
        id=None,
        name=None,
        category=None,
        liability_account_id=None,
        expense_account_id=None,
        standard_amount=None,
        percentage=None,
        calculation_type=None,
        current_record=None,
        subject_to_nic=None,
        subject_to_pension=None,
        subject_to_tax=None,
        is_calculating_on_qualifying_earnings=None,
        show_balance_to_employee=None,
    ):
        self._id = None
        self._name = None
        self._category = None
        self._liability_account_id = None
        self._expense_account_id = None
        self._standard_amount = None
        self._percentage = None
        self._calculation_type = None
        self._current_record = None
        self._subject_to_nic = None
        self._subject_to_pension = None
        self._subject_to_tax = None
        self._is_calculating_on_qualifying_earnings = None
        self._show_balance_to_employee = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.category = category
        self.liability_account_id = liability_account_id
        self.expense_account_id = expense_account_id
        if standard_amount is not None:
            self.standard_amount = standard_amount
        self.percentage = percentage
        self.calculation_type = calculation_type
        if current_record is not None:
            self.current_record = current_record
        if subject_to_nic is not None:
            self.subject_to_nic = subject_to_nic
        if subject_to_pension is not None:
            self.subject_to_pension = subject_to_pension
        if subject_to_tax is not None:
            self.subject_to_tax = subject_to_tax
        if is_calculating_on_qualifying_earnings is not None:
            self.is_calculating_on_qualifying_earnings = (
                is_calculating_on_qualifying_earnings
            )
        if show_balance_to_employee is not None:
            self.show_balance_to_employee = show_balance_to_employee

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
        allowed_values = ["StakeholderPension", "Other", "None"]
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
        if percentage is None:
            raise ValueError("Invalid value for `percentage`, must not be `None`")
        self._percentage = percentage

    @property
    def calculation_type(self):
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        if calculation_type is None:
            raise ValueError("Invalid value for `calculation_type`, must not be `None`")
        allowed_values = ["FixedAmount", "PercentageOfGross", "None"]
        if calculation_type:
            if calculation_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `calculation_type` ({0}), must be one of {1}".format(
                        calculation_type, allowed_values
                    )
                )
        self._calculation_type = calculation_type

    @property
    def current_record(self):
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        self._current_record = current_record

    @property
    def subject_to_nic(self):
        return self._subject_to_nic

    @subject_to_nic.setter
    def subject_to_nic(self, subject_to_nic):
        self._subject_to_nic = subject_to_nic

    @property
    def subject_to_pension(self):
        return self._subject_to_pension

    @subject_to_pension.setter
    def subject_to_pension(self, subject_to_pension):
        self._subject_to_pension = subject_to_pension

    @property
    def subject_to_tax(self):
        return self._subject_to_tax

    @subject_to_tax.setter
    def subject_to_tax(self, subject_to_tax):
        self._subject_to_tax = subject_to_tax

    @property
    def is_calculating_on_qualifying_earnings(self):
        return self._is_calculating_on_qualifying_earnings

    @is_calculating_on_qualifying_earnings.setter
    def is_calculating_on_qualifying_earnings(
        self, is_calculating_on_qualifying_earnings
    ):
        self._is_calculating_on_qualifying_earnings = (
            is_calculating_on_qualifying_earnings
        )

    @property
    def show_balance_to_employee(self):
        return self._show_balance_to_employee

    @show_balance_to_employee.setter
    def show_balance_to_employee(self, show_balance_to_employee):
        self._show_balance_to_employee = show_balance_to_employee
