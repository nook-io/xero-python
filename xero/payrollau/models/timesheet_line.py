# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class TimesheetLine(BaseModel):
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
        "earnings_rate_id": "str",
        "tracking_item_id": "str",
        "number_of_units": "list[float]",
        "updated_date_utc": "datetime[ms-format]",
    }

    attribute_map = {
        "earnings_rate_id": "EarningsRateID",
        "tracking_item_id": "TrackingItemID",
        "number_of_units": "NumberOfUnits",
        "updated_date_utc": "UpdatedDateUTC",
    }

    def __init__(
        self,
        earnings_rate_id=None,
        tracking_item_id=None,
        number_of_units=None,
        updated_date_utc=None,
    ):  # noqa: E501
        """TimesheetLine - a model defined in OpenAPI"""  # noqa: E501

        self._earnings_rate_id = None
        self._tracking_item_id = None
        self._number_of_units = None
        self._updated_date_utc = None
        self.discriminator = None

        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        if tracking_item_id is not None:
            self.tracking_item_id = tracking_item_id
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def earnings_rate_id(self):
        """Gets the earnings_rate_id of this TimesheetLine.  # noqa: E501

        The Xero identifier for an Earnings Rate  # noqa: E501

        :return: The earnings_rate_id of this TimesheetLine.  # noqa: E501
        :rtype: str
        """
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        """Sets the earnings_rate_id of this TimesheetLine.

        The Xero identifier for an Earnings Rate  # noqa: E501

        :param earnings_rate_id: The earnings_rate_id of this TimesheetLine.  # noqa: E501
        :type: str
        """

        self._earnings_rate_id = earnings_rate_id

    @property
    def tracking_item_id(self):
        """Gets the tracking_item_id of this TimesheetLine.  # noqa: E501

        The Xero identifier for a Tracking Category. The TrackingOptionID must belong to the TrackingCategory selected as TimesheetCategories under Payroll Settings.  # noqa: E501

        :return: The tracking_item_id of this TimesheetLine.  # noqa: E501
        :rtype: str
        """
        return self._tracking_item_id

    @tracking_item_id.setter
    def tracking_item_id(self, tracking_item_id):
        """Sets the tracking_item_id of this TimesheetLine.

        The Xero identifier for a Tracking Category. The TrackingOptionID must belong to the TrackingCategory selected as TimesheetCategories under Payroll Settings.  # noqa: E501

        :param tracking_item_id: The tracking_item_id of this TimesheetLine.  # noqa: E501
        :type: str
        """

        self._tracking_item_id = tracking_item_id

    @property
    def number_of_units(self):
        """Gets the number_of_units of this TimesheetLine.  # noqa: E501

        The number of units on a timesheet line  # noqa: E501

        :return: The number_of_units of this TimesheetLine.  # noqa: E501
        :rtype: list[float]
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this TimesheetLine.

        The number of units on a timesheet line  # noqa: E501

        :param number_of_units: The number_of_units of this TimesheetLine.  # noqa: E501
        :type: list[float]
        """

        self._number_of_units = number_of_units

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this TimesheetLine.  # noqa: E501

        Last modified timestamp  # noqa: E501

        :return: The updated_date_utc of this TimesheetLine.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this TimesheetLine.

        Last modified timestamp  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this TimesheetLine.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc
