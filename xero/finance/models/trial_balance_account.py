# coding: utf-8

"""
    Xero Finance API

    The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class TrialBalanceAccount(BaseModel):
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
        "account_id": "str",
        "account_type": "str",
        "account_code": "str",
        "account_class": "str",
        "status": "str",
        "reporting_code": "str",
        "account_name": "str",
        "balance": "TrialBalanceEntry",
        "signed_balance": "float",
        "account_movement": "TrialBalanceMovement",
    }

    attribute_map = {
        "account_id": "accountId",
        "account_type": "accountType",
        "account_code": "accountCode",
        "account_class": "accountClass",
        "status": "status",
        "reporting_code": "reportingCode",
        "account_name": "accountName",
        "balance": "balance",
        "signed_balance": "signedBalance",
        "account_movement": "accountMovement",
    }

    def __init__(
        self,
        account_id=None,
        account_type=None,
        account_code=None,
        account_class=None,
        status=None,
        reporting_code=None,
        account_name=None,
        balance=None,
        signed_balance=None,
        account_movement=None,
    ):  # noqa: E501
        """TrialBalanceAccount - a model defined in OpenAPI"""  # noqa: E501

        self._account_id = None
        self._account_type = None
        self._account_code = None
        self._account_class = None
        self._status = None
        self._reporting_code = None
        self._account_name = None
        self._balance = None
        self._signed_balance = None
        self._account_movement = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_type is not None:
            self.account_type = account_type
        if account_code is not None:
            self.account_code = account_code
        if account_class is not None:
            self.account_class = account_class
        if status is not None:
            self.status = status
        if reporting_code is not None:
            self.reporting_code = reporting_code
        if account_name is not None:
            self.account_name = account_name
        if balance is not None:
            self.balance = balance
        if signed_balance is not None:
            self.signed_balance = signed_balance
        if account_movement is not None:
            self.account_movement = account_movement

    @property
    def account_id(self):
        """Gets the account_id of this TrialBalanceAccount.  # noqa: E501

        ID of the account  # noqa: E501

        :return: The account_id of this TrialBalanceAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TrialBalanceAccount.

        ID of the account  # noqa: E501

        :param account_id: The account_id of this TrialBalanceAccount.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_type(self):
        """Gets the account_type of this TrialBalanceAccount.  # noqa: E501

        The type of the account. See <a href='https://developer.xero.com/documentation/api/types#AccountTypes'>Account Types</a>  # noqa: E501

        :return: The account_type of this TrialBalanceAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this TrialBalanceAccount.

        The type of the account. See <a href='https://developer.xero.com/documentation/api/types#AccountTypes'>Account Types</a>  # noqa: E501

        :param account_type: The account_type of this TrialBalanceAccount.  # noqa: E501
        :type: str
        """

        self._account_type = account_type

    @property
    def account_code(self):
        """Gets the account_code of this TrialBalanceAccount.  # noqa: E501

        Customer defined alpha numeric account code e.g 200 or SALES  # noqa: E501

        :return: The account_code of this TrialBalanceAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this TrialBalanceAccount.

        Customer defined alpha numeric account code e.g 200 or SALES  # noqa: E501

        :param account_code: The account_code of this TrialBalanceAccount.  # noqa: E501
        :type: str
        """

        self._account_code = account_code

    @property
    def account_class(self):
        """Gets the account_class of this TrialBalanceAccount.  # noqa: E501

        The class of the account. See <a href='https://developer.xero.com/documentation/api/types#AccountClassTypes'>Account Class Types</a>  # noqa: E501

        :return: The account_class of this TrialBalanceAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_class

    @account_class.setter
    def account_class(self, account_class):
        """Sets the account_class of this TrialBalanceAccount.

        The class of the account. See <a href='https://developer.xero.com/documentation/api/types#AccountClassTypes'>Account Class Types</a>  # noqa: E501

        :param account_class: The account_class of this TrialBalanceAccount.  # noqa: E501
        :type: str
        """

        self._account_class = account_class

    @property
    def status(self):
        """Gets the status of this TrialBalanceAccount.  # noqa: E501

        Accounts with a status of ACTIVE can be updated to ARCHIVED. See <a href='https://developer.xero.com/documentation/api/types#AccountStatusCodes'>Account Status Codes</a>  # noqa: E501

        :return: The status of this TrialBalanceAccount.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TrialBalanceAccount.

        Accounts with a status of ACTIVE can be updated to ARCHIVED. See <a href='https://developer.xero.com/documentation/api/types#AccountStatusCodes'>Account Status Codes</a>  # noqa: E501

        :param status: The status of this TrialBalanceAccount.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def reporting_code(self):
        """Gets the reporting_code of this TrialBalanceAccount.  # noqa: E501

        Reporting code (Shown if set)  # noqa: E501

        :return: The reporting_code of this TrialBalanceAccount.  # noqa: E501
        :rtype: str
        """
        return self._reporting_code

    @reporting_code.setter
    def reporting_code(self, reporting_code):
        """Sets the reporting_code of this TrialBalanceAccount.

        Reporting code (Shown if set)  # noqa: E501

        :param reporting_code: The reporting_code of this TrialBalanceAccount.  # noqa: E501
        :type: str
        """

        self._reporting_code = reporting_code

    @property
    def account_name(self):
        """Gets the account_name of this TrialBalanceAccount.  # noqa: E501

        Name of the account  # noqa: E501

        :return: The account_name of this TrialBalanceAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this TrialBalanceAccount.

        Name of the account  # noqa: E501

        :param account_name: The account_name of this TrialBalanceAccount.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def balance(self):
        """Gets the balance of this TrialBalanceAccount.  # noqa: E501


        :return: The balance of this TrialBalanceAccount.  # noqa: E501
        :rtype: TrialBalanceEntry
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this TrialBalanceAccount.


        :param balance: The balance of this TrialBalanceAccount.  # noqa: E501
        :type: TrialBalanceEntry
        """

        self._balance = balance

    @property
    def signed_balance(self):
        """Gets the signed_balance of this TrialBalanceAccount.  # noqa: E501

        Value of balance. Expense and Asset accounts code debits as positive. Revenue, Liability, and Equity accounts code debits as negative  # noqa: E501

        :return: The signed_balance of this TrialBalanceAccount.  # noqa: E501
        :rtype: float
        """
        return self._signed_balance

    @signed_balance.setter
    def signed_balance(self, signed_balance):
        """Sets the signed_balance of this TrialBalanceAccount.

        Value of balance. Expense and Asset accounts code debits as positive. Revenue, Liability, and Equity accounts code debits as negative  # noqa: E501

        :param signed_balance: The signed_balance of this TrialBalanceAccount.  # noqa: E501
        :type: float
        """

        self._signed_balance = signed_balance

    @property
    def account_movement(self):
        """Gets the account_movement of this TrialBalanceAccount.  # noqa: E501


        :return: The account_movement of this TrialBalanceAccount.  # noqa: E501
        :rtype: TrialBalanceMovement
        """
        return self._account_movement

    @account_movement.setter
    def account_movement(self, account_movement):
        """Sets the account_movement of this TrialBalanceAccount.


        :param account_movement: The account_movement of this TrialBalanceAccount.  # noqa: E501
        :type: TrialBalanceMovement
        """

        self._account_movement = account_movement
