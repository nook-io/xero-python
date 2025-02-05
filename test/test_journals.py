# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.journals import Journals  # noqa: E501


class TestJournals(unittest.TestCase):
    """Journals unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Journals:
        """Test Journals
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Journals`
        """
        model = Journals()  # noqa: E501
        if include_optional:
            return Journals(
                warnings = [
                    xero_python.models.validation_error.ValidationError(
                        message = '', )
                    ],
                journals = [
                    xero_python.models.journal.Journal(
                        journal_id = '', 
                        journal_date = '', 
                        journal_number = 56, 
                        created_date_utc = '/Date(1573755038314)/', 
                        reference = '', 
                        source_id = '', 
                        source_type = 'ACCREC', 
                        journal_lines = [
                            xero_python.models.journal_line.JournalLine(
                                journal_line_id = '7be9db36-3598-4755-ba5c-c2dbc8c4a7a2', 
                                account_id = 'ceef66a5-a545-413b-9312-78a53caadbc4', 
                                account_code = '090', 
                                account_type = 'BANK', 
                                account_name = 'Checking Account', 
                                description = 'My business checking account', 
                                net_amount = 4130.98, 
                                gross_amount = 4130.98, 
                                tax_amount = 0.0, 
                                tax_type = '', 
                                tax_name = 'Tax Exempt', 
                                tracking_categories = [
                                    xero_python.models.tracking_category.TrackingCategory(
                                        tracking_category_id = '', 
                                        tracking_option_id = '', 
                                        name = '', 
                                        option = '', 
                                        status = 'ACTIVE', 
                                        options = [
                                            xero_python.models.tracking_option.TrackingOption(
                                                tracking_option_id = '', 
                                                name = '', 
                                                status = 'ACTIVE', 
                                                tracking_category_id = '', )
                                            ], )
                                    ], )
                            ], )
                    ]
            )
        else:
            return Journals(
        )
        """

    def testJournals(self):
        """Test Journals"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
