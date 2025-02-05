# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.actions import Actions  # noqa: E501


class TestActions(unittest.TestCase):
    """Actions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Actions:
        """Test Actions
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Actions`
        """
        model = Actions()  # noqa: E501
        if include_optional:
            return Actions(
                actions = [
                    xero_python.models.action.Action(
                        name = 'UseMulticurrency', 
                        status = 'ALLOWED', )
                    ]
            )
        else:
            return Actions(
        )
        """

    def testActions(self):
        """Test Actions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
