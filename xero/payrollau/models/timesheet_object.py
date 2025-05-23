# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class TimesheetObject(BaseModel):
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
    openapi_types = {"timesheet": "Timesheet"}

    attribute_map = {"timesheet": "Timesheet"}

    def __init__(self, timesheet=None):  # noqa: E501
        """TimesheetObject - a model defined in OpenAPI"""  # noqa: E501

        self._timesheet = None
        self.discriminator = None

        if timesheet is not None:
            self.timesheet = timesheet

    @property
    def timesheet(self):
        """Gets the timesheet of this TimesheetObject.  # noqa: E501


        :return: The timesheet of this TimesheetObject.  # noqa: E501
        :rtype: Timesheet
        """
        return self._timesheet

    @timesheet.setter
    def timesheet(self, timesheet):
        """Sets the timesheet of this TimesheetObject.


        :param timesheet: The timesheet of this TimesheetObject.  # noqa: E501
        :type: Timesheet
        """

        self._timesheet = timesheet
