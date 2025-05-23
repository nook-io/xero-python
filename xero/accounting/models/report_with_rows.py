# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class ReportWithRows(BaseModel):
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
    openapi_types = {"reports": "list[ReportWithRow]"}

    attribute_map = {"reports": "Reports"}

    def __init__(self, reports=None):  # noqa: E501
        """ReportWithRows - a model defined in OpenAPI"""  # noqa: E501

        self._reports = None
        self.discriminator = None

        if reports is not None:
            self.reports = reports

    @property
    def reports(self):
        """Gets the reports of this ReportWithRows.  # noqa: E501


        :return: The reports of this ReportWithRows.  # noqa: E501
        :rtype: list[ReportWithRow]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this ReportWithRows.


        :param reports: The reports of this ReportWithRows.  # noqa: E501
        :type: list[ReportWithRow]
        """

        self._reports = reports
