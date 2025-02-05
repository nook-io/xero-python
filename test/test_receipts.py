# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.receipts import Receipts  # noqa: E501


class TestReceipts(unittest.TestCase):
    """Receipts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Receipts:
        """Test Receipts
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Receipts`
        """
        model = Receipts()  # noqa: E501
        if include_optional:
            return Receipts(
                receipts = [
                    xero_python.models.receipt.Receipt(
                        date = '', 
                        contact = xero_python.models.contact.Contact(
                            contact_id = '', 
                            merged_to_contact_id = '', 
                            contact_number = '', 
                            account_number = '', 
                            contact_status = 'ACTIVE', 
                            name = '', 
                            first_name = '', 
                            last_name = '', 
                            company_number = '', 
                            email_address = '', 
                            contact_persons = [
                                xero_python.models.contact_person.ContactPerson(
                                    first_name = '', 
                                    last_name = '', 
                                    email_address = '', 
                                    include_in_emails = True, )
                                ], 
                            bank_account_details = '', 
                            tax_number = '', 
                            accounts_receivable_tax_type = '', 
                            accounts_payable_tax_type = '', 
                            addresses = [
                                xero_python.models.address.Address(
                                    address_type = 'POBOX', 
                                    address_line1 = '', 
                                    address_line2 = '', 
                                    address_line3 = '', 
                                    address_line4 = '', 
                                    city = '', 
                                    region = '', 
                                    postal_code = '', 
                                    country = '', 
                                    attention_to = '', )
                                ], 
                            phones = [
                                xero_python.models.phone.Phone(
                                    phone_type = 'DEFAULT', 
                                    phone_number = '', 
                                    phone_area_code = '', 
                                    phone_country_code = '', )
                                ], 
                            is_supplier = True, 
                            is_customer = True, 
                            sales_default_line_amount_type = 'INCLUSIVE', 
                            purchases_default_line_amount_type = 'INCLUSIVE', 
                            default_currency = 'AED', 
                            xero_network_key = '', 
                            sales_default_account_code = '', 
                            purchases_default_account_code = '', 
                            sales_tracking_categories = [
                                xero_python.models.sales_tracking_category.SalesTrackingCategory(
                                    tracking_category_name = '', 
                                    tracking_option_name = '', )
                                ], 
                            purchases_tracking_categories = [
                                xero_python.models.sales_tracking_category.SalesTrackingCategory(
                                    tracking_category_name = '', 
                                    tracking_option_name = '', )
                                ], 
                            tracking_category_name = '', 
                            tracking_category_option = '', 
                            payment_terms = xero_python.models.payment_term.PaymentTerm(
                                bills = xero_python.models.bill.Bill(
                                    day = 56, 
                                    type = 'DAYSAFTERBILLDATE', ), 
                                sales = xero_python.models.bill.Bill(
                                    day = 56, ), ), 
                            updated_date_utc = '/Date(1573755038314)/', 
                            contact_groups = [
                                xero_python.models.contact_group.ContactGroup(
                                    name = '', 
                                    status = 'ACTIVE', 
                                    contact_group_id = '', 
                                    contacts = [
                                        xero_python.models.contact.Contact(
                                            contact_id = '', 
                                            merged_to_contact_id = '', 
                                            contact_number = '', 
                                            account_number = '', 
                                            contact_status = 'ACTIVE', 
                                            name = '', 
                                            first_name = '', 
                                            last_name = '', 
                                            company_number = '', 
                                            email_address = '', 
                                            bank_account_details = '', 
                                            tax_number = '', 
                                            accounts_receivable_tax_type = '', 
                                            accounts_payable_tax_type = '', 
                                            is_supplier = True, 
                                            is_customer = True, 
                                            sales_default_line_amount_type = 'INCLUSIVE', 
                                            purchases_default_line_amount_type = 'INCLUSIVE', 
                                            xero_network_key = '', 
                                            sales_default_account_code = '', 
                                            purchases_default_account_code = '', 
                                            tracking_category_name = '', 
                                            tracking_category_option = '', 
                                            updated_date_utc = '/Date(1573755038314)/', 
                                            website = '', 
                                            branding_theme = xero_python.models.branding_theme.BrandingTheme(
                                                branding_theme_id = '', 
                                                name = '', 
                                                logo_url = '', 
                                                sort_order = 56, 
                                                created_date_utc = '/Date(1573755038314)/', ), 
                                            batch_payments = xero_python.models.batch_payment_details.BatchPaymentDetails(
                                                bank_account_number = '123-456-1111111', 
                                                bank_account_name = 'ACME Bank', 
                                                details = 'Hello World', 
                                                code = 'ABC', 
                                                reference = 'Foobar', ), 
                                            discount = 1.337, 
                                            balances = xero_python.models.balances.Balances(
                                                accounts_receivable = xero_python.models.accounts_receivable.AccountsReceivable(
                                                    outstanding = 1.337, 
                                                    overdue = 1.337, ), 
                                                accounts_payable = xero_python.models.accounts_payable.AccountsPayable(
                                                    outstanding = 1.337, 
                                                    overdue = 1.337, ), ), 
                                            attachments = [
                                                xero_python.models.attachment.Attachment(
                                                    attachment_id = '00000000-0000-0000-0000-000000000000', 
                                                    file_name = 'xero-dev.jpg', 
                                                    url = 'https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg', 
                                                    mime_type = 'image/jpg', 
                                                    content_length = 56, 
                                                    include_online = True, )
                                                ], 
                                            has_attachments = False, 
                                            validation_errors = [
                                                xero_python.models.validation_error.ValidationError(
                                                    message = '', )
                                                ], 
                                            has_validation_errors = False, 
                                            status_attribute_string = '', )
                                        ], )
                                ], 
                            website = '', 
                            branding_theme = xero_python.models.branding_theme.BrandingTheme(
                                branding_theme_id = '', 
                                name = '', 
                                logo_url = '', 
                                sort_order = 56, 
                                created_date_utc = '/Date(1573755038314)/', ), 
                            batch_payments = xero_python.models.batch_payment_details.BatchPaymentDetails(
                                bank_account_number = '123-456-1111111', 
                                bank_account_name = 'ACME Bank', 
                                details = 'Hello World', 
                                code = 'ABC', 
                                reference = 'Foobar', ), 
                            discount = 1.337, 
                            balances = xero_python.models.balances.Balances(), 
                            attachments = [
                                xero_python.models.attachment.Attachment(
                                    attachment_id = '00000000-0000-0000-0000-000000000000', 
                                    file_name = 'xero-dev.jpg', 
                                    url = 'https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg', 
                                    mime_type = 'image/jpg', 
                                    content_length = 56, 
                                    include_online = True, )
                                ], 
                            has_attachments = False, 
                            validation_errors = [
                                xero_python.models.validation_error.ValidationError(
                                    message = '', )
                                ], 
                            has_validation_errors = False, 
                            status_attribute_string = '', ), 
                        line_items = [
                            xero_python.models.line_item.LineItem(
                                line_item_id = '00000000-0000-0000-0000-000000000000', 
                                description = '', 
                                quantity = 1.337, 
                                unit_amount = 1.337, 
                                item_code = '', 
                                account_code = '', 
                                account_id = '00000000-0000-0000-0000-000000000000', 
                                tax_type = '', 
                                tax_amount = 1.337, 
                                item = xero_python.models.line_item_item.LineItemItem(
                                    code = '', 
                                    name = '', 
                                    item_id = '', ), 
                                line_amount = 1.337, 
                                tracking = [
                                    xero_python.models.line_item_tracking.LineItemTracking(
                                        tracking_category_id = '00000000-0000-0000-0000-000000000000', 
                                        tracking_option_id = '00000000-0000-0000-0000-000000000000', 
                                        name = 'Region', 
                                        option = 'North', )
                                    ], 
                                discount_rate = 1.337, 
                                discount_amount = 1.337, 
                                repeating_invoice_id = '00000000-0000-0000-0000-000000000000', 
                                taxability = 'TAXABLE', 
                                sales_tax_code_id = 1.337, 
                                tax_breakdown = [
                                    xero_python.models.tax_breakdown_component.TaxBreakdownComponent(
                                        tax_component_id = '', 
                                        name = '', 
                                        tax_percentage = 1.337, 
                                        tax_amount = 1.337, 
                                        taxable_amount = 1.337, 
                                        non_taxable_amount = 1.337, 
                                        exempt_amount = 1.337, 
                                        state_assigned_no = '', 
                                        jurisdiction_region = '', )
                                    ], )
                            ], 
                        user = xero_python.models.user.User(
                            user_id = '', 
                            email_address = '', 
                            first_name = '', 
                            last_name = '', 
                            updated_date_utc = '/Date(1573755038314)/', 
                            is_subscriber = True, 
                            organisation_role = 'READONLY', ), 
                        reference = '', 
                        line_amount_types = 'Exclusive', 
                        sub_total = 1.337, 
                        total_tax = 1.337, 
                        total = 1.337, 
                        receipt_id = '', 
                        status = 'DRAFT', 
                        receipt_number = '', 
                        updated_date_utc = '/Date(1573755038314)/', 
                        has_attachments = False, 
                        url = '', 
                        validation_errors = [
                            
                            ], 
                        warnings = [
                            
                            ], 
                        attachments = , )
                    ]
            )
        else:
            return Receipts(
        )
        """

    def testReceipts(self):
        """Test Receipts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
