# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class Employees(BaseModel):
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
    openapi_types = {"employees": "list[Employee]"}

    attribute_map = {"employees": "Employees"}

    def __init__(self, employees=None):  # noqa: E501
        """Employees - a model defined in OpenAPI"""  # noqa: E501

        self._employees = None
        self.discriminator = None

        if employees is not None:
            self.employees = employees

    @property
    def employees(self):
        """Gets the employees of this Employees.  # noqa: E501


        :return: The employees of this Employees.  # noqa: E501
        :rtype: list[Employee]
        """
        return self._employees

    @employees.setter
    def employees(self, employees):
        """Sets the employees of this Employees.


        :param employees: The employees of this Employees.  # noqa: E501
        :type: list[Employee]
        """

        self._employees = employees
