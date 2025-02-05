# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.payment_services import PaymentServices  # noqa: E501


class TestPaymentServices(unittest.TestCase):
    """PaymentServices unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentServices:
        """Test PaymentServices
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PaymentServices`
        """
        model = PaymentServices()  # noqa: E501
        if include_optional:
            return PaymentServices(
                payment_services = [
                    xero_python.models.payment_service.PaymentService(
                        payment_service_id = '', 
                        payment_service_name = '', 
                        payment_service_url = '', 
                        pay_now_text = '', 
                        payment_service_type = '', 
                        validation_errors = [
                            xero_python.models.validation_error.ValidationError(
                                message = '', )
                            ], )
                    ]
            )
        else:
            return PaymentServices(
        )
        """

    def testPaymentServices(self):
        """Test PaymentServices"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
