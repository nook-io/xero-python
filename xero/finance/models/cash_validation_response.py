# coding: utf-8

"""
    Xero Finance API

    The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class CashValidationResponse(BaseModel):
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
        "statement_balance": "StatementBalanceResponse",
        "statement_balance_date": "date",
        "bank_statement": "BankStatementResponse",
        "cash_account": "CashAccountResponse",
    }

    attribute_map = {
        "account_id": "accountId",
        "statement_balance": "statementBalance",
        "statement_balance_date": "statementBalanceDate",
        "bank_statement": "bankStatement",
        "cash_account": "cashAccount",
    }

    def __init__(
        self,
        account_id=None,
        statement_balance=None,
        statement_balance_date=None,
        bank_statement=None,
        cash_account=None,
    ):  # noqa: E501
        """CashValidationResponse - a model defined in OpenAPI"""  # noqa: E501

        self._account_id = None
        self._statement_balance = None
        self._statement_balance_date = None
        self._bank_statement = None
        self._cash_account = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if statement_balance is not None:
            self.statement_balance = statement_balance
        if statement_balance_date is not None:
            self.statement_balance_date = statement_balance_date
        if bank_statement is not None:
            self.bank_statement = bank_statement
        if cash_account is not None:
            self.cash_account = cash_account

    @property
    def account_id(self):
        """Gets the account_id of this CashValidationResponse.  # noqa: E501

        The Xero identifier for an account  # noqa: E501

        :return: The account_id of this CashValidationResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CashValidationResponse.

        The Xero identifier for an account  # noqa: E501

        :param account_id: The account_id of this CashValidationResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def statement_balance(self):
        """Gets the statement_balance of this CashValidationResponse.  # noqa: E501


        :return: The statement_balance of this CashValidationResponse.  # noqa: E501
        :rtype: StatementBalanceResponse
        """
        return self._statement_balance

    @statement_balance.setter
    def statement_balance(self, statement_balance):
        """Sets the statement_balance of this CashValidationResponse.


        :param statement_balance: The statement_balance of this CashValidationResponse.  # noqa: E501
        :type: StatementBalanceResponse
        """

        self._statement_balance = statement_balance

    @property
    def statement_balance_date(self):
        """Gets the statement_balance_date of this CashValidationResponse.  # noqa: E501

        UTC Date when the last bank statement item was entered into Xero. This date is represented in ISO 8601 format.  # noqa: E501

        :return: The statement_balance_date of this CashValidationResponse.  # noqa: E501
        :rtype: date
        """
        return self._statement_balance_date

    @statement_balance_date.setter
    def statement_balance_date(self, statement_balance_date):
        """Sets the statement_balance_date of this CashValidationResponse.

        UTC Date when the last bank statement item was entered into Xero. This date is represented in ISO 8601 format.  # noqa: E501

        :param statement_balance_date: The statement_balance_date of this CashValidationResponse.  # noqa: E501
        :type: date
        """

        self._statement_balance_date = statement_balance_date

    @property
    def bank_statement(self):
        """Gets the bank_statement of this CashValidationResponse.  # noqa: E501


        :return: The bank_statement of this CashValidationResponse.  # noqa: E501
        :rtype: BankStatementResponse
        """
        return self._bank_statement

    @bank_statement.setter
    def bank_statement(self, bank_statement):
        """Sets the bank_statement of this CashValidationResponse.


        :param bank_statement: The bank_statement of this CashValidationResponse.  # noqa: E501
        :type: BankStatementResponse
        """

        self._bank_statement = bank_statement

    @property
    def cash_account(self):
        """Gets the cash_account of this CashValidationResponse.  # noqa: E501


        :return: The cash_account of this CashValidationResponse.  # noqa: E501
        :rtype: CashAccountResponse
        """
        return self._cash_account

    @cash_account.setter
    def cash_account(self, cash_account):
        """Sets the cash_account of this CashValidationResponse.


        :param cash_account: The cash_account of this CashValidationResponse.  # noqa: E501
        :type: CashAccountResponse
        """

        self._cash_account = cash_account
