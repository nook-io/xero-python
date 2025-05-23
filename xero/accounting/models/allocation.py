# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class Allocation(BaseModel):
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
        "allocation_id": "str",
        "invoice": "Invoice",
        "overpayment": "Overpayment",
        "prepayment": "Prepayment",
        "credit_note": "CreditNote",
        "amount": "float",
        "date": "date[ms-format]",
        "is_deleted": "bool",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
    }

    attribute_map = {
        "allocation_id": "AllocationID",
        "invoice": "Invoice",
        "overpayment": "Overpayment",
        "prepayment": "Prepayment",
        "credit_note": "CreditNote",
        "amount": "Amount",
        "date": "Date",
        "is_deleted": "IsDeleted",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        allocation_id=None,
        invoice=None,
        overpayment=None,
        prepayment=None,
        credit_note=None,
        amount=None,
        date=None,
        is_deleted=None,
        status_attribute_string=None,
        validation_errors=None,
    ):  # noqa: E501
        """Allocation - a model defined in OpenAPI"""  # noqa: E501

        self._allocation_id = None
        self._invoice = None
        self._overpayment = None
        self._prepayment = None
        self._credit_note = None
        self._amount = None
        self._date = None
        self._is_deleted = None
        self._status_attribute_string = None
        self._validation_errors = None
        self.discriminator = None

        if allocation_id is not None:
            self.allocation_id = allocation_id
        self.invoice = invoice
        if overpayment is not None:
            self.overpayment = overpayment
        if prepayment is not None:
            self.prepayment = prepayment
        if credit_note is not None:
            self.credit_note = credit_note
        self.amount = amount
        self.date = date
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def allocation_id(self):
        """Gets the allocation_id of this Allocation.  # noqa: E501

        Xero generated unique identifier  # noqa: E501

        :return: The allocation_id of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._allocation_id

    @allocation_id.setter
    def allocation_id(self, allocation_id):
        """Sets the allocation_id of this Allocation.

        Xero generated unique identifier  # noqa: E501

        :param allocation_id: The allocation_id of this Allocation.  # noqa: E501
        :type: str
        """

        self._allocation_id = allocation_id

    @property
    def invoice(self):
        """Gets the invoice of this Allocation.  # noqa: E501


        :return: The invoice of this Allocation.  # noqa: E501
        :rtype: Invoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this Allocation.


        :param invoice: The invoice of this Allocation.  # noqa: E501
        :type: Invoice
        """
        if invoice is None:
            raise ValueError(
                "Invalid value for `invoice`, must not be `None`"
            )  # noqa: E501

        self._invoice = invoice

    @property
    def overpayment(self):
        """Gets the overpayment of this Allocation.  # noqa: E501


        :return: The overpayment of this Allocation.  # noqa: E501
        :rtype: Overpayment
        """
        return self._overpayment

    @overpayment.setter
    def overpayment(self, overpayment):
        """Sets the overpayment of this Allocation.


        :param overpayment: The overpayment of this Allocation.  # noqa: E501
        :type: Overpayment
        """

        self._overpayment = overpayment

    @property
    def prepayment(self):
        """Gets the prepayment of this Allocation.  # noqa: E501


        :return: The prepayment of this Allocation.  # noqa: E501
        :rtype: Prepayment
        """
        return self._prepayment

    @prepayment.setter
    def prepayment(self, prepayment):
        """Sets the prepayment of this Allocation.


        :param prepayment: The prepayment of this Allocation.  # noqa: E501
        :type: Prepayment
        """

        self._prepayment = prepayment

    @property
    def credit_note(self):
        """Gets the credit_note of this Allocation.  # noqa: E501


        :return: The credit_note of this Allocation.  # noqa: E501
        :rtype: CreditNote
        """
        return self._credit_note

    @credit_note.setter
    def credit_note(self, credit_note):
        """Sets the credit_note of this Allocation.


        :param credit_note: The credit_note of this Allocation.  # noqa: E501
        :type: CreditNote
        """

        self._credit_note = credit_note

    @property
    def amount(self):
        """Gets the amount of this Allocation.  # noqa: E501

        the amount being applied to the invoice  # noqa: E501

        :return: The amount of this Allocation.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Allocation.

        the amount being applied to the invoice  # noqa: E501

        :param amount: The amount of this Allocation.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError(
                "Invalid value for `amount`, must not be `None`"
            )  # noqa: E501

        self._amount = amount

    @property
    def date(self):
        """Gets the date of this Allocation.  # noqa: E501

        the date the allocation is applied YYYY-MM-DD.  # noqa: E501

        :return: The date of this Allocation.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Allocation.

        the date the allocation is applied YYYY-MM-DD.  # noqa: E501

        :param date: The date of this Allocation.  # noqa: E501
        :type: date
        """
        if date is None:
            raise ValueError(
                "Invalid value for `date`, must not be `None`"
            )  # noqa: E501

        self._date = date

    @property
    def is_deleted(self):
        """Gets the is_deleted of this Allocation.  # noqa: E501

        A flag that returns true when the allocation is succesfully deleted  # noqa: E501

        :return: The is_deleted of this Allocation.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this Allocation.

        A flag that returns true when the allocation is succesfully deleted  # noqa: E501

        :param is_deleted: The is_deleted of this Allocation.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def status_attribute_string(self):
        """Gets the status_attribute_string of this Allocation.  # noqa: E501

        A string to indicate if a invoice status  # noqa: E501

        :return: The status_attribute_string of this Allocation.  # noqa: E501
        :rtype: str
        """
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        """Sets the status_attribute_string of this Allocation.

        A string to indicate if a invoice status  # noqa: E501

        :param status_attribute_string: The status_attribute_string of this Allocation.  # noqa: E501
        :type: str
        """

        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        """Gets the validation_errors of this Allocation.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this Allocation.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this Allocation.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this Allocation.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors
