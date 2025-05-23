# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class ExternalLink(BaseModel):
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
    openapi_types = {"link_type": "str", "url": "str", "description": "str"}

    attribute_map = {
        "link_type": "LinkType",
        "url": "Url",
        "description": "Description",
    }

    def __init__(self, link_type=None, url=None, description=None):  # noqa: E501
        """ExternalLink - a model defined in OpenAPI"""  # noqa: E501

        self._link_type = None
        self._url = None
        self._description = None
        self.discriminator = None

        if link_type is not None:
            self.link_type = link_type
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description

    @property
    def link_type(self):
        """Gets the link_type of this ExternalLink.  # noqa: E501

        See External link types  # noqa: E501

        :return: The link_type of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this ExternalLink.

        See External link types  # noqa: E501

        :param link_type: The link_type of this ExternalLink.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Facebook",
            "GooglePlus",
            "LinkedIn",
            "Twitter",
            "Website",
            "None",
        ]  # noqa: E501

        if link_type:
            if link_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `link_type` ({0}), must be one of {1}".format(  # noqa: E501
                        link_type, allowed_values
                    )
                )

        self._link_type = link_type

    @property
    def url(self):
        """Gets the url of this ExternalLink.  # noqa: E501

        URL for service e.g. http://twitter.com/xeroapi  # noqa: E501

        :return: The url of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ExternalLink.

        URL for service e.g. http://twitter.com/xeroapi  # noqa: E501

        :param url: The url of this ExternalLink.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def description(self):
        """Gets the description of this ExternalLink.  # noqa: E501


        :return: The description of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExternalLink.


        :param description: The description of this ExternalLink.  # noqa: E501
        :type: str
        """

        self._description = description
