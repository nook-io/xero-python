# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.address1 import Address1  # noqa: E501


class TestAddress1(unittest.TestCase):
    """Address1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Address1:
        """Test Address1
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Address1`
        """
        model = Address1()  # noqa: E501
        if include_optional:
            return Address1(
                address_line1 = '123 Main St',
                address_line2 = 'Apt 4',
                city = 'Fulham',
                post_code = 'SW6 6EY',
                country_name = 'United Kingdom'
            )
        else:
            return Address1(
                address_line1 = '123 Main St',
                city = 'Fulham',
                post_code = 'SW6 6EY',
        )
        """

    def testAddress1(self):
        """Test Address1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
