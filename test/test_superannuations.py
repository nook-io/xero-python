# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.superannuations import Superannuations  # noqa: E501


class TestSuperannuations(unittest.TestCase):
    """Superannuations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Superannuations:
        """Test Superannuations
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Superannuations`
        """
        model = Superannuations()  # noqa: E501
        if include_optional:
            return Superannuations(
                pagination = xero_python.models.pagination.Pagination(
                    page = 1, 
                    page_size = 10, 
                    page_count = 1, 
                    item_count = 2, ),
                problem = xero_python.models.problem.Problem(
                    type = 'application/problem+json', 
                    title = 'BadRequest', 
                    status = '400', 
                    detail = 'Validation error occurred.', 
                    instance = '', 
                    invalid_fields = [
                        xero_python.models.invalid_field.InvalidField(
                            name = 'DateOfBirth', 
                            reason = 'The Date of Birth is required.', )
                        ], ),
                benefits = [
                    xero_python.models.benefit_1.Benefit_1(
                        id = '', 
                        name = '', 
                        category = 'KiwiSaver', 
                        liability_account_id = '', 
                        expense_account_id = '', 
                        calculation_type_nz = 'FixedAmount', 
                        standard_amount = 1.337, 
                        percentage = 1.337, 
                        company_max = 1.337, 
                        current_record = True, )
                    ]
            )
        else:
            return Superannuations(
        )
        """

    def testSuperannuations(self):
        """Test Superannuations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
