# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.account1 import Account1  # noqa: E501


class TestAccount1(unittest.TestCase):
    """Account1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Account1:
        """Test Account1
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Account1`
        """
        model = Account1()  # noqa: E501
        if include_optional:
            return Account1(
                account_id = '',
                type = 'BANK',
                code = '',
                name = ''
            )
        else:
            return Account1(
        )
        """

    def testAccount1(self):
        """Test Account1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
