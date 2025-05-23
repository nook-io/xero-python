# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class TaxSettings(BaseModel):
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
        "period_units": "float",
        "period_type": "str",
        "tax_code": "TaxCode",
        "special_tax_rate": "str",
        "lump_sum_tax_code": "str",
        "lump_sum_amount": "str",
    }

    attribute_map = {
        "period_units": "periodUnits",
        "period_type": "periodType",
        "tax_code": "taxCode",
        "special_tax_rate": "specialTaxRate",
        "lump_sum_tax_code": "lumpSumTaxCode",
        "lump_sum_amount": "lumpSumAmount",
    }

    def __init__(
        self,
        period_units=None,
        period_type=None,
        tax_code=None,
        special_tax_rate=None,
        lump_sum_tax_code=None,
        lump_sum_amount=None,
    ):  # noqa: E501
        """TaxSettings - a model defined in OpenAPI"""  # noqa: E501

        self._period_units = None
        self._period_type = None
        self._tax_code = None
        self._special_tax_rate = None
        self._lump_sum_tax_code = None
        self._lump_sum_amount = None
        self.discriminator = None

        if period_units is not None:
            self.period_units = period_units
        if period_type is not None:
            self.period_type = period_type
        if tax_code is not None:
            self.tax_code = tax_code
        if special_tax_rate is not None:
            self.special_tax_rate = special_tax_rate
        if lump_sum_tax_code is not None:
            self.lump_sum_tax_code = lump_sum_tax_code
        if lump_sum_amount is not None:
            self.lump_sum_amount = lump_sum_amount

    @property
    def period_units(self):
        """Gets the period_units of this TaxSettings.  # noqa: E501

        The number of units for the period type  # noqa: E501

        :return: The period_units of this TaxSettings.  # noqa: E501
        :rtype: float
        """
        return self._period_units

    @period_units.setter
    def period_units(self, period_units):
        """Sets the period_units of this TaxSettings.

        The number of units for the period type  # noqa: E501

        :param period_units: The period_units of this TaxSettings.  # noqa: E501
        :type: float
        """

        self._period_units = period_units

    @property
    def period_type(self):
        """Gets the period_type of this TaxSettings.  # noqa: E501

        The type of period (\"weeks\" or \"months\")  # noqa: E501

        :return: The period_type of this TaxSettings.  # noqa: E501
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this TaxSettings.

        The type of period (\"weeks\" or \"months\")  # noqa: E501

        :param period_type: The period_type of this TaxSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["weeks", "months", "None"]  # noqa: E501

        if period_type:
            if period_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `period_type` ({0}), must be one of {1}".format(  # noqa: E501
                        period_type, allowed_values
                    )
                )

        self._period_type = period_type

    @property
    def tax_code(self):
        """Gets the tax_code of this TaxSettings.  # noqa: E501


        :return: The tax_code of this TaxSettings.  # noqa: E501
        :rtype: TaxCode
        """
        return self._tax_code

    @tax_code.setter
    def tax_code(self, tax_code):
        """Sets the tax_code of this TaxSettings.


        :param tax_code: The tax_code of this TaxSettings.  # noqa: E501
        :type: TaxCode
        """

        self._tax_code = tax_code

    @property
    def special_tax_rate(self):
        """Gets the special_tax_rate of this TaxSettings.  # noqa: E501

        Tax rate for STC and WT  # noqa: E501

        :return: The special_tax_rate of this TaxSettings.  # noqa: E501
        :rtype: str
        """
        return self._special_tax_rate

    @special_tax_rate.setter
    def special_tax_rate(self, special_tax_rate):
        """Sets the special_tax_rate of this TaxSettings.

        Tax rate for STC and WT  # noqa: E501

        :param special_tax_rate: The special_tax_rate of this TaxSettings.  # noqa: E501
        :type: str
        """

        self._special_tax_rate = special_tax_rate

    @property
    def lump_sum_tax_code(self):
        """Gets the lump_sum_tax_code of this TaxSettings.  # noqa: E501

        Tax code for a lump sum amount  # noqa: E501

        :return: The lump_sum_tax_code of this TaxSettings.  # noqa: E501
        :rtype: str
        """
        return self._lump_sum_tax_code

    @lump_sum_tax_code.setter
    def lump_sum_tax_code(self, lump_sum_tax_code):
        """Sets the lump_sum_tax_code of this TaxSettings.

        Tax code for a lump sum amount  # noqa: E501

        :param lump_sum_tax_code: The lump_sum_tax_code of this TaxSettings.  # noqa: E501
        :type: str
        """

        self._lump_sum_tax_code = lump_sum_tax_code

    @property
    def lump_sum_amount(self):
        """Gets the lump_sum_amount of this TaxSettings.  # noqa: E501

        The total of the lump sum amount  # noqa: E501

        :return: The lump_sum_amount of this TaxSettings.  # noqa: E501
        :rtype: str
        """
        return self._lump_sum_amount

    @lump_sum_amount.setter
    def lump_sum_amount(self, lump_sum_amount):
        """Sets the lump_sum_amount of this TaxSettings.

        The total of the lump sum amount  # noqa: E501

        :param lump_sum_amount: The lump_sum_amount of this TaxSettings.  # noqa: E501
        :type: str
        """

        self._lump_sum_amount = lump_sum_amount
