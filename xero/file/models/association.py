# coding: utf-8

"""
    Xero Files API

    These endpoints are specific to Xero Files API  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class Association(BaseModel):
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
        "send_with_object": "bool",
        "name": "str",
        "size": "int",
        "file_id": "str",
        "object_id": "str",
        "object_group": "ObjectGroup",
        "object_type": "ObjectType",
    }

    attribute_map = {
        "send_with_object": "SendWithObject",
        "name": "Name",
        "size": "Size",
        "file_id": "FileId",
        "object_id": "ObjectId",
        "object_group": "ObjectGroup",
        "object_type": "ObjectType",
    }

    def __init__(
        self,
        send_with_object=None,
        name=None,
        size=None,
        file_id=None,
        object_id=None,
        object_group=None,
        object_type=None,
    ):  # noqa: E501
        """Association - a model defined in OpenAPI"""  # noqa: E501

        self._send_with_object = None
        self._name = None
        self._size = None
        self._file_id = None
        self._object_id = None
        self._object_group = None
        self._object_type = None
        self.discriminator = None

        if send_with_object is not None:
            self.send_with_object = send_with_object
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if file_id is not None:
            self.file_id = file_id
        if object_id is not None:
            self.object_id = object_id
        if object_group is not None:
            self.object_group = object_group
        if object_type is not None:
            self.object_type = object_type

    @property
    def send_with_object(self):
        """Gets the send_with_object of this Association.  # noqa: E501

        Boolean flag to determines whether the file is sent with the document it is attached to on client facing communications. Note- The SendWithObject element is only returned when using /Associations/{ObjectId} endpoint.  # noqa: E501

        :return: The send_with_object of this Association.  # noqa: E501
        :rtype: bool
        """
        return self._send_with_object

    @send_with_object.setter
    def send_with_object(self, send_with_object):
        """Sets the send_with_object of this Association.

        Boolean flag to determines whether the file is sent with the document it is attached to on client facing communications. Note- The SendWithObject element is only returned when using /Associations/{ObjectId} endpoint.  # noqa: E501

        :param send_with_object: The send_with_object of this Association.  # noqa: E501
        :type: bool
        """

        self._send_with_object = send_with_object

    @property
    def name(self):
        """Gets the name of this Association.  # noqa: E501

        The name of the associated file. Note- The Name element is only returned when using /Associations/{ObjectId} endpoint.  # noqa: E501

        :return: The name of this Association.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Association.

        The name of the associated file. Note- The Name element is only returned when using /Associations/{ObjectId} endpoint.  # noqa: E501

        :param name: The name of this Association.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this Association.  # noqa: E501

        The size of the associated file in bytes. Note- The Size element is only returned when using /Associations/{ObjectId} endpoint.  # noqa: E501

        :return: The size of this Association.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Association.

        The size of the associated file in bytes. Note- The Size element is only returned when using /Associations/{ObjectId} endpoint.  # noqa: E501

        :param size: The size of this Association.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def file_id(self):
        """Gets the file_id of this Association.  # noqa: E501

        The unique identifier of the file  # noqa: E501

        :return: The file_id of this Association.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this Association.

        The unique identifier of the file  # noqa: E501

        :param file_id: The file_id of this Association.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def object_id(self):
        """Gets the object_id of this Association.  # noqa: E501

        The identifier of the object that the file is being associated with (e.g. InvoiceID, BankTransactionID, ContactID)  # noqa: E501

        :return: The object_id of this Association.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this Association.

        The identifier of the object that the file is being associated with (e.g. InvoiceID, BankTransactionID, ContactID)  # noqa: E501

        :param object_id: The object_id of this Association.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def object_group(self):
        """Gets the object_group of this Association.  # noqa: E501


        :return: The object_group of this Association.  # noqa: E501
        :rtype: ObjectGroup
        """
        return self._object_group

    @object_group.setter
    def object_group(self, object_group):
        """Sets the object_group of this Association.


        :param object_group: The object_group of this Association.  # noqa: E501
        :type: ObjectGroup
        """

        self._object_group = object_group

    @property
    def object_type(self):
        """Gets the object_type of this Association.  # noqa: E501


        :return: The object_type of this Association.  # noqa: E501
        :rtype: ObjectType
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this Association.


        :param object_type: The object_type of this Association.  # noqa: E501
        :type: ObjectType
        """

        self._object_type = object_type
