# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class SettingsObject(BaseModel):
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
    openapi_types = {"settings": "Settings"}

    attribute_map = {"settings": "Settings"}

    def __init__(self, settings=None):  # noqa: E501
        """SettingsObject - a model defined in OpenAPI"""  # noqa: E501

        self._settings = None
        self.discriminator = None

        if settings is not None:
            self.settings = settings

    @property
    def settings(self):
        """Gets the settings of this SettingsObject.  # noqa: E501


        :return: The settings of this SettingsObject.  # noqa: E501
        :rtype: Settings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this SettingsObject.


        :param settings: The settings of this SettingsObject.  # noqa: E501
        :type: Settings
        """

        self._settings = settings
