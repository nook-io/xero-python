# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.employee_leave_setup import EmployeeLeaveSetup  # noqa: E501


class TestEmployeeLeaveSetup(unittest.TestCase):
    """EmployeeLeaveSetup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmployeeLeaveSetup:
        """Test EmployeeLeaveSetup
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EmployeeLeaveSetup`
        """
        model = EmployeeLeaveSetup()  # noqa: E501
        if include_optional:
            return EmployeeLeaveSetup(
                include_holiday_pay = False,
                holiday_pay_opening_balance = 10.5,
                annual_leave_opening_balance = 25.89,
                negative_annual_leave_balance_paid_amount = 10.0,
                sick_leave_hours_to_accrue_annually = 100.5,
                sick_leave_maximum_hours_to_accrue = 200.5,
                sick_leave_opening_balance = 10.5,
                sick_leave_schedule_of_accrual = 'OnAnniversaryDate',
                sick_leave_anniversary_date = 'Sun Jan 19 00:00:00 GMT 2020'
            )
        else:
            return EmployeeLeaveSetup(
        )
        """

    def testEmployeeLeaveSetup(self):
        """Test EmployeeLeaveSetup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
