# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.employee_leave import EmployeeLeave  # noqa: E501


class TestEmployeeLeave(unittest.TestCase):
    """EmployeeLeave unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmployeeLeave:
        """Test EmployeeLeave
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EmployeeLeave`
        """
        model = EmployeeLeave()  # noqa: E501
        if include_optional:
            return EmployeeLeave(
                leave_id = '',
                leave_type_id = '',
                description = '',
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                periods = [
                    xero_python.models.leave_period_1.LeavePeriod_1(
                        period_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        period_end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        number_of_units = 1.337, 
                        period_status = 'Approved', )
                    ],
                updated_date_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return EmployeeLeave(
                leave_type_id = '',
                description = '',
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testEmployeeLeave(self):
        """Test EmployeeLeave"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
