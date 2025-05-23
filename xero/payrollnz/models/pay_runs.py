# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class PayRuns(BaseModel):
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
        "pay_runs": "list[PayRun]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_runs": "payRuns",
    }

    def __init__(self, pagination=None, problem=None, pay_runs=None):  # noqa: E501
        """PayRuns - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._pay_runs = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_runs is not None:
            self.pay_runs = pay_runs

    @property
    def pagination(self):
        """Gets the pagination of this PayRuns.  # noqa: E501


        :return: The pagination of this PayRuns.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PayRuns.


        :param pagination: The pagination of this PayRuns.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this PayRuns.  # noqa: E501


        :return: The problem of this PayRuns.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this PayRuns.


        :param problem: The problem of this PayRuns.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def pay_runs(self):
        """Gets the pay_runs of this PayRuns.  # noqa: E501


        :return: The pay_runs of this PayRuns.  # noqa: E501
        :rtype: list[PayRun]
        """
        return self._pay_runs

    @pay_runs.setter
    def pay_runs(self, pay_runs):
        """Sets the pay_runs of this PayRuns.


        :param pay_runs: The pay_runs of this PayRuns.  # noqa: E501
        :type: list[PayRun]
        """

        self._pay_runs = pay_runs
