# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.reimbursement import Reimbursement  # noqa: E501


class TestReimbursement(unittest.TestCase):
    """Reimbursement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Reimbursement:
        """Test Reimbursement
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Reimbursement`
        """
        model = Reimbursement()  # noqa: E501
        if include_optional:
            return Reimbursement(
                reimbursement_id = '',
                name = '',
                account_id = '',
                current_record = True
            )
        else:
            return Reimbursement(
                name = '',
                account_id = '',
        )
        """

    def testReimbursement(self):
        """Test Reimbursement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
