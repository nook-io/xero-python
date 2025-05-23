# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class Reimbursement(BaseModel):
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
    ):  # noqa: E501
        """Reimbursement - a model defined in OpenAPI"""  # noqa: E501

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
        """Gets the reimbursement_id of this Reimbursement.  # noqa: E501

        Xero unique identifier for a reimbursement  # noqa: E501

        :return: The reimbursement_id of this Reimbursement.  # noqa: E501
        :rtype: str
        """
        return self._reimbursement_id

    @reimbursement_id.setter
    def reimbursement_id(self, reimbursement_id):
        """Sets the reimbursement_id of this Reimbursement.

        Xero unique identifier for a reimbursement  # noqa: E501

        :param reimbursement_id: The reimbursement_id of this Reimbursement.  # noqa: E501
        :type: str
        """

        self._reimbursement_id = reimbursement_id

    @property
    def name(self):
        """Gets the name of this Reimbursement.  # noqa: E501

        Name of the reimbursement  # noqa: E501

        :return: The name of this Reimbursement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Reimbursement.

        Name of the reimbursement  # noqa: E501

        :param name: The name of this Reimbursement.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def account_id(self):
        """Gets the account_id of this Reimbursement.  # noqa: E501

        Xero unique identifier for the account used for the reimbursement  # noqa: E501

        :return: The account_id of this Reimbursement.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Reimbursement.

        Xero unique identifier for the account used for the reimbursement  # noqa: E501

        :param account_id: The account_id of this Reimbursement.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError(
                "Invalid value for `account_id`, must not be `None`"
            )  # noqa: E501

        self._account_id = account_id

    @property
    def current_record(self):
        """Gets the current_record of this Reimbursement.  # noqa: E501

        Indicates that whether the reimbursement is active  # noqa: E501

        :return: The current_record of this Reimbursement.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this Reimbursement.

        Indicates that whether the reimbursement is active  # noqa: E501

        :param current_record: The current_record of this Reimbursement.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record

    @property
    def reimbursement_category(self):
        """Gets the reimbursement_category of this Reimbursement.  # noqa: E501

        See Reimbursement Categories  # noqa: E501

        :return: The reimbursement_category of this Reimbursement.  # noqa: E501
        :rtype: str
        """
        return self._reimbursement_category

    @reimbursement_category.setter
    def reimbursement_category(self, reimbursement_category):
        """Sets the reimbursement_category of this Reimbursement.

        See Reimbursement Categories  # noqa: E501

        :param reimbursement_category: The reimbursement_category of this Reimbursement.  # noqa: E501
        :type: str
        """
        allowed_values = ["GST", "NoGST", "GSTInclusive", "None"]  # noqa: E501

        if reimbursement_category:
            if reimbursement_category not in allowed_values:
                raise ValueError(
                    "Invalid value for `reimbursement_category` ({0}), must be one of {1}".format(  # noqa: E501
                        reimbursement_category, allowed_values
                    )
                )

        self._reimbursement_category = reimbursement_category

    @property
    def calculation_type(self):
        """Gets the calculation_type of this Reimbursement.  # noqa: E501

        See Calculation Types  # noqa: E501

        :return: The calculation_type of this Reimbursement.  # noqa: E501
        :rtype: str
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this Reimbursement.

        See Calculation Types  # noqa: E501

        :param calculation_type: The calculation_type of this Reimbursement.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "FixedAmount", "RatePerUnit", "None"]  # noqa: E501

        if calculation_type:
            if calculation_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `calculation_type` ({0}), must be one of {1}".format(  # noqa: E501
                        calculation_type, allowed_values
                    )
                )

        self._calculation_type = calculation_type

    @property
    def standard_amount(self):
        """Gets the standard_amount of this Reimbursement.  # noqa: E501

        Optional Fixed Rate Amount. Applicable when calculation type is Fixed Amount  # noqa: E501

        :return: The standard_amount of this Reimbursement.  # noqa: E501
        :rtype: str
        """
        return self._standard_amount

    @standard_amount.setter
    def standard_amount(self, standard_amount):
        """Sets the standard_amount of this Reimbursement.

        Optional Fixed Rate Amount. Applicable when calculation type is Fixed Amount  # noqa: E501

        :param standard_amount: The standard_amount of this Reimbursement.  # noqa: E501
        :type: str
        """

        self._standard_amount = standard_amount

    @property
    def standard_type_of_units(self):
        """Gets the standard_type_of_units of this Reimbursement.  # noqa: E501

        Optional Type Of Units. Applicable when calculation type is Rate Per Unit  # noqa: E501

        :return: The standard_type_of_units of this Reimbursement.  # noqa: E501
        :rtype: str
        """
        return self._standard_type_of_units

    @standard_type_of_units.setter
    def standard_type_of_units(self, standard_type_of_units):
        """Sets the standard_type_of_units of this Reimbursement.

        Optional Type Of Units. Applicable when calculation type is Rate Per Unit  # noqa: E501

        :param standard_type_of_units: The standard_type_of_units of this Reimbursement.  # noqa: E501
        :type: str
        """
        allowed_values = ["Hours", "km", "None"]  # noqa: E501

        if standard_type_of_units:
            if standard_type_of_units not in allowed_values:
                raise ValueError(
                    "Invalid value for `standard_type_of_units` ({0}), must be one of {1}".format(  # noqa: E501
                        standard_type_of_units, allowed_values
                    )
                )

        self._standard_type_of_units = standard_type_of_units

    @property
    def standard_rate_per_unit(self):
        """Gets the standard_rate_per_unit of this Reimbursement.  # noqa: E501

        Optional Rate Per Unit. Applicable when calculation type is Rate Per Unit  # noqa: E501

        :return: The standard_rate_per_unit of this Reimbursement.  # noqa: E501
        :rtype: float
        """
        return self._standard_rate_per_unit

    @standard_rate_per_unit.setter
    def standard_rate_per_unit(self, standard_rate_per_unit):
        """Sets the standard_rate_per_unit of this Reimbursement.

        Optional Rate Per Unit. Applicable when calculation type is Rate Per Unit  # noqa: E501

        :param standard_rate_per_unit: The standard_rate_per_unit of this Reimbursement.  # noqa: E501
        :type: float
        """

        self._standard_rate_per_unit = standard_rate_per_unit
