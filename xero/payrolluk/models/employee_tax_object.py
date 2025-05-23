# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class EmployeeTaxObject(BaseModel):
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
        "pagination": "Pagination",
        "problem": "Problem",
        "employee_tax": "EmployeeTax",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "employee_tax": "employeeTax",
    }

    def __init__(self, pagination=None, problem=None, employee_tax=None):  # noqa: E501
        """EmployeeTaxObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._employee_tax = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if employee_tax is not None:
            self.employee_tax = employee_tax

    @property
    def pagination(self):
        """Gets the pagination of this EmployeeTaxObject.  # noqa: E501


        :return: The pagination of this EmployeeTaxObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EmployeeTaxObject.


        :param pagination: The pagination of this EmployeeTaxObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EmployeeTaxObject.  # noqa: E501


        :return: The problem of this EmployeeTaxObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EmployeeTaxObject.


        :param problem: The problem of this EmployeeTaxObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def employee_tax(self):
        """Gets the employee_tax of this EmployeeTaxObject.  # noqa: E501


        :return: The employee_tax of this EmployeeTaxObject.  # noqa: E501
        :rtype: EmployeeTax
        """
        return self._employee_tax

    @employee_tax.setter
    def employee_tax(self, employee_tax):
        """Sets the employee_tax of this EmployeeTaxObject.


        :param employee_tax: The employee_tax of this EmployeeTaxObject.  # noqa: E501
        :type: EmployeeTax
        """

        self._employee_tax = employee_tax
