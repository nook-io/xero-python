# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.benefit_line import BenefitLine  # noqa: E501


class TestBenefitLine(unittest.TestCase):
    """BenefitLine unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BenefitLine:
        """Test BenefitLine
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `BenefitLine`
        """
        model = BenefitLine()  # noqa: E501
        if include_optional:
            return BenefitLine(
                benefit_type_id = '',
                display_name = '',
                amount = 1.337,
                fixed_amount = 1.337,
                percentage = 1.337
            )
        else:
            return BenefitLine(
        )
        """

    def testBenefitLine(self):
        """Test BenefitLine"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
