# coding: utf-8

"""
    Xero Finance API

    The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class BankStatementResponse(BaseModel):
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
        "statement_lines": "StatementLinesResponse",
        "current_statement": "CurrentStatementResponse",
    }

    attribute_map = {
        "statement_lines": "statementLines",
        "current_statement": "currentStatement",
    }

    def __init__(self, statement_lines=None, current_statement=None):  # noqa: E501
        """BankStatementResponse - a model defined in OpenAPI"""  # noqa: E501

        self._statement_lines = None
        self._current_statement = None
        self.discriminator = None

        if statement_lines is not None:
            self.statement_lines = statement_lines
        if current_statement is not None:
            self.current_statement = current_statement

    @property
    def statement_lines(self):
        """Gets the statement_lines of this BankStatementResponse.  # noqa: E501


        :return: The statement_lines of this BankStatementResponse.  # noqa: E501
        :rtype: StatementLinesResponse
        """
        return self._statement_lines

    @statement_lines.setter
    def statement_lines(self, statement_lines):
        """Sets the statement_lines of this BankStatementResponse.


        :param statement_lines: The statement_lines of this BankStatementResponse.  # noqa: E501
        :type: StatementLinesResponse
        """

        self._statement_lines = statement_lines

    @property
    def current_statement(self):
        """Gets the current_statement of this BankStatementResponse.  # noqa: E501


        :return: The current_statement of this BankStatementResponse.  # noqa: E501
        :rtype: CurrentStatementResponse
        """
        return self._current_statement

    @current_statement.setter
    def current_statement(self, current_statement):
        """Sets the current_statement of this BankStatementResponse.


        :param current_statement: The current_statement of this BankStatementResponse.  # noqa: E501
        :type: CurrentStatementResponse
        """

        self._current_statement = current_statement
