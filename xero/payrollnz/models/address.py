# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class Address(BaseModel):
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
        "address_line1": "str",
        "address_line2": "str",
        "city": "str",
        "suburb": "str",
        "post_code": "str",
        "country_name": "str",
    }

    attribute_map = {
        "address_line1": "addressLine1",
        "address_line2": "addressLine2",
        "city": "city",
        "suburb": "suburb",
        "post_code": "postCode",
        "country_name": "countryName",
    }

    def __init__(
        self,
        address_line1=None,
        address_line2=None,
        city=None,
        suburb=None,
        post_code=None,
        country_name=None,
    ):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501

        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._suburb = None
        self._post_code = None
        self._country_name = None
        self.discriminator = None

        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        self.city = city
        if suburb is not None:
            self.suburb = suburb
        self.post_code = post_code
        if country_name is not None:
            self.country_name = country_name

    @property
    def address_line1(self):
        """Gets the address_line1 of this Address.  # noqa: E501

        Address line 1 for employee home address  # noqa: E501

        :return: The address_line1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this Address.

        Address line 1 for employee home address  # noqa: E501

        :param address_line1: The address_line1 of this Address.  # noqa: E501
        :type: str
        """
        if address_line1 is None:
            raise ValueError(
                "Invalid value for `address_line1`, must not be `None`"
            )  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this Address.  # noqa: E501

        Address line 2 for employee home address  # noqa: E501

        :return: The address_line2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this Address.

        Address line 2 for employee home address  # noqa: E501

        :param address_line2: The address_line2 of this Address.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        Suburb for employee home address  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        Suburb for employee home address  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError(
                "Invalid value for `city`, must not be `None`"
            )  # noqa: E501

        self._city = city

    @property
    def suburb(self):
        """Gets the suburb of this Address.  # noqa: E501

        Suburb for employee home address  # noqa: E501

        :return: The suburb of this Address.  # noqa: E501
        :rtype: str
        """
        return self._suburb

    @suburb.setter
    def suburb(self, suburb):
        """Sets the suburb of this Address.

        Suburb for employee home address  # noqa: E501

        :param suburb: The suburb of this Address.  # noqa: E501
        :type: str
        """

        self._suburb = suburb

    @property
    def post_code(self):
        """Gets the post_code of this Address.  # noqa: E501

        PostCode for employee home address  # noqa: E501

        :return: The post_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this Address.

        PostCode for employee home address  # noqa: E501

        :param post_code: The post_code of this Address.  # noqa: E501
        :type: str
        """
        if post_code is None:
            raise ValueError(
                "Invalid value for `post_code`, must not be `None`"
            )  # noqa: E501

        self._post_code = post_code

    @property
    def country_name(self):
        """Gets the country_name of this Address.  # noqa: E501

        Country of HomeAddress  # noqa: E501

        :return: The country_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this Address.

        Country of HomeAddress  # noqa: E501

        :param country_name: The country_name of this Address.  # noqa: E501
        :type: str
        """

        self._country_name = country_name
