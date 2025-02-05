# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.employee_statutory_sick_leave import EmployeeStatutorySickLeave  # noqa: E501


class TestEmployeeStatutorySickLeave(unittest.TestCase):
    """EmployeeStatutorySickLeave unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmployeeStatutorySickLeave:
        """Test EmployeeStatutorySickLeave
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EmployeeStatutorySickLeave`
        """
        model = EmployeeStatutorySickLeave()  # noqa: E501
        if include_optional:
            return EmployeeStatutorySickLeave(
                statutory_leave_id = '',
                employee_id = '',
                leave_type_id = '',
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                type = 'Sick',
                status = 'Pending',
                work_pattern = [
                    ''
                    ],
                is_pregnancy_related = True,
                sufficient_notice = True,
                is_entitled = True,
                entitlement_weeks_requested = 1.337,
                entitlement_weeks_qualified = 1.337,
                entitlement_weeks_remaining = 1.337,
                overlaps_with_other_leave = True,
                entitlement_failure_reasons = [
                    'UnableToCalculateAwe'
                    ]
            )
        else:
            return EmployeeStatutorySickLeave(
                employee_id = '',
                leave_type_id = '',
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                work_pattern = [
                    ''
                    ],
                is_pregnancy_related = True,
                sufficient_notice = True,
        )
        """

    def testEmployeeStatutorySickLeave(self):
        """Test EmployeeStatutorySickLeave"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
