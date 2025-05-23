# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class Deduction(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "deduction_id": "str",
        "deduction_name": "str",
        "deduction_category": "str",
        "liability_account_id": "str",
        "current_record": "bool",
        "standard_amount": "float",
        "reduces_super_liability": "bool",
        "reduces_tax_liability": "bool",
        "calculation_type": "str",
        "percentage": "float",
        "subject_to_nic": "bool",
        "subject_to_tax": "bool",
        "is_reduced_by_basic_rate": "bool",
        "apply_to_pension_calculations": "bool",
        "is_calculating_on_qualifying_earnings": "bool",
        "is_pension": "bool",
    }

    attribute_map = {
        "deduction_id": "deductionId",
        "deduction_name": "deductionName",
        "deduction_category": "deductionCategory",
        "liability_account_id": "liabilityAccountId",
        "current_record": "currentRecord",
        "standard_amount": "standardAmount",
        "reduces_super_liability": "reducesSuperLiability",
        "reduces_tax_liability": "reducesTaxLiability",
        "calculation_type": "calculationType",
        "percentage": "percentage",
        "subject_to_nic": "subjectToNIC",
        "subject_to_tax": "subjectToTax",
        "is_reduced_by_basic_rate": "isReducedByBasicRate",
        "apply_to_pension_calculations": "applyToPensionCalculations",
        "is_calculating_on_qualifying_earnings": "isCalculatingOnQualifyingEarnings",
        "is_pension": "isPension",
    }

    def __init__(
        self,
        deduction_id=None,
        deduction_name=None,
        deduction_category=None,
        liability_account_id=None,
        current_record=None,
        standard_amount=None,
        reduces_super_liability=None,
        reduces_tax_liability=None,
        calculation_type=None,
        percentage=None,
        subject_to_nic=None,
        subject_to_tax=None,
        is_reduced_by_basic_rate=None,
        apply_to_pension_calculations=None,
        is_calculating_on_qualifying_earnings=None,
        is_pension=None,
    ):  # noqa: E501
        """Deduction - a model defined in OpenAPI"""  # noqa: E501

        self._deduction_id = None
        self._deduction_name = None
        self._deduction_category = None
        self._liability_account_id = None
        self._current_record = None
        self._standard_amount = None
        self._reduces_super_liability = None
        self._reduces_tax_liability = None
        self._calculation_type = None
        self._percentage = None
        self._subject_to_nic = None
        self._subject_to_tax = None
        self._is_reduced_by_basic_rate = None
        self._apply_to_pension_calculations = None
        self._is_calculating_on_qualifying_earnings = None
        self._is_pension = None
        self.discriminator = None

        if deduction_id is not None:
            self.deduction_id = deduction_id
        self.deduction_name = deduction_name
        if deduction_category is not None:
            self.deduction_category = deduction_category
        self.liability_account_id = liability_account_id
        if current_record is not None:
            self.current_record = current_record
        if standard_amount is not None:
            self.standard_amount = standard_amount
        if reduces_super_liability is not None:
            self.reduces_super_liability = reduces_super_liability
        if reduces_tax_liability is not None:
            self.reduces_tax_liability = reduces_tax_liability
        if calculation_type is not None:
            self.calculation_type = calculation_type
        if percentage is not None:
            self.percentage = percentage
        if subject_to_nic is not None:
            self.subject_to_nic = subject_to_nic
        if subject_to_tax is not None:
            self.subject_to_tax = subject_to_tax
        if is_reduced_by_basic_rate is not None:
            self.is_reduced_by_basic_rate = is_reduced_by_basic_rate
        if apply_to_pension_calculations is not None:
            self.apply_to_pension_calculations = apply_to_pension_calculations
        if is_calculating_on_qualifying_earnings is not None:
            self.is_calculating_on_qualifying_earnings = (
                is_calculating_on_qualifying_earnings
            )
        if is_pension is not None:
            self.is_pension = is_pension

    @property
    def deduction_id(self):
        """Gets the deduction_id of this Deduction.  # noqa: E501

        The Xero identifier for Deduction  # noqa: E501

        :return: The deduction_id of this Deduction.  # noqa: E501
        :rtype: str
        """
        return self._deduction_id

    @deduction_id.setter
    def deduction_id(self, deduction_id):
        """Sets the deduction_id of this Deduction.

        The Xero identifier for Deduction  # noqa: E501

        :param deduction_id: The deduction_id of this Deduction.  # noqa: E501
        :type: str
        """

        self._deduction_id = deduction_id

    @property
    def deduction_name(self):
        """Gets the deduction_name of this Deduction.  # noqa: E501

        Name of the deduction  # noqa: E501

        :return: The deduction_name of this Deduction.  # noqa: E501
        :rtype: str
        """
        return self._deduction_name

    @deduction_name.setter
    def deduction_name(self, deduction_name):
        """Sets the deduction_name of this Deduction.

        Name of the deduction  # noqa: E501

        :param deduction_name: The deduction_name of this Deduction.  # noqa: E501
        :type: str
        """
        if deduction_name is None:
            raise ValueError(
                "Invalid value for `deduction_name`, must not be `None`"
            )  # noqa: E501

        self._deduction_name = deduction_name

    @property
    def deduction_category(self):
        """Gets the deduction_category of this Deduction.  # noqa: E501

        Deduction Category type  # noqa: E501

        :return: The deduction_category of this Deduction.  # noqa: E501
        :rtype: str
        """
        return self._deduction_category

    @deduction_category.setter
    def deduction_category(self, deduction_category):
        """Sets the deduction_category of this Deduction.

        Deduction Category type  # noqa: E501

        :param deduction_category: The deduction_category of this Deduction.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "CapitalContributions",
            "ChildCareVoucher",
            "MakingGood",
            "PostgraduateLoanDeductions",
            "PrivateUsePayments",
            "SalarySacrifice",
            "StakeholderPension",
            "StakeholderPensionPostTax",
            "StudentLoanDeductions",
            "UkOther",
            "None",
        ]  # noqa: E501

        if deduction_category:
            if deduction_category not in allowed_values:
                raise ValueError(
                    "Invalid value for `deduction_category` ({0}), must be one of {1}".format(  # noqa: E501
                        deduction_category, allowed_values
                    )
                )

        self._deduction_category = deduction_category

    @property
    def liability_account_id(self):
        """Gets the liability_account_id of this Deduction.  # noqa: E501

        Xero identifier for Liability Account  # noqa: E501

        :return: The liability_account_id of this Deduction.  # noqa: E501
        :rtype: str
        """
        return self._liability_account_id

    @liability_account_id.setter
    def liability_account_id(self, liability_account_id):
        """Sets the liability_account_id of this Deduction.

        Xero identifier for Liability Account  # noqa: E501

        :param liability_account_id: The liability_account_id of this Deduction.  # noqa: E501
        :type: str
        """
        if liability_account_id is None:
            raise ValueError(
                "Invalid value for `liability_account_id`, must not be `None`"
            )  # noqa: E501

        self._liability_account_id = liability_account_id

    @property
    def current_record(self):
        """Gets the current_record of this Deduction.  # noqa: E501

        Identifier of a record is active or not.  # noqa: E501

        :return: The current_record of this Deduction.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this Deduction.

        Identifier of a record is active or not.  # noqa: E501

        :param current_record: The current_record of this Deduction.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record

    @property
    def standard_amount(self):
        """Gets the standard_amount of this Deduction.  # noqa: E501

        Standard amount of the deduction  # noqa: E501

        :return: The standard_amount of this Deduction.  # noqa: E501
        :rtype: float
        """
        return self._standard_amount

    @standard_amount.setter
    def standard_amount(self, standard_amount):
        """Sets the standard_amount of this Deduction.

        Standard amount of the deduction  # noqa: E501

        :param standard_amount: The standard_amount of this Deduction.  # noqa: E501
        :type: float
        """

        self._standard_amount = standard_amount

    @property
    def reduces_super_liability(self):
        """Gets the reduces_super_liability of this Deduction.  # noqa: E501

        Identifier of reduces super liability  # noqa: E501

        :return: The reduces_super_liability of this Deduction.  # noqa: E501
        :rtype: bool
        """
        return self._reduces_super_liability

    @reduces_super_liability.setter
    def reduces_super_liability(self, reduces_super_liability):
        """Sets the reduces_super_liability of this Deduction.

        Identifier of reduces super liability  # noqa: E501

        :param reduces_super_liability: The reduces_super_liability of this Deduction.  # noqa: E501
        :type: bool
        """

        self._reduces_super_liability = reduces_super_liability

    @property
    def reduces_tax_liability(self):
        """Gets the reduces_tax_liability of this Deduction.  # noqa: E501

        Identifier of reduces tax liability  # noqa: E501

        :return: The reduces_tax_liability of this Deduction.  # noqa: E501
        :rtype: bool
        """
        return self._reduces_tax_liability

    @reduces_tax_liability.setter
    def reduces_tax_liability(self, reduces_tax_liability):
        """Sets the reduces_tax_liability of this Deduction.

        Identifier of reduces tax liability  # noqa: E501

        :param reduces_tax_liability: The reduces_tax_liability of this Deduction.  # noqa: E501
        :type: bool
        """

        self._reduces_tax_liability = reduces_tax_liability

    @property
    def calculation_type(self):
        """Gets the calculation_type of this Deduction.  # noqa: E501

        determine the calculation type whether fixed amount or percentage of gross  # noqa: E501

        :return: The calculation_type of this Deduction.  # noqa: E501
        :rtype: str
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this Deduction.

        determine the calculation type whether fixed amount or percentage of gross  # noqa: E501

        :param calculation_type: The calculation_type of this Deduction.  # noqa: E501
        :type: str
        """
        allowed_values = ["FixedAmount", "PercentageOfGross", "None"]  # noqa: E501

        if calculation_type:
            if calculation_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `calculation_type` ({0}), must be one of {1}".format(  # noqa: E501
                        calculation_type, allowed_values
                    )
                )

        self._calculation_type = calculation_type

    @property
    def percentage(self):
        """Gets the percentage of this Deduction.  # noqa: E501

        Percentage of gross  # noqa: E501

        :return: The percentage of this Deduction.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this Deduction.

        Percentage of gross  # noqa: E501

        :param percentage: The percentage of this Deduction.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def subject_to_nic(self):
        """Gets the subject_to_nic of this Deduction.  # noqa: E501

        Identifier of subject To NIC  # noqa: E501

        :return: The subject_to_nic of this Deduction.  # noqa: E501
        :rtype: bool
        """
        return self._subject_to_nic

    @subject_to_nic.setter
    def subject_to_nic(self, subject_to_nic):
        """Sets the subject_to_nic of this Deduction.

        Identifier of subject To NIC  # noqa: E501

        :param subject_to_nic: The subject_to_nic of this Deduction.  # noqa: E501
        :type: bool
        """

        self._subject_to_nic = subject_to_nic

    @property
    def subject_to_tax(self):
        """Gets the subject_to_tax of this Deduction.  # noqa: E501

        Identifier of subject To Tax  # noqa: E501

        :return: The subject_to_tax of this Deduction.  # noqa: E501
        :rtype: bool
        """
        return self._subject_to_tax

    @subject_to_tax.setter
    def subject_to_tax(self, subject_to_tax):
        """Sets the subject_to_tax of this Deduction.

        Identifier of subject To Tax  # noqa: E501

        :param subject_to_tax: The subject_to_tax of this Deduction.  # noqa: E501
        :type: bool
        """

        self._subject_to_tax = subject_to_tax

    @property
    def is_reduced_by_basic_rate(self):
        """Gets the is_reduced_by_basic_rate of this Deduction.  # noqa: E501

        Identifier of reduced by basic rate applicable or not  # noqa: E501

        :return: The is_reduced_by_basic_rate of this Deduction.  # noqa: E501
        :rtype: bool
        """
        return self._is_reduced_by_basic_rate

    @is_reduced_by_basic_rate.setter
    def is_reduced_by_basic_rate(self, is_reduced_by_basic_rate):
        """Sets the is_reduced_by_basic_rate of this Deduction.

        Identifier of reduced by basic rate applicable or not  # noqa: E501

        :param is_reduced_by_basic_rate: The is_reduced_by_basic_rate of this Deduction.  # noqa: E501
        :type: bool
        """

        self._is_reduced_by_basic_rate = is_reduced_by_basic_rate

    @property
    def apply_to_pension_calculations(self):
        """Gets the apply_to_pension_calculations of this Deduction.  # noqa: E501

        Identifier for apply to pension calculations  # noqa: E501

        :return: The apply_to_pension_calculations of this Deduction.  # noqa: E501
        :rtype: bool
        """
        return self._apply_to_pension_calculations

    @apply_to_pension_calculations.setter
    def apply_to_pension_calculations(self, apply_to_pension_calculations):
        """Sets the apply_to_pension_calculations of this Deduction.

        Identifier for apply to pension calculations  # noqa: E501

        :param apply_to_pension_calculations: The apply_to_pension_calculations of this Deduction.  # noqa: E501
        :type: bool
        """

        self._apply_to_pension_calculations = apply_to_pension_calculations

    @property
    def is_calculating_on_qualifying_earnings(self):
        """Gets the is_calculating_on_qualifying_earnings of this Deduction.  # noqa: E501

        Identifier of calculating on qualifying earnings  # noqa: E501

        :return: The is_calculating_on_qualifying_earnings of this Deduction.  # noqa: E501
        :rtype: bool
        """
        return self._is_calculating_on_qualifying_earnings

    @is_calculating_on_qualifying_earnings.setter
    def is_calculating_on_qualifying_earnings(
        self, is_calculating_on_qualifying_earnings
    ):
        """Sets the is_calculating_on_qualifying_earnings of this Deduction.

        Identifier of calculating on qualifying earnings  # noqa: E501

        :param is_calculating_on_qualifying_earnings: The is_calculating_on_qualifying_earnings of this Deduction.  # noqa: E501
        :type: bool
        """

        self._is_calculating_on_qualifying_earnings = (
            is_calculating_on_qualifying_earnings
        )

    @property
    def is_pension(self):
        """Gets the is_pension of this Deduction.  # noqa: E501

        Identifier of applicable for pension or not  # noqa: E501

        :return: The is_pension of this Deduction.  # noqa: E501
        :rtype: bool
        """
        return self._is_pension

    @is_pension.setter
    def is_pension(self, is_pension):
        """Sets the is_pension of this Deduction.

        Identifier of applicable for pension or not  # noqa: E501

        :param is_pension: The is_pension of this Deduction.  # noqa: E501
        :type: bool
        """

        self._is_pension = is_pension
