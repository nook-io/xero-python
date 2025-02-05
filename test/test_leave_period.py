# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.leave_period import LeavePeriod  # noqa: E501


class TestLeavePeriod(unittest.TestCase):
    """LeavePeriod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeavePeriod:
        """Test LeavePeriod
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LeavePeriod`
        """
        model = LeavePeriod()  # noqa: E501
        if include_optional:
            return LeavePeriod(
                number_of_units = 22.8,
                pay_period_end_date = '/Date(322560000000+0000)/',
                pay_period_start_date = '/Date(322560000000+0000)/',
                leave_period_status = 'SCHEDULED'
            )
        else:
            return LeavePeriod(
        )
        """

    def testLeavePeriod(self):
        """Test LeavePeriod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
