# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.folder import Folder  # noqa: E501


class TestFolder(unittest.TestCase):
    """Folder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Folder:
        """Test Folder
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Folder`
        """
        model = Folder()  # noqa: E501
        if include_optional:
            return Folder(
                name = 'assets',
                file_count = 5,
                email = 'foo@bar.com',
                is_inbox = True,
                id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c'
            )
        else:
            return Folder(
        )
        """

    def testFolder(self):
        """Test Folder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
