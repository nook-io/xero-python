# coding: utf-8

"""
    Xero Assets API

    The Assets API exposes fixed asset related functions of the Xero Accounting application and can be used for a variety of purposes such as creating assets, retrieving asset valuations etc.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class Error(BaseModel):
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
        "resource_validation_errors": "list[ResourceValidationErrorsElement]",
        "field_validation_errors": "list[FieldValidationErrorsElement]",
        "type": "str",
        "title": "str",
        "detail": "str",
    }

    attribute_map = {
        "resource_validation_errors": "resourceValidationErrors",
        "field_validation_errors": "fieldValidationErrors",
        "type": "type",
        "title": "title",
        "detail": "detail",
    }

    def __init__(
        self,
        resource_validation_errors=None,
        field_validation_errors=None,
        type=None,
        title=None,
        detail=None,
    ):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501

        self._resource_validation_errors = None
        self._field_validation_errors = None
        self._type = None
        self._title = None
        self._detail = None
        self.discriminator = None

        if resource_validation_errors is not None:
            self.resource_validation_errors = resource_validation_errors
        if field_validation_errors is not None:
            self.field_validation_errors = field_validation_errors
        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if detail is not None:
            self.detail = detail

    @property
    def resource_validation_errors(self):
        """Gets the resource_validation_errors of this Error.  # noqa: E501

        Array of elements of resource validation errors  # noqa: E501

        :return: The resource_validation_errors of this Error.  # noqa: E501
        :rtype: list[ResourceValidationErrorsElement]
        """
        return self._resource_validation_errors

    @resource_validation_errors.setter
    def resource_validation_errors(self, resource_validation_errors):
        """Sets the resource_validation_errors of this Error.

        Array of elements of resource validation errors  # noqa: E501

        :param resource_validation_errors: The resource_validation_errors of this Error.  # noqa: E501
        :type: list[ResourceValidationErrorsElement]
        """

        self._resource_validation_errors = resource_validation_errors

    @property
    def field_validation_errors(self):
        """Gets the field_validation_errors of this Error.  # noqa: E501

        Array of elements of field validation errors  # noqa: E501

        :return: The field_validation_errors of this Error.  # noqa: E501
        :rtype: list[FieldValidationErrorsElement]
        """
        return self._field_validation_errors

    @field_validation_errors.setter
    def field_validation_errors(self, field_validation_errors):
        """Sets the field_validation_errors of this Error.

        Array of elements of field validation errors  # noqa: E501

        :param field_validation_errors: The field_validation_errors of this Error.  # noqa: E501
        :type: list[FieldValidationErrorsElement]
        """

        self._field_validation_errors = field_validation_errors

    @property
    def type(self):
        """Gets the type of this Error.  # noqa: E501

        The internal type of error, not accessible externally  # noqa: E501

        :return: The type of this Error.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Error.

        The internal type of error, not accessible externally  # noqa: E501

        :param type: The type of this Error.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this Error.  # noqa: E501

        Title of the error  # noqa: E501

        :return: The title of this Error.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Error.

        Title of the error  # noqa: E501

        :param title: The title of this Error.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def detail(self):
        """Gets the detail of this Error.  # noqa: E501

        Detail of the error  # noqa: E501

        :return: The detail of this Error.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Error.

        Detail of the error  # noqa: E501

        :param detail: The detail of this Error.  # noqa: E501
        :type: str
        """

        self._detail = detail
