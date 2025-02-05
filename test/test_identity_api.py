# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.api.identity_api import IdentityApi  # noqa: E501


class TestIdentityApi(unittest.IsolatedAsyncioTestCase):
    """IdentityApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = IdentityApi()

    async def asyncTearDown(self) -> None:
        pass

    async def test_delete_connection(self) -> None:
        """Test case for delete_connection

        Deletes a connection for this user (i.e. disconnect a tenant)  # noqa: E501
        """
        pass

    async def test_get_connections(self) -> None:
        """Test case for get_connections

        Retrieves the connections for this user  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
