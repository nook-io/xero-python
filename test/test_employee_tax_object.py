# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.employee_tax_object import EmployeeTaxObject  # noqa: E501


class TestEmployeeTaxObject(unittest.TestCase):
    """EmployeeTaxObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmployeeTaxObject:
        """Test EmployeeTaxObject
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EmployeeTaxObject`
        """
        model = EmployeeTaxObject()  # noqa: E501
        if include_optional:
            return EmployeeTaxObject(
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
                employee_tax = xero_python.models.employee_tax.EmployeeTax(
                    starter_type = 'New Employee with P45', 
                    starter_declaration = 'B.) This is currently their only job', 
                    tax_code = '1185L', 
                    w1_m1 = True, 
                    previous_taxable_pay = 1.337, 
                    previous_tax_paid = 1.337, 
                    student_loan_deduction = 'Plan Type 2', 
                    has_post_graduate_loans = True, 
                    is_director = True, 
                    directorship_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    nic_calculation_method = 'Annualized', )
            )
        else:
            return EmployeeTaxObject(
        )
        """

    def testEmployeeTaxObject(self):
        """Test EmployeeTaxObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
