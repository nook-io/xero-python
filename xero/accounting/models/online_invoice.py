# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class OnlineInvoice(BaseModel):
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
    openapi_types = {"online_invoice_url": "str"}

    attribute_map = {"online_invoice_url": "OnlineInvoiceUrl"}

    def __init__(self, online_invoice_url=None):  # noqa: E501
        """OnlineInvoice - a model defined in OpenAPI"""  # noqa: E501

        self._online_invoice_url = None
        self.discriminator = None

        if online_invoice_url is not None:
            self.online_invoice_url = online_invoice_url

    @property
    def online_invoice_url(self):
        """Gets the online_invoice_url of this OnlineInvoice.  # noqa: E501

        the URL to an online invoice  # noqa: E501

        :return: The online_invoice_url of this OnlineInvoice.  # noqa: E501
        :rtype: str
        """
        return self._online_invoice_url

    @online_invoice_url.setter
    def online_invoice_url(self, online_invoice_url):
        """Sets the online_invoice_url of this OnlineInvoice.

        the URL to an online invoice  # noqa: E501

        :param online_invoice_url: The online_invoice_url of this OnlineInvoice.  # noqa: E501
        :type: str
        """

        self._online_invoice_url = online_invoice_url
