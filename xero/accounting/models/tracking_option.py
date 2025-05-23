# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class TrackingOption(BaseModel):
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
        "tracking_option_id": "str",
        "name": "str",
        "status": "str",
        "tracking_category_id": "str",
    }

    attribute_map = {
        "tracking_option_id": "TrackingOptionID",
        "name": "Name",
        "status": "Status",
        "tracking_category_id": "TrackingCategoryID",
    }

    def __init__(
        self, tracking_option_id=None, name=None, status=None, tracking_category_id=None
    ):  # noqa: E501
        """TrackingOption - a model defined in OpenAPI"""  # noqa: E501

        self._tracking_option_id = None
        self._name = None
        self._status = None
        self._tracking_category_id = None
        self.discriminator = None

        if tracking_option_id is not None:
            self.tracking_option_id = tracking_option_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if tracking_category_id is not None:
            self.tracking_category_id = tracking_category_id

    @property
    def tracking_option_id(self):
        """Gets the tracking_option_id of this TrackingOption.  # noqa: E501

        The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a  # noqa: E501

        :return: The tracking_option_id of this TrackingOption.  # noqa: E501
        :rtype: str
        """
        return self._tracking_option_id

    @tracking_option_id.setter
    def tracking_option_id(self, tracking_option_id):
        """Sets the tracking_option_id of this TrackingOption.

        The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a  # noqa: E501

        :param tracking_option_id: The tracking_option_id of this TrackingOption.  # noqa: E501
        :type: str
        """

        self._tracking_option_id = tracking_option_id

    @property
    def name(self):
        """Gets the name of this TrackingOption.  # noqa: E501

        The name of the tracking option e.g. Marketing, East (max length = 100)  # noqa: E501

        :return: The name of this TrackingOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrackingOption.

        The name of the tracking option e.g. Marketing, East (max length = 100)  # noqa: E501

        :param name: The name of this TrackingOption.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError(
                "Invalid value for `name`, "
                "length must be less than or equal to `100`"
            )  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this TrackingOption.  # noqa: E501

        The status of a tracking option  # noqa: E501

        :return: The status of this TrackingOption.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TrackingOption.

        The status of a tracking option  # noqa: E501

        :param status: The status of this TrackingOption.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "ARCHIVED", "DELETED", "None"]  # noqa: E501

        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                        status, allowed_values
                    )
                )

        self._status = status

    @property
    def tracking_category_id(self):
        """Gets the tracking_category_id of this TrackingOption.  # noqa: E501

        Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :return: The tracking_category_id of this TrackingOption.  # noqa: E501
        :rtype: str
        """
        return self._tracking_category_id

    @tracking_category_id.setter
    def tracking_category_id(self, tracking_category_id):
        """Sets the tracking_category_id of this TrackingOption.

        Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :param tracking_category_id: The tracking_category_id of this TrackingOption.  # noqa: E501
        :type: str
        """

        self._tracking_category_id = tracking_category_id
