# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.report_attribute import ReportAttribute  # noqa: E501


class TestReportAttribute(unittest.TestCase):
    """ReportAttribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportAttribute:
        """Test ReportAttribute
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ReportAttribute`
        """
        model = ReportAttribute()  # noqa: E501
        if include_optional:
            return ReportAttribute(
                id = '',
                value = ''
            )
        else:
            return ReportAttribute(
        )
        """

    def testReportAttribute(self):
        """Test ReportAttribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
