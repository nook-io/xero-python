# coding: utf-8

"""
    Xero Files API

    These endpoints are specific to Xero Files API  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class User(BaseModel):
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
        "id": "str",
        "name": "str",
        "first_name": "str",
        "last_name": "str",
        "full_name": "str",
    }

    attribute_map = {
        "id": "Id",
        "name": "Name",
        "first_name": "FirstName",
        "last_name": "LastName",
        "full_name": "FullName",
    }

    def __init__(
        self, id=None, name=None, first_name=None, last_name=None, full_name=None
    ):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._first_name = None
        self._last_name = None
        self._full_name = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if full_name is not None:
            self.full_name = full_name

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        Xero identifier  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501

        Key is Name, but returns Email address of user who created the file  # noqa: E501

        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.

        Key is Name, but returns Email address of user who created the file  # noqa: E501

        :param name: The name of this User.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501

        First name of user  # noqa: E501

        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.

        First name of user  # noqa: E501

        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501

        Last name of user  # noqa: E501

        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.

        Last name of user  # noqa: E501

        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def full_name(self):
        """Gets the full_name of this User.  # noqa: E501

        Last name of user  # noqa: E501

        :return: The full_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this User.

        Last name of user  # noqa: E501

        :param full_name: The full_name of this User.  # noqa: E501
        :type: str
        """

        self._full_name = full_name
