# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class CreditNote(BaseModel):
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
        "type": "str",
        "contact": "Contact",
        "date": "date[ms-format]",
        "due_date": "date[ms-format]",
        "status": "str",
        "line_amount_types": "LineAmountTypes",
        "line_items": "list[LineItem]",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "cis_deduction": "float",
        "cis_rate": "float",
        "updated_date_utc": "datetime[ms-format]",
        "currency_code": "CurrencyCode",
        "fully_paid_on_date": "date[ms-format]",
        "credit_note_id": "str",
        "credit_note_number": "str",
        "reference": "str",
        "sent_to_contact": "bool",
        "currency_rate": "float",
        "remaining_credit": "float",
        "allocations": "list[Allocation]",
        "applied_amount": "float",
        "payments": "list[Payment]",
        "branding_theme_id": "str",
        "status_attribute_string": "str",
        "has_attachments": "bool",
        "has_errors": "bool",
        "validation_errors": "list[ValidationError]",
        "warnings": "list[ValidationError]",
        "invoice_addresses": "list[InvoiceAddress]",
    }

    attribute_map = {
        "type": "Type",
        "contact": "Contact",
        "date": "Date",
        "due_date": "DueDate",
        "status": "Status",
        "line_amount_types": "LineAmountTypes",
        "line_items": "LineItems",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "cis_deduction": "CISDeduction",
        "cis_rate": "CISRate",
        "updated_date_utc": "UpdatedDateUTC",
        "currency_code": "CurrencyCode",
        "fully_paid_on_date": "FullyPaidOnDate",
        "credit_note_id": "CreditNoteID",
        "credit_note_number": "CreditNoteNumber",
        "reference": "Reference",
        "sent_to_contact": "SentToContact",
        "currency_rate": "CurrencyRate",
        "remaining_credit": "RemainingCredit",
        "allocations": "Allocations",
        "applied_amount": "AppliedAmount",
        "payments": "Payments",
        "branding_theme_id": "BrandingThemeID",
        "status_attribute_string": "StatusAttributeString",
        "has_attachments": "HasAttachments",
        "has_errors": "HasErrors",
        "validation_errors": "ValidationErrors",
        "warnings": "Warnings",
        "invoice_addresses": "InvoiceAddresses",
    }

    def __init__(
        self,
        type=None,
        contact=None,
        date=None,
        due_date=None,
        status=None,
        line_amount_types=None,
        line_items=None,
        sub_total=None,
        total_tax=None,
        total=None,
        cis_deduction=None,
        cis_rate=None,
        updated_date_utc=None,
        currency_code=None,
        fully_paid_on_date=None,
        credit_note_id=None,
        credit_note_number=None,
        reference=None,
        sent_to_contact=None,
        currency_rate=None,
        remaining_credit=None,
        allocations=None,
        applied_amount=None,
        payments=None,
        branding_theme_id=None,
        status_attribute_string=None,
        has_attachments=False,
        has_errors=False,
        validation_errors=None,
        warnings=None,
        invoice_addresses=None,
    ):  # noqa: E501
        """CreditNote - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._contact = None
        self._date = None
        self._due_date = None
        self._status = None
        self._line_amount_types = None
        self._line_items = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._cis_deduction = None
        self._cis_rate = None
        self._updated_date_utc = None
        self._currency_code = None
        self._fully_paid_on_date = None
        self._credit_note_id = None
        self._credit_note_number = None
        self._reference = None
        self._sent_to_contact = None
        self._currency_rate = None
        self._remaining_credit = None
        self._allocations = None
        self._applied_amount = None
        self._payments = None
        self._branding_theme_id = None
        self._status_attribute_string = None
        self._has_attachments = None
        self._has_errors = None
        self._validation_errors = None
        self._warnings = None
        self._invoice_addresses = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if contact is not None:
            self.contact = contact
        if date is not None:
            self.date = date
        if due_date is not None:
            self.due_date = due_date
        if status is not None:
            self.status = status
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if line_items is not None:
            self.line_items = line_items
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if cis_deduction is not None:
            self.cis_deduction = cis_deduction
        if cis_rate is not None:
            self.cis_rate = cis_rate
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if currency_code is not None:
            self.currency_code = currency_code
        if fully_paid_on_date is not None:
            self.fully_paid_on_date = fully_paid_on_date
        if credit_note_id is not None:
            self.credit_note_id = credit_note_id
        if credit_note_number is not None:
            self.credit_note_number = credit_note_number
        if reference is not None:
            self.reference = reference
        if sent_to_contact is not None:
            self.sent_to_contact = sent_to_contact
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if remaining_credit is not None:
            self.remaining_credit = remaining_credit
        if allocations is not None:
            self.allocations = allocations
        if applied_amount is not None:
            self.applied_amount = applied_amount
        if payments is not None:
            self.payments = payments
        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if has_errors is not None:
            self.has_errors = has_errors
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if warnings is not None:
            self.warnings = warnings
        if invoice_addresses is not None:
            self.invoice_addresses = invoice_addresses

    @property
    def type(self):
        """Gets the type of this CreditNote.  # noqa: E501

        See Credit Note Types  # noqa: E501

        :return: The type of this CreditNote.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreditNote.

        See Credit Note Types  # noqa: E501

        :param type: The type of this CreditNote.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCPAYCREDIT", "ACCRECCREDIT", "None"]  # noqa: E501

        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                        type, allowed_values
                    )
                )

        self._type = type

    @property
    def contact(self):
        """Gets the contact of this CreditNote.  # noqa: E501


        :return: The contact of this CreditNote.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this CreditNote.


        :param contact: The contact of this CreditNote.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def date(self):
        """Gets the date of this CreditNote.  # noqa: E501

        The date the credit note is issued YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation  # noqa: E501

        :return: The date of this CreditNote.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this CreditNote.

        The date the credit note is issued YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation  # noqa: E501

        :param date: The date of this CreditNote.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def due_date(self):
        """Gets the due_date of this CreditNote.  # noqa: E501

        Date invoice is due – YYYY-MM-DD  # noqa: E501

        :return: The due_date of this CreditNote.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this CreditNote.

        Date invoice is due – YYYY-MM-DD  # noqa: E501

        :param due_date: The due_date of this CreditNote.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def status(self):
        """Gets the status of this CreditNote.  # noqa: E501

        See Credit Note Status Codes  # noqa: E501

        :return: The status of this CreditNote.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreditNote.

        See Credit Note Status Codes  # noqa: E501

        :param status: The status of this CreditNote.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "DRAFT",
            "SUBMITTED",
            "DELETED",
            "AUTHORISED",
            "PAID",
            "VOIDED",
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
    def line_amount_types(self):
        """Gets the line_amount_types of this CreditNote.  # noqa: E501


        :return: The line_amount_types of this CreditNote.  # noqa: E501
        :rtype: LineAmountTypes
        """
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        """Sets the line_amount_types of this CreditNote.


        :param line_amount_types: The line_amount_types of this CreditNote.  # noqa: E501
        :type: LineAmountTypes
        """

        self._line_amount_types = line_amount_types

    @property
    def line_items(self):
        """Gets the line_items of this CreditNote.  # noqa: E501

        See Invoice Line Items  # noqa: E501

        :return: The line_items of this CreditNote.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this CreditNote.

        See Invoice Line Items  # noqa: E501

        :param line_items: The line_items of this CreditNote.  # noqa: E501
        :type: list[LineItem]
        """

        self._line_items = line_items

    @property
    def sub_total(self):
        """Gets the sub_total of this CreditNote.  # noqa: E501

        The subtotal of the credit note excluding taxes  # noqa: E501

        :return: The sub_total of this CreditNote.  # noqa: E501
        :rtype: float
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this CreditNote.

        The subtotal of the credit note excluding taxes  # noqa: E501

        :param sub_total: The sub_total of this CreditNote.  # noqa: E501
        :type: float
        """

        self._sub_total = sub_total

    @property
    def total_tax(self):
        """Gets the total_tax of this CreditNote.  # noqa: E501

        The total tax on the credit note  # noqa: E501

        :return: The total_tax of this CreditNote.  # noqa: E501
        :rtype: float
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """Sets the total_tax of this CreditNote.

        The total tax on the credit note  # noqa: E501

        :param total_tax: The total_tax of this CreditNote.  # noqa: E501
        :type: float
        """

        self._total_tax = total_tax

    @property
    def total(self):
        """Gets the total of this CreditNote.  # noqa: E501

        The total of the Credit Note(subtotal + total tax)  # noqa: E501

        :return: The total of this CreditNote.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CreditNote.

        The total of the Credit Note(subtotal + total tax)  # noqa: E501

        :param total: The total of this CreditNote.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def cis_deduction(self):
        """Gets the cis_deduction of this CreditNote.  # noqa: E501

        CIS deduction for UK contractors  # noqa: E501

        :return: The cis_deduction of this CreditNote.  # noqa: E501
        :rtype: float
        """
        return self._cis_deduction

    @cis_deduction.setter
    def cis_deduction(self, cis_deduction):
        """Sets the cis_deduction of this CreditNote.

        CIS deduction for UK contractors  # noqa: E501

        :param cis_deduction: The cis_deduction of this CreditNote.  # noqa: E501
        :type: float
        """

        self._cis_deduction = cis_deduction

    @property
    def cis_rate(self):
        """Gets the cis_rate of this CreditNote.  # noqa: E501

        CIS Deduction rate for the organisation  # noqa: E501

        :return: The cis_rate of this CreditNote.  # noqa: E501
        :rtype: float
        """
        return self._cis_rate

    @cis_rate.setter
    def cis_rate(self, cis_rate):
        """Sets the cis_rate of this CreditNote.

        CIS Deduction rate for the organisation  # noqa: E501

        :param cis_rate: The cis_rate of this CreditNote.  # noqa: E501
        :type: float
        """

        self._cis_rate = cis_rate

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this CreditNote.  # noqa: E501

        UTC timestamp of last update to the credit note  # noqa: E501

        :return: The updated_date_utc of this CreditNote.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this CreditNote.

        UTC timestamp of last update to the credit note  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this CreditNote.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def currency_code(self):
        """Gets the currency_code of this CreditNote.  # noqa: E501


        :return: The currency_code of this CreditNote.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CreditNote.


        :param currency_code: The currency_code of this CreditNote.  # noqa: E501
        :type: CurrencyCode
        """

        self._currency_code = currency_code

    @property
    def fully_paid_on_date(self):
        """Gets the fully_paid_on_date of this CreditNote.  # noqa: E501

        Date when credit note was fully paid(UTC format)  # noqa: E501

        :return: The fully_paid_on_date of this CreditNote.  # noqa: E501
        :rtype: date
        """
        return self._fully_paid_on_date

    @fully_paid_on_date.setter
    def fully_paid_on_date(self, fully_paid_on_date):
        """Sets the fully_paid_on_date of this CreditNote.

        Date when credit note was fully paid(UTC format)  # noqa: E501

        :param fully_paid_on_date: The fully_paid_on_date of this CreditNote.  # noqa: E501
        :type: date
        """

        self._fully_paid_on_date = fully_paid_on_date

    @property
    def credit_note_id(self):
        """Gets the credit_note_id of this CreditNote.  # noqa: E501

        Xero generated unique identifier  # noqa: E501

        :return: The credit_note_id of this CreditNote.  # noqa: E501
        :rtype: str
        """
        return self._credit_note_id

    @credit_note_id.setter
    def credit_note_id(self, credit_note_id):
        """Sets the credit_note_id of this CreditNote.

        Xero generated unique identifier  # noqa: E501

        :param credit_note_id: The credit_note_id of this CreditNote.  # noqa: E501
        :type: str
        """

        self._credit_note_id = credit_note_id

    @property
    def credit_note_number(self):
        """Gets the credit_note_number of this CreditNote.  # noqa: E501

        ACCRECCREDIT – Unique alpha numeric code identifying credit note (when missing will auto-generate from your Organisation Invoice Settings)  # noqa: E501

        :return: The credit_note_number of this CreditNote.  # noqa: E501
        :rtype: str
        """
        return self._credit_note_number

    @credit_note_number.setter
    def credit_note_number(self, credit_note_number):
        """Sets the credit_note_number of this CreditNote.

        ACCRECCREDIT – Unique alpha numeric code identifying credit note (when missing will auto-generate from your Organisation Invoice Settings)  # noqa: E501

        :param credit_note_number: The credit_note_number of this CreditNote.  # noqa: E501
        :type: str
        """

        self._credit_note_number = credit_note_number

    @property
    def reference(self):
        """Gets the reference of this CreditNote.  # noqa: E501

        ACCRECCREDIT only – additional reference number  # noqa: E501

        :return: The reference of this CreditNote.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this CreditNote.

        ACCRECCREDIT only – additional reference number  # noqa: E501

        :param reference: The reference of this CreditNote.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def sent_to_contact(self):
        """Gets the sent_to_contact of this CreditNote.  # noqa: E501

        Boolean to set whether the credit note in the Xero app should be marked as “sent”. This can be set only on credit notes that have been approved  # noqa: E501

        :return: The sent_to_contact of this CreditNote.  # noqa: E501
        :rtype: bool
        """
        return self._sent_to_contact

    @sent_to_contact.setter
    def sent_to_contact(self, sent_to_contact):
        """Sets the sent_to_contact of this CreditNote.

        Boolean to set whether the credit note in the Xero app should be marked as “sent”. This can be set only on credit notes that have been approved  # noqa: E501

        :param sent_to_contact: The sent_to_contact of this CreditNote.  # noqa: E501
        :type: bool
        """

        self._sent_to_contact = sent_to_contact

    @property
    def currency_rate(self):
        """Gets the currency_rate of this CreditNote.  # noqa: E501

        The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used  # noqa: E501

        :return: The currency_rate of this CreditNote.  # noqa: E501
        :rtype: float
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this CreditNote.

        The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used  # noqa: E501

        :param currency_rate: The currency_rate of this CreditNote.  # noqa: E501
        :type: float
        """

        self._currency_rate = currency_rate

    @property
    def remaining_credit(self):
        """Gets the remaining_credit of this CreditNote.  # noqa: E501

        The remaining credit balance on the Credit Note  # noqa: E501

        :return: The remaining_credit of this CreditNote.  # noqa: E501
        :rtype: float
        """
        return self._remaining_credit

    @remaining_credit.setter
    def remaining_credit(self, remaining_credit):
        """Sets the remaining_credit of this CreditNote.

        The remaining credit balance on the Credit Note  # noqa: E501

        :param remaining_credit: The remaining_credit of this CreditNote.  # noqa: E501
        :type: float
        """

        self._remaining_credit = remaining_credit

    @property
    def allocations(self):
        """Gets the allocations of this CreditNote.  # noqa: E501

        See Allocations  # noqa: E501

        :return: The allocations of this CreditNote.  # noqa: E501
        :rtype: list[Allocation]
        """
        return self._allocations

    @allocations.setter
    def allocations(self, allocations):
        """Sets the allocations of this CreditNote.

        See Allocations  # noqa: E501

        :param allocations: The allocations of this CreditNote.  # noqa: E501
        :type: list[Allocation]
        """

        self._allocations = allocations

    @property
    def applied_amount(self):
        """Gets the applied_amount of this CreditNote.  # noqa: E501

        The amount of applied to an invoice  # noqa: E501

        :return: The applied_amount of this CreditNote.  # noqa: E501
        :rtype: float
        """
        return self._applied_amount

    @applied_amount.setter
    def applied_amount(self, applied_amount):
        """Sets the applied_amount of this CreditNote.

        The amount of applied to an invoice  # noqa: E501

        :param applied_amount: The applied_amount of this CreditNote.  # noqa: E501
        :type: float
        """

        self._applied_amount = applied_amount

    @property
    def payments(self):
        """Gets the payments of this CreditNote.  # noqa: E501

        See Payments  # noqa: E501

        :return: The payments of this CreditNote.  # noqa: E501
        :rtype: list[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this CreditNote.

        See Payments  # noqa: E501

        :param payments: The payments of this CreditNote.  # noqa: E501
        :type: list[Payment]
        """

        self._payments = payments

    @property
    def branding_theme_id(self):
        """Gets the branding_theme_id of this CreditNote.  # noqa: E501

        See BrandingThemes  # noqa: E501

        :return: The branding_theme_id of this CreditNote.  # noqa: E501
        :rtype: str
        """
        return self._branding_theme_id

    @branding_theme_id.setter
    def branding_theme_id(self, branding_theme_id):
        """Sets the branding_theme_id of this CreditNote.

        See BrandingThemes  # noqa: E501

        :param branding_theme_id: The branding_theme_id of this CreditNote.  # noqa: E501
        :type: str
        """

        self._branding_theme_id = branding_theme_id

    @property
    def status_attribute_string(self):
        """Gets the status_attribute_string of this CreditNote.  # noqa: E501

        A string to indicate if a invoice status  # noqa: E501

        :return: The status_attribute_string of this CreditNote.  # noqa: E501
        :rtype: str
        """
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        """Sets the status_attribute_string of this CreditNote.

        A string to indicate if a invoice status  # noqa: E501

        :param status_attribute_string: The status_attribute_string of this CreditNote.  # noqa: E501
        :type: str
        """

        self._status_attribute_string = status_attribute_string

    @property
    def has_attachments(self):
        """Gets the has_attachments of this CreditNote.  # noqa: E501

        boolean to indicate if a credit note has an attachment  # noqa: E501

        :return: The has_attachments of this CreditNote.  # noqa: E501
        :rtype: bool
        """
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        """Sets the has_attachments of this CreditNote.

        boolean to indicate if a credit note has an attachment  # noqa: E501

        :param has_attachments: The has_attachments of this CreditNote.  # noqa: E501
        :type: bool
        """

        self._has_attachments = has_attachments

    @property
    def has_errors(self):
        """Gets the has_errors of this CreditNote.  # noqa: E501

        A boolean to indicate if a credit note has an validation errors  # noqa: E501

        :return: The has_errors of this CreditNote.  # noqa: E501
        :rtype: bool
        """
        return self._has_errors

    @has_errors.setter
    def has_errors(self, has_errors):
        """Sets the has_errors of this CreditNote.

        A boolean to indicate if a credit note has an validation errors  # noqa: E501

        :param has_errors: The has_errors of this CreditNote.  # noqa: E501
        :type: bool
        """

        self._has_errors = has_errors

    @property
    def validation_errors(self):
        """Gets the validation_errors of this CreditNote.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this CreditNote.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this CreditNote.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this CreditNote.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors

    @property
    def warnings(self):
        """Gets the warnings of this CreditNote.  # noqa: E501

        Displays array of warning messages from the API  # noqa: E501

        :return: The warnings of this CreditNote.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this CreditNote.

        Displays array of warning messages from the API  # noqa: E501

        :param warnings: The warnings of this CreditNote.  # noqa: E501
        :type: list[ValidationError]
        """

        self._warnings = warnings

    @property
    def invoice_addresses(self):
        """Gets the invoice_addresses of this CreditNote.  # noqa: E501

        An array of addresses used to auto calculate sales tax  # noqa: E501

        :return: The invoice_addresses of this CreditNote.  # noqa: E501
        :rtype: list[InvoiceAddress]
        """
        return self._invoice_addresses

    @invoice_addresses.setter
    def invoice_addresses(self, invoice_addresses):
        """Sets the invoice_addresses of this CreditNote.

        An array of addresses used to auto calculate sales tax  # noqa: E501

        :param invoice_addresses: The invoice_addresses of this CreditNote.  # noqa: E501
        :type: list[InvoiceAddress]
        """

        self._invoice_addresses = invoice_addresses
