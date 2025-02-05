# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.bank_transaction_response import BankTransactionResponse  # noqa: E501


class TestBankTransactionResponse(unittest.TestCase):
    """BankTransactionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankTransactionResponse:
        """Test BankTransactionResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `BankTransactionResponse`
        """
        model = BankTransactionResponse()  # noqa: E501
        if include_optional:
            return BankTransactionResponse(
                bank_transaction_id = '',
                batch_payment_id = '',
                contact = xero_python.models.contact_response.ContactResponse(
                    contact_id = '', 
                    contact_name = '', ),
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                amount = 1.337,
                line_items = [
                    xero_python.models.line_item_response.LineItemResponse(
                        account_id = '', 
                        reporting_code = '', 
                        line_amount = 1.337, 
                        account_type = '', )
                    ]
            )
        else:
            return BankTransactionResponse(
        )
        """

    def testBankTransactionResponse(self):
        """Test BankTransactionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
