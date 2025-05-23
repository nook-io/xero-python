# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class TimesheetEarningsLine(BaseModel):
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
        "earnings_line_id": "str",
        "earnings_rate_id": "str",
        "display_name": "str",
        "rate_per_unit": "float",
        "number_of_units": "float",
        "fixed_amount": "float",
        "amount": "float",
        "is_linked_to_timesheet": "bool",
        "is_average_daily_pay_rate": "bool",
        "is_system_generated": "bool",
    }

    attribute_map = {
        "earnings_line_id": "earningsLineID",
        "earnings_rate_id": "earningsRateID",
        "display_name": "displayName",
        "rate_per_unit": "ratePerUnit",
        "number_of_units": "numberOfUnits",
        "fixed_amount": "fixedAmount",
        "amount": "amount",
        "is_linked_to_timesheet": "isLinkedToTimesheet",
        "is_average_daily_pay_rate": "isAverageDailyPayRate",
        "is_system_generated": "isSystemGenerated",
    }

    def __init__(
        self,
        earnings_line_id=None,
        earnings_rate_id=None,
        display_name=None,
        rate_per_unit=None,
        number_of_units=None,
        fixed_amount=None,
        amount=None,
        is_linked_to_timesheet=None,
        is_average_daily_pay_rate=None,
        is_system_generated=None,
    ):  # noqa: E501
        """TimesheetEarningsLine - a model defined in OpenAPI"""  # noqa: E501

        self._earnings_line_id = None
        self._earnings_rate_id = None
        self._display_name = None
        self._rate_per_unit = None
        self._number_of_units = None
        self._fixed_amount = None
        self._amount = None
        self._is_linked_to_timesheet = None
        self._is_average_daily_pay_rate = None
        self._is_system_generated = None
        self.discriminator = None

        if earnings_line_id is not None:
            self.earnings_line_id = earnings_line_id
        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        if display_name is not None:
            self.display_name = display_name
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount
        if amount is not None:
            self.amount = amount
        if is_linked_to_timesheet is not None:
            self.is_linked_to_timesheet = is_linked_to_timesheet
        if is_average_daily_pay_rate is not None:
            self.is_average_daily_pay_rate = is_average_daily_pay_rate
        if is_system_generated is not None:
            self.is_system_generated = is_system_generated

    @property
    def earnings_line_id(self):
        """Gets the earnings_line_id of this TimesheetEarningsLine.  # noqa: E501

        Xero identifier for payroll earnings line  # noqa: E501

        :return: The earnings_line_id of this TimesheetEarningsLine.  # noqa: E501
        :rtype: str
        """
        return self._earnings_line_id

    @earnings_line_id.setter
    def earnings_line_id(self, earnings_line_id):
        """Sets the earnings_line_id of this TimesheetEarningsLine.

        Xero identifier for payroll earnings line  # noqa: E501

        :param earnings_line_id: The earnings_line_id of this TimesheetEarningsLine.  # noqa: E501
        :type: str
        """

        self._earnings_line_id = earnings_line_id

    @property
    def earnings_rate_id(self):
        """Gets the earnings_rate_id of this TimesheetEarningsLine.  # noqa: E501

        Xero identifier for payroll leave earnings rate  # noqa: E501

        :return: The earnings_rate_id of this TimesheetEarningsLine.  # noqa: E501
        :rtype: str
        """
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        """Sets the earnings_rate_id of this TimesheetEarningsLine.

        Xero identifier for payroll leave earnings rate  # noqa: E501

        :param earnings_rate_id: The earnings_rate_id of this TimesheetEarningsLine.  # noqa: E501
        :type: str
        """

        self._earnings_rate_id = earnings_rate_id

    @property
    def display_name(self):
        """Gets the display_name of this TimesheetEarningsLine.  # noqa: E501

        name of earnings rate for display in UI  # noqa: E501

        :return: The display_name of this TimesheetEarningsLine.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TimesheetEarningsLine.

        name of earnings rate for display in UI  # noqa: E501

        :param display_name: The display_name of this TimesheetEarningsLine.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def rate_per_unit(self):
        """Gets the rate_per_unit of this TimesheetEarningsLine.  # noqa: E501

        Rate per unit for leave earnings line  # noqa: E501

        :return: The rate_per_unit of this TimesheetEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        """Sets the rate_per_unit of this TimesheetEarningsLine.

        Rate per unit for leave earnings line  # noqa: E501

        :param rate_per_unit: The rate_per_unit of this TimesheetEarningsLine.  # noqa: E501
        :type: float
        """

        self._rate_per_unit = rate_per_unit

    @property
    def number_of_units(self):
        """Gets the number_of_units of this TimesheetEarningsLine.  # noqa: E501

        Leave earnings number of units  # noqa: E501

        :return: The number_of_units of this TimesheetEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this TimesheetEarningsLine.

        Leave earnings number of units  # noqa: E501

        :param number_of_units: The number_of_units of this TimesheetEarningsLine.  # noqa: E501
        :type: float
        """

        self._number_of_units = number_of_units

    @property
    def fixed_amount(self):
        """Gets the fixed_amount of this TimesheetEarningsLine.  # noqa: E501

        Leave earnings fixed amount. Only applicable if the EarningsRate RateType is Fixed  # noqa: E501

        :return: The fixed_amount of this TimesheetEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        """Sets the fixed_amount of this TimesheetEarningsLine.

        Leave earnings fixed amount. Only applicable if the EarningsRate RateType is Fixed  # noqa: E501

        :param fixed_amount: The fixed_amount of this TimesheetEarningsLine.  # noqa: E501
        :type: float
        """

        self._fixed_amount = fixed_amount

    @property
    def amount(self):
        """Gets the amount of this TimesheetEarningsLine.  # noqa: E501

        The amount of the earnings line.  # noqa: E501

        :return: The amount of this TimesheetEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TimesheetEarningsLine.

        The amount of the earnings line.  # noqa: E501

        :param amount: The amount of this TimesheetEarningsLine.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def is_linked_to_timesheet(self):
        """Gets the is_linked_to_timesheet of this TimesheetEarningsLine.  # noqa: E501

        Identifies if the leave earnings is taken from the timesheet. False for leave earnings line  # noqa: E501

        :return: The is_linked_to_timesheet of this TimesheetEarningsLine.  # noqa: E501
        :rtype: bool
        """
        return self._is_linked_to_timesheet

    @is_linked_to_timesheet.setter
    def is_linked_to_timesheet(self, is_linked_to_timesheet):
        """Sets the is_linked_to_timesheet of this TimesheetEarningsLine.

        Identifies if the leave earnings is taken from the timesheet. False for leave earnings line  # noqa: E501

        :param is_linked_to_timesheet: The is_linked_to_timesheet of this TimesheetEarningsLine.  # noqa: E501
        :type: bool
        """

        self._is_linked_to_timesheet = is_linked_to_timesheet

    @property
    def is_average_daily_pay_rate(self):
        """Gets the is_average_daily_pay_rate of this TimesheetEarningsLine.  # noqa: E501

        Identifies if the earnings is using an average daily pay rate  # noqa: E501

        :return: The is_average_daily_pay_rate of this TimesheetEarningsLine.  # noqa: E501
        :rtype: bool
        """
        return self._is_average_daily_pay_rate

    @is_average_daily_pay_rate.setter
    def is_average_daily_pay_rate(self, is_average_daily_pay_rate):
        """Sets the is_average_daily_pay_rate of this TimesheetEarningsLine.

        Identifies if the earnings is using an average daily pay rate  # noqa: E501

        :param is_average_daily_pay_rate: The is_average_daily_pay_rate of this TimesheetEarningsLine.  # noqa: E501
        :type: bool
        """

        self._is_average_daily_pay_rate = is_average_daily_pay_rate

    @property
    def is_system_generated(self):
        """Gets the is_system_generated of this TimesheetEarningsLine.  # noqa: E501

        Flag to identify whether the earnings line is system generated or not.  # noqa: E501

        :return: The is_system_generated of this TimesheetEarningsLine.  # noqa: E501
        :rtype: bool
        """
        return self._is_system_generated

    @is_system_generated.setter
    def is_system_generated(self, is_system_generated):
        """Sets the is_system_generated of this TimesheetEarningsLine.

        Flag to identify whether the earnings line is system generated or not.  # noqa: E501

        :param is_system_generated: The is_system_generated of this TimesheetEarningsLine.  # noqa: E501
        :type: bool
        """

        self._is_system_generated = is_system_generated
