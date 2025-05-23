# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class PurchaseOrder(BaseModel):
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
        "contact": "Contact",
        "line_items": "list[LineItem]",
        "date": "date[ms-format]",
        "delivery_date": "date[ms-format]",
        "line_amount_types": "LineAmountTypes",
        "purchase_order_number": "str",
        "reference": "str",
        "branding_theme_id": "str",
        "currency_code": "CurrencyCode",
        "status": "str",
        "sent_to_contact": "bool",
        "delivery_address": "str",
        "attention_to": "str",
        "telephone": "str",
        "delivery_instructions": "str",
        "expected_arrival_date": "date[ms-format]",
        "purchase_order_id": "str",
        "currency_rate": "float",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "total_discount": "float",
        "has_attachments": "bool",
        "updated_date_utc": "datetime[ms-format]",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
        "warnings": "list[ValidationError]",
        "attachments": "list[Attachment]",
    }

    attribute_map = {
        "contact": "Contact",
        "line_items": "LineItems",
        "date": "Date",
        "delivery_date": "DeliveryDate",
        "line_amount_types": "LineAmountTypes",
        "purchase_order_number": "PurchaseOrderNumber",
        "reference": "Reference",
        "branding_theme_id": "BrandingThemeID",
        "currency_code": "CurrencyCode",
        "status": "Status",
        "sent_to_contact": "SentToContact",
        "delivery_address": "DeliveryAddress",
        "attention_to": "AttentionTo",
        "telephone": "Telephone",
        "delivery_instructions": "DeliveryInstructions",
        "expected_arrival_date": "ExpectedArrivalDate",
        "purchase_order_id": "PurchaseOrderID",
        "currency_rate": "CurrencyRate",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "total_discount": "TotalDiscount",
        "has_attachments": "HasAttachments",
        "updated_date_utc": "UpdatedDateUTC",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
        "warnings": "Warnings",
        "attachments": "Attachments",
    }

    def __init__(
        self,
        contact=None,
        line_items=None,
        date=None,
        delivery_date=None,
        line_amount_types=None,
        purchase_order_number=None,
        reference=None,
        branding_theme_id=None,
        currency_code=None,
        status=None,
        sent_to_contact=None,
        delivery_address=None,
        attention_to=None,
        telephone=None,
        delivery_instructions=None,
        expected_arrival_date=None,
        purchase_order_id=None,
        currency_rate=None,
        sub_total=None,
        total_tax=None,
        total=None,
        total_discount=None,
        has_attachments=False,
        updated_date_utc=None,
        status_attribute_string=None,
        validation_errors=None,
        warnings=None,
        attachments=None,
    ):  # noqa: E501
        """PurchaseOrder - a model defined in OpenAPI"""  # noqa: E501

        self._contact = None
        self._line_items = None
        self._date = None
        self._delivery_date = None
        self._line_amount_types = None
        self._purchase_order_number = None
        self._reference = None
        self._branding_theme_id = None
        self._currency_code = None
        self._status = None
        self._sent_to_contact = None
        self._delivery_address = None
        self._attention_to = None
        self._telephone = None
        self._delivery_instructions = None
        self._expected_arrival_date = None
        self._purchase_order_id = None
        self._currency_rate = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._total_discount = None
        self._has_attachments = None
        self._updated_date_utc = None
        self._status_attribute_string = None
        self._validation_errors = None
        self._warnings = None
        self._attachments = None
        self.discriminator = None

        if contact is not None:
            self.contact = contact
        if line_items is not None:
            self.line_items = line_items
        if date is not None:
            self.date = date
        if delivery_date is not None:
            self.delivery_date = delivery_date
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if reference is not None:
            self.reference = reference
        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if currency_code is not None:
            self.currency_code = currency_code
        if status is not None:
            self.status = status
        if sent_to_contact is not None:
            self.sent_to_contact = sent_to_contact
        if delivery_address is not None:
            self.delivery_address = delivery_address
        if attention_to is not None:
            self.attention_to = attention_to
        if telephone is not None:
            self.telephone = telephone
        if delivery_instructions is not None:
            self.delivery_instructions = delivery_instructions
        if expected_arrival_date is not None:
            self.expected_arrival_date = expected_arrival_date
        if purchase_order_id is not None:
            self.purchase_order_id = purchase_order_id
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if total_discount is not None:
            self.total_discount = total_discount
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if warnings is not None:
            self.warnings = warnings
        if attachments is not None:
            self.attachments = attachments

    @property
    def contact(self):
        """Gets the contact of this PurchaseOrder.  # noqa: E501


        :return: The contact of this PurchaseOrder.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this PurchaseOrder.


        :param contact: The contact of this PurchaseOrder.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def line_items(self):
        """Gets the line_items of this PurchaseOrder.  # noqa: E501

        See LineItems  # noqa: E501

        :return: The line_items of this PurchaseOrder.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this PurchaseOrder.

        See LineItems  # noqa: E501

        :param line_items: The line_items of this PurchaseOrder.  # noqa: E501
        :type: list[LineItem]
        """

        self._line_items = line_items

    @property
    def date(self):
        """Gets the date of this PurchaseOrder.  # noqa: E501

        Date purchase order was issued – YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation  # noqa: E501

        :return: The date of this PurchaseOrder.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this PurchaseOrder.

        Date purchase order was issued – YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation  # noqa: E501

        :param date: The date of this PurchaseOrder.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def delivery_date(self):
        """Gets the delivery_date of this PurchaseOrder.  # noqa: E501

        Date the goods are to be delivered – YYYY-MM-DD  # noqa: E501

        :return: The delivery_date of this PurchaseOrder.  # noqa: E501
        :rtype: date
        """
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        """Sets the delivery_date of this PurchaseOrder.

        Date the goods are to be delivered – YYYY-MM-DD  # noqa: E501

        :param delivery_date: The delivery_date of this PurchaseOrder.  # noqa: E501
        :type: date
        """

        self._delivery_date = delivery_date

    @property
    def line_amount_types(self):
        """Gets the line_amount_types of this PurchaseOrder.  # noqa: E501


        :return: The line_amount_types of this PurchaseOrder.  # noqa: E501
        :rtype: LineAmountTypes
        """
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        """Sets the line_amount_types of this PurchaseOrder.


        :param line_amount_types: The line_amount_types of this PurchaseOrder.  # noqa: E501
        :type: LineAmountTypes
        """

        self._line_amount_types = line_amount_types

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this PurchaseOrder.  # noqa: E501

        Unique alpha numeric code identifying purchase order (when missing will auto-generate from your Organisation Invoice Settings)  # noqa: E501

        :return: The purchase_order_number of this PurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this PurchaseOrder.

        Unique alpha numeric code identifying purchase order (when missing will auto-generate from your Organisation Invoice Settings)  # noqa: E501

        :param purchase_order_number: The purchase_order_number of this PurchaseOrder.  # noqa: E501
        :type: str
        """

        self._purchase_order_number = purchase_order_number

    @property
    def reference(self):
        """Gets the reference of this PurchaseOrder.  # noqa: E501

        Additional reference number  # noqa: E501

        :return: The reference of this PurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PurchaseOrder.

        Additional reference number  # noqa: E501

        :param reference: The reference of this PurchaseOrder.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def branding_theme_id(self):
        """Gets the branding_theme_id of this PurchaseOrder.  # noqa: E501

        See BrandingThemes  # noqa: E501

        :return: The branding_theme_id of this PurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._branding_theme_id

    @branding_theme_id.setter
    def branding_theme_id(self, branding_theme_id):
        """Sets the branding_theme_id of this PurchaseOrder.

        See BrandingThemes  # noqa: E501

        :param branding_theme_id: The branding_theme_id of this PurchaseOrder.  # noqa: E501
        :type: str
        """

        self._branding_theme_id = branding_theme_id

    @property
    def currency_code(self):
        """Gets the currency_code of this PurchaseOrder.  # noqa: E501


        :return: The currency_code of this PurchaseOrder.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this PurchaseOrder.


        :param currency_code: The currency_code of this PurchaseOrder.  # noqa: E501
        :type: CurrencyCode
        """

        self._currency_code = currency_code

    @property
    def status(self):
        """Gets the status of this PurchaseOrder.  # noqa: E501

        See Purchase Order Status Codes  # noqa: E501

        :return: The status of this PurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PurchaseOrder.

        See Purchase Order Status Codes  # noqa: E501

        :param status: The status of this PurchaseOrder.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "DRAFT",
            "SUBMITTED",
            "AUTHORISED",
            "BILLED",
            "DELETED",
            "None",
        ]  # noqa: E501

        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                        status, allowed_values
                    )
                )

        self._status = status

    @property
    def sent_to_contact(self):
        """Gets the sent_to_contact of this PurchaseOrder.  # noqa: E501

        Boolean to set whether the purchase order should be marked as “sent”. This can be set only on purchase orders that have been approved or billed  # noqa: E501

        :return: The sent_to_contact of this PurchaseOrder.  # noqa: E501
        :rtype: bool
        """
        return self._sent_to_contact

    @sent_to_contact.setter
    def sent_to_contact(self, sent_to_contact):
        """Sets the sent_to_contact of this PurchaseOrder.

        Boolean to set whether the purchase order should be marked as “sent”. This can be set only on purchase orders that have been approved or billed  # noqa: E501

        :param sent_to_contact: The sent_to_contact of this PurchaseOrder.  # noqa: E501
        :type: bool
        """

        self._sent_to_contact = sent_to_contact

    @property
    def delivery_address(self):
        """Gets the delivery_address of this PurchaseOrder.  # noqa: E501

        The address the goods are to be delivered to  # noqa: E501

        :return: The delivery_address of this PurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        """Sets the delivery_address of this PurchaseOrder.

        The address the goods are to be delivered to  # noqa: E501

        :param delivery_address: The delivery_address of this PurchaseOrder.  # noqa: E501
        :type: str
        """

        self._delivery_address = delivery_address

    @property
    def attention_to(self):
        """Gets the attention_to of this PurchaseOrder.  # noqa: E501

        The person that the delivery is going to  # noqa: E501

        :return: The attention_to of this PurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._attention_to

    @attention_to.setter
    def attention_to(self, attention_to):
        """Sets the attention_to of this PurchaseOrder.

        The person that the delivery is going to  # noqa: E501

        :param attention_to: The attention_to of this PurchaseOrder.  # noqa: E501
        :type: str
        """

        self._attention_to = attention_to

    @property
    def telephone(self):
        """Gets the telephone of this PurchaseOrder.  # noqa: E501

        The phone number for the person accepting the delivery  # noqa: E501

        :return: The telephone of this PurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this PurchaseOrder.

        The phone number for the person accepting the delivery  # noqa: E501

        :param telephone: The telephone of this PurchaseOrder.  # noqa: E501
        :type: str
        """

        self._telephone = telephone

    @property
    def delivery_instructions(self):
        """Gets the delivery_instructions of this PurchaseOrder.  # noqa: E501

        A free text feild for instructions (500 characters max)  # noqa: E501

        :return: The delivery_instructions of this PurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._delivery_instructions

    @delivery_instructions.setter
    def delivery_instructions(self, delivery_instructions):
        """Sets the delivery_instructions of this PurchaseOrder.

        A free text feild for instructions (500 characters max)  # noqa: E501

        :param delivery_instructions: The delivery_instructions of this PurchaseOrder.  # noqa: E501
        :type: str
        """

        self._delivery_instructions = delivery_instructions

    @property
    def expected_arrival_date(self):
        """Gets the expected_arrival_date of this PurchaseOrder.  # noqa: E501

        The date the goods are expected to arrive.  # noqa: E501

        :return: The expected_arrival_date of this PurchaseOrder.  # noqa: E501
        :rtype: date
        """
        return self._expected_arrival_date

    @expected_arrival_date.setter
    def expected_arrival_date(self, expected_arrival_date):
        """Sets the expected_arrival_date of this PurchaseOrder.

        The date the goods are expected to arrive.  # noqa: E501

        :param expected_arrival_date: The expected_arrival_date of this PurchaseOrder.  # noqa: E501
        :type: date
        """

        self._expected_arrival_date = expected_arrival_date

    @property
    def purchase_order_id(self):
        """Gets the purchase_order_id of this PurchaseOrder.  # noqa: E501

        Xero generated unique identifier for purchase order  # noqa: E501

        :return: The purchase_order_id of this PurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_id

    @purchase_order_id.setter
    def purchase_order_id(self, purchase_order_id):
        """Sets the purchase_order_id of this PurchaseOrder.

        Xero generated unique identifier for purchase order  # noqa: E501

        :param purchase_order_id: The purchase_order_id of this PurchaseOrder.  # noqa: E501
        :type: str
        """

        self._purchase_order_id = purchase_order_id

    @property
    def currency_rate(self):
        """Gets the currency_rate of this PurchaseOrder.  # noqa: E501

        The currency rate for a multicurrency purchase order. If no rate is specified, the XE.com day rate is used.  # noqa: E501

        :return: The currency_rate of this PurchaseOrder.  # noqa: E501
        :rtype: float
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this PurchaseOrder.

        The currency rate for a multicurrency purchase order. If no rate is specified, the XE.com day rate is used.  # noqa: E501

        :param currency_rate: The currency_rate of this PurchaseOrder.  # noqa: E501
        :type: float
        """

        self._currency_rate = currency_rate

    @property
    def sub_total(self):
        """Gets the sub_total of this PurchaseOrder.  # noqa: E501

        Total of purchase order excluding taxes  # noqa: E501

        :return: The sub_total of this PurchaseOrder.  # noqa: E501
        :rtype: float
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this PurchaseOrder.

        Total of purchase order excluding taxes  # noqa: E501

        :param sub_total: The sub_total of this PurchaseOrder.  # noqa: E501
        :type: float
        """

        self._sub_total = sub_total

    @property
    def total_tax(self):
        """Gets the total_tax of this PurchaseOrder.  # noqa: E501

        Total tax on purchase order  # noqa: E501

        :return: The total_tax of this PurchaseOrder.  # noqa: E501
        :rtype: float
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """Sets the total_tax of this PurchaseOrder.

        Total tax on purchase order  # noqa: E501

        :param total_tax: The total_tax of this PurchaseOrder.  # noqa: E501
        :type: float
        """

        self._total_tax = total_tax

    @property
    def total(self):
        """Gets the total of this PurchaseOrder.  # noqa: E501

        Total of Purchase Order tax inclusive (i.e. SubTotal + TotalTax)  # noqa: E501

        :return: The total of this PurchaseOrder.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PurchaseOrder.

        Total of Purchase Order tax inclusive (i.e. SubTotal + TotalTax)  # noqa: E501

        :param total: The total of this PurchaseOrder.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def total_discount(self):
        """Gets the total_discount of this PurchaseOrder.  # noqa: E501

        Total of discounts applied on the purchase order line items  # noqa: E501

        :return: The total_discount of this PurchaseOrder.  # noqa: E501
        :rtype: float
        """
        return self._total_discount

    @total_discount.setter
    def total_discount(self, total_discount):
        """Sets the total_discount of this PurchaseOrder.

        Total of discounts applied on the purchase order line items  # noqa: E501

        :param total_discount: The total_discount of this PurchaseOrder.  # noqa: E501
        :type: float
        """

        self._total_discount = total_discount

    @property
    def has_attachments(self):
        """Gets the has_attachments of this PurchaseOrder.  # noqa: E501

        boolean to indicate if a purchase order has an attachment  # noqa: E501

        :return: The has_attachments of this PurchaseOrder.  # noqa: E501
        :rtype: bool
        """
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        """Sets the has_attachments of this PurchaseOrder.

        boolean to indicate if a purchase order has an attachment  # noqa: E501

        :param has_attachments: The has_attachments of this PurchaseOrder.  # noqa: E501
        :type: bool
        """

        self._has_attachments = has_attachments

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this PurchaseOrder.  # noqa: E501

        Last modified date UTC format  # noqa: E501

        :return: The updated_date_utc of this PurchaseOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this PurchaseOrder.

        Last modified date UTC format  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this PurchaseOrder.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def status_attribute_string(self):
        """Gets the status_attribute_string of this PurchaseOrder.  # noqa: E501

        A string to indicate if a invoice status  # noqa: E501

        :return: The status_attribute_string of this PurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        """Sets the status_attribute_string of this PurchaseOrder.

        A string to indicate if a invoice status  # noqa: E501

        :param status_attribute_string: The status_attribute_string of this PurchaseOrder.  # noqa: E501
        :type: str
        """

        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        """Gets the validation_errors of this PurchaseOrder.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this PurchaseOrder.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this PurchaseOrder.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this PurchaseOrder.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors

    @property
    def warnings(self):
        """Gets the warnings of this PurchaseOrder.  # noqa: E501

        Displays array of warning messages from the API  # noqa: E501

        :return: The warnings of this PurchaseOrder.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this PurchaseOrder.

        Displays array of warning messages from the API  # noqa: E501

        :param warnings: The warnings of this PurchaseOrder.  # noqa: E501
        :type: list[ValidationError]
        """

        self._warnings = warnings

    @property
    def attachments(self):
        """Gets the attachments of this PurchaseOrder.  # noqa: E501

        Displays array of attachments from the API  # noqa: E501

        :return: The attachments of this PurchaseOrder.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this PurchaseOrder.

        Displays array of attachments from the API  # noqa: E501

        :param attachments: The attachments of this PurchaseOrder.  # noqa: E501
        :type: list[Attachment]
        """

        self._attachments = attachments
