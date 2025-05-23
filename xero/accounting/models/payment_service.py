# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class PaymentService(BaseModel):
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
        "payment_service_id": "str",
        "payment_service_name": "str",
        "payment_service_url": "str",
        "pay_now_text": "str",
        "payment_service_type": "str",
        "validation_errors": "list[ValidationError]",
    }

    attribute_map = {
        "payment_service_id": "PaymentServiceID",
        "payment_service_name": "PaymentServiceName",
        "payment_service_url": "PaymentServiceUrl",
        "pay_now_text": "PayNowText",
        "payment_service_type": "PaymentServiceType",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        payment_service_id=None,
        payment_service_name=None,
        payment_service_url=None,
        pay_now_text=None,
        payment_service_type=None,
        validation_errors=None,
    ):  # noqa: E501
        """PaymentService - a model defined in OpenAPI"""  # noqa: E501

        self._payment_service_id = None
        self._payment_service_name = None
        self._payment_service_url = None
        self._pay_now_text = None
        self._payment_service_type = None
        self._validation_errors = None
        self.discriminator = None

        if payment_service_id is not None:
            self.payment_service_id = payment_service_id
        if payment_service_name is not None:
            self.payment_service_name = payment_service_name
        if payment_service_url is not None:
            self.payment_service_url = payment_service_url
        if pay_now_text is not None:
            self.pay_now_text = pay_now_text
        if payment_service_type is not None:
            self.payment_service_type = payment_service_type
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def payment_service_id(self):
        """Gets the payment_service_id of this PaymentService.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The payment_service_id of this PaymentService.  # noqa: E501
        :rtype: str
        """
        return self._payment_service_id

    @payment_service_id.setter
    def payment_service_id(self, payment_service_id):
        """Sets the payment_service_id of this PaymentService.

        Xero identifier  # noqa: E501

        :param payment_service_id: The payment_service_id of this PaymentService.  # noqa: E501
        :type: str
        """

        self._payment_service_id = payment_service_id

    @property
    def payment_service_name(self):
        """Gets the payment_service_name of this PaymentService.  # noqa: E501

        Name of payment service  # noqa: E501

        :return: The payment_service_name of this PaymentService.  # noqa: E501
        :rtype: str
        """
        return self._payment_service_name

    @payment_service_name.setter
    def payment_service_name(self, payment_service_name):
        """Sets the payment_service_name of this PaymentService.

        Name of payment service  # noqa: E501

        :param payment_service_name: The payment_service_name of this PaymentService.  # noqa: E501
        :type: str
        """

        self._payment_service_name = payment_service_name

    @property
    def payment_service_url(self):
        """Gets the payment_service_url of this PaymentService.  # noqa: E501

        The custom payment URL  # noqa: E501

        :return: The payment_service_url of this PaymentService.  # noqa: E501
        :rtype: str
        """
        return self._payment_service_url

    @payment_service_url.setter
    def payment_service_url(self, payment_service_url):
        """Sets the payment_service_url of this PaymentService.

        The custom payment URL  # noqa: E501

        :param payment_service_url: The payment_service_url of this PaymentService.  # noqa: E501
        :type: str
        """

        self._payment_service_url = payment_service_url

    @property
    def pay_now_text(self):
        """Gets the pay_now_text of this PaymentService.  # noqa: E501

        The text displayed on the Pay Now button in Xero Online Invoicing. If this is not set it will default to Pay by credit card  # noqa: E501

        :return: The pay_now_text of this PaymentService.  # noqa: E501
        :rtype: str
        """
        return self._pay_now_text

    @pay_now_text.setter
    def pay_now_text(self, pay_now_text):
        """Sets the pay_now_text of this PaymentService.

        The text displayed on the Pay Now button in Xero Online Invoicing. If this is not set it will default to Pay by credit card  # noqa: E501

        :param pay_now_text: The pay_now_text of this PaymentService.  # noqa: E501
        :type: str
        """

        self._pay_now_text = pay_now_text

    @property
    def payment_service_type(self):
        """Gets the payment_service_type of this PaymentService.  # noqa: E501

        This will always be CUSTOM for payment services created via the API.  # noqa: E501

        :return: The payment_service_type of this PaymentService.  # noqa: E501
        :rtype: str
        """
        return self._payment_service_type

    @payment_service_type.setter
    def payment_service_type(self, payment_service_type):
        """Sets the payment_service_type of this PaymentService.

        This will always be CUSTOM for payment services created via the API.  # noqa: E501

        :param payment_service_type: The payment_service_type of this PaymentService.  # noqa: E501
        :type: str
        """

        self._payment_service_type = payment_service_type

    @property
    def validation_errors(self):
        """Gets the validation_errors of this PaymentService.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this PaymentService.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this PaymentService.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this PaymentService.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors
