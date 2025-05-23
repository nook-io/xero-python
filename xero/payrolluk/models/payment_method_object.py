# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class PaymentMethodObject(BaseModel):
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
        "payment_method": "PaymentMethod",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "payment_method": "paymentMethod",
    }

    def __init__(
        self, pagination=None, problem=None, payment_method=None
    ):  # noqa: E501
        """PaymentMethodObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._payment_method = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if payment_method is not None:
            self.payment_method = payment_method

    @property
    def pagination(self):
        """Gets the pagination of this PaymentMethodObject.  # noqa: E501


        :return: The pagination of this PaymentMethodObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaymentMethodObject.


        :param pagination: The pagination of this PaymentMethodObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this PaymentMethodObject.  # noqa: E501


        :return: The problem of this PaymentMethodObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this PaymentMethodObject.


        :param problem: The problem of this PaymentMethodObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentMethodObject.  # noqa: E501


        :return: The payment_method of this PaymentMethodObject.  # noqa: E501
        :rtype: PaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentMethodObject.


        :param payment_method: The payment_method of this PaymentMethodObject.  # noqa: E501
        :type: PaymentMethod
        """

        self._payment_method = payment_method
