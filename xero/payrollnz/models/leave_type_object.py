# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class LeaveTypeObject(BaseModel):
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
        "leave_type": "LeaveType",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "leave_type": "leaveType",
    }

    def __init__(self, pagination=None, problem=None, leave_type=None):  # noqa: E501
        """LeaveTypeObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._leave_type = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave_type is not None:
            self.leave_type = leave_type

    @property
    def pagination(self):
        """Gets the pagination of this LeaveTypeObject.  # noqa: E501


        :return: The pagination of this LeaveTypeObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this LeaveTypeObject.


        :param pagination: The pagination of this LeaveTypeObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this LeaveTypeObject.  # noqa: E501


        :return: The problem of this LeaveTypeObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this LeaveTypeObject.


        :param problem: The problem of this LeaveTypeObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def leave_type(self):
        """Gets the leave_type of this LeaveTypeObject.  # noqa: E501


        :return: The leave_type of this LeaveTypeObject.  # noqa: E501
        :rtype: LeaveType
        """
        return self._leave_type

    @leave_type.setter
    def leave_type(self, leave_type):
        """Sets the leave_type of this LeaveTypeObject.


        :param leave_type: The leave_type of this LeaveTypeObject.  # noqa: E501
        :type: LeaveType
        """

        self._leave_type = leave_type
