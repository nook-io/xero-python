# coding: utf-8

"""
    Xero Files API

    These endpoints are specific to Xero Files API  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class UploadObject(BaseModel):
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
        "body": "str",
        "name": "str",
        "filename": "str",
        "mime_type": "str",
    }

    attribute_map = {
        "body": "body",
        "name": "name",
        "filename": "filename",
        "mime_type": "mimeType",
    }

    def __init__(
        self, body=None, name=None, filename=None, mime_type=None
    ):  # noqa: E501
        """UploadObject - a model defined in OpenAPI"""  # noqa: E501

        self._body = None
        self._name = None
        self._filename = None
        self._mime_type = None
        self.discriminator = None

        self.body = body
        self.name = name
        self.filename = filename
        if mime_type is not None:
            self.mime_type = mime_type

    @property
    def body(self):
        """Gets the body of this UploadObject.  # noqa: E501


        :return: The body of this UploadObject.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UploadObject.


        :param body: The body of this UploadObject.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError(
                "Invalid value for `body`, must not be `None`"
            )  # noqa: E501

        self._body = body

    @property
    def name(self):
        """Gets the name of this UploadObject.  # noqa: E501

        exact name of the file you are uploading  # noqa: E501

        :return: The name of this UploadObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UploadObject.

        exact name of the file you are uploading  # noqa: E501

        :param name: The name of this UploadObject.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def filename(self):
        """Gets the filename of this UploadObject.  # noqa: E501


        :return: The filename of this UploadObject.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this UploadObject.


        :param filename: The filename of this UploadObject.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError(
                "Invalid value for `filename`, must not be `None`"
            )  # noqa: E501

        self._filename = filename

    @property
    def mime_type(self):
        """Gets the mime_type of this UploadObject.  # noqa: E501


        :return: The mime_type of this UploadObject.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this UploadObject.


        :param mime_type: The mime_type of this UploadObject.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type
