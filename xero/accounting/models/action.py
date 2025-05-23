# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class Action(BaseModel):
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
    openapi_types = {"name": "str", "status": "str"}

    attribute_map = {"name": "Name", "status": "Status"}

    def __init__(self, name=None, status=None):  # noqa: E501
        """Action - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def name(self):
        """Gets the name of this Action.  # noqa: E501

        Name of the actions for this organisation  # noqa: E501

        :return: The name of this Action.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Action.

        Name of the actions for this organisation  # noqa: E501

        :param name: The name of this Action.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this Action.  # noqa: E501

        Status of the action for this organisation  # noqa: E501

        :return: The status of this Action.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Action.

        Status of the action for this organisation  # noqa: E501

        :param status: The status of this Action.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALLOWED", "NOT-ALLOWED", "None"]  # noqa: E501

        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                        status, allowed_values
                    )
                )

        self._status = status
