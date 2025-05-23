# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class ContactPerson(BaseModel):
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
        "first_name": "str",
        "last_name": "str",
        "email_address": "str",
        "include_in_emails": "bool",
    }

    attribute_map = {
        "first_name": "FirstName",
        "last_name": "LastName",
        "email_address": "EmailAddress",
        "include_in_emails": "IncludeInEmails",
    }

    def __init__(
        self,
        first_name=None,
        last_name=None,
        email_address=None,
        include_in_emails=None,
    ):  # noqa: E501
        """ContactPerson - a model defined in OpenAPI"""  # noqa: E501

        self._first_name = None
        self._last_name = None
        self._email_address = None
        self._include_in_emails = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email_address is not None:
            self.email_address = email_address
        if include_in_emails is not None:
            self.include_in_emails = include_in_emails

    @property
    def first_name(self):
        """Gets the first_name of this ContactPerson.  # noqa: E501

        First name of person  # noqa: E501

        :return: The first_name of this ContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ContactPerson.

        First name of person  # noqa: E501

        :param first_name: The first_name of this ContactPerson.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ContactPerson.  # noqa: E501

        Last name of person  # noqa: E501

        :return: The last_name of this ContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ContactPerson.

        Last name of person  # noqa: E501

        :param last_name: The last_name of this ContactPerson.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email_address(self):
        """Gets the email_address of this ContactPerson.  # noqa: E501

        Email address of person  # noqa: E501

        :return: The email_address of this ContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this ContactPerson.

        Email address of person  # noqa: E501

        :param email_address: The email_address of this ContactPerson.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def include_in_emails(self):
        """Gets the include_in_emails of this ContactPerson.  # noqa: E501

        boolean to indicate whether contact should be included on emails with invoices etc.  # noqa: E501

        :return: The include_in_emails of this ContactPerson.  # noqa: E501
        :rtype: bool
        """
        return self._include_in_emails

    @include_in_emails.setter
    def include_in_emails(self, include_in_emails):
        """Sets the include_in_emails of this ContactPerson.

        boolean to indicate whether contact should be included on emails with invoices etc.  # noqa: E501

        :param include_in_emails: The include_in_emails of this ContactPerson.  # noqa: E501
        :type: bool
        """

        self._include_in_emails = include_in_emails
