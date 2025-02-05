# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.cashflow_type import CashflowType  # noqa: E501


class TestCashflowType(unittest.TestCase):
    """CashflowType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CashflowType:
        """Test CashflowType
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CashflowType`
        """
        model = CashflowType()  # noqa: E501
        if include_optional:
            return CashflowType(
                name = '',
                total = 1.337,
                accounts = [
                    xero_python.models.cashflow_account.CashflowAccount(
                        account_id = '', 
                        account_type = '', 
                        account_class = '', 
                        code = '', 
                        name = '', 
                        reporting_code = '', 
                        total = 1.337, )
                    ]
            )
        else:
            return CashflowType(
        )
        """

    def testCashflowType(self):
        """Test CashflowType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
