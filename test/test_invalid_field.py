# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.invalid_field import InvalidField  # noqa: E501


class TestInvalidField(unittest.TestCase):
    """InvalidField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvalidField:
        """Test InvalidField
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `InvalidField`
        """
        model = InvalidField()  # noqa: E501
        if include_optional:
            return InvalidField(
                name = 'DateOfBirth',
                reason = 'The Date of Birth is required.'
            )
        else:
            return InvalidField(
        )
        """

    def testInvalidField(self):
        """Test InvalidField"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
