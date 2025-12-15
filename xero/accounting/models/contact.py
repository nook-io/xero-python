from xero.models import BaseModel


class Contact(BaseModel):
    openapi_types = {
        "contact_id": "str",
        "merged_to_contact_id": "str",
        "contact_number": "str",
        "account_number": "str",
        "contact_status": "str",
        "name": "str",
        "first_name": "str",
        "last_name": "str",
        "company_number": "str",
        "email_address": "str",
        "contact_persons": "list[ContactPerson]",
        "bank_account_details": "str",
        "tax_number": "str",
        "accounts_receivable_tax_type": "str",
        "accounts_payable_tax_type": "str",
        "addresses": "list[Address]",
        "phones": "list[Phone]",
        "is_supplier": "bool",
        "is_customer": "bool",
        "sales_default_line_amount_type": "str",
        "purchases_default_line_amount_type": "str",
        "default_currency": "CurrencyCode",
        "xero_network_key": "str",
        "sales_default_account_code": "str",
        "purchases_default_account_code": "str",
        "sales_tracking_categories": "list[SalesTrackingCategory]",
        "purchases_tracking_categories": "list[SalesTrackingCategory]",
        "tracking_category_name": "str",
        "tracking_category_option": "str",
        "payment_terms": "PaymentTerm",
        "updated_date_utc": "datetime[ms-format]",
        "contact_groups": "list[ContactGroup]",
        "website": "str",
        "branding_theme": "BrandingTheme",
        "batch_payments": "BatchPaymentDetails",
        "discount": "float",
        "balances": "Balances",
        "attachments": "list[Attachment]",
        "has_attachments": "bool",
        "validation_errors": "list[ValidationError]",
        "has_validation_errors": "bool",
        "status_attribute_string": "str",
    }
    attribute_map = {
        "contact_id": "ContactID",
        "merged_to_contact_id": "MergedToContactID",
        "contact_number": "ContactNumber",
        "account_number": "AccountNumber",
        "contact_status": "ContactStatus",
        "name": "Name",
        "first_name": "FirstName",
        "last_name": "LastName",
        "company_number": "CompanyNumber",
        "email_address": "EmailAddress",
        "contact_persons": "ContactPersons",
        "bank_account_details": "BankAccountDetails",
        "tax_number": "TaxNumber",
        "accounts_receivable_tax_type": "AccountsReceivableTaxType",
        "accounts_payable_tax_type": "AccountsPayableTaxType",
        "addresses": "Addresses",
        "phones": "Phones",
        "is_supplier": "IsSupplier",
        "is_customer": "IsCustomer",
        "sales_default_line_amount_type": "SalesDefaultLineAmountType",
        "purchases_default_line_amount_type": "PurchasesDefaultLineAmountType",
        "default_currency": "DefaultCurrency",
        "xero_network_key": "XeroNetworkKey",
        "sales_default_account_code": "SalesDefaultAccountCode",
        "purchases_default_account_code": "PurchasesDefaultAccountCode",
        "sales_tracking_categories": "SalesTrackingCategories",
        "purchases_tracking_categories": "PurchasesTrackingCategories",
        "tracking_category_name": "TrackingCategoryName",
        "tracking_category_option": "TrackingCategoryOption",
        "payment_terms": "PaymentTerms",
        "updated_date_utc": "UpdatedDateUTC",
        "contact_groups": "ContactGroups",
        "website": "Website",
        "branding_theme": "BrandingTheme",
        "batch_payments": "BatchPayments",
        "discount": "Discount",
        "balances": "Balances",
        "attachments": "Attachments",
        "has_attachments": "HasAttachments",
        "validation_errors": "ValidationErrors",
        "has_validation_errors": "HasValidationErrors",
        "status_attribute_string": "StatusAttributeString",
    }

    def __init__(
        self,
        contact_id=None,
        merged_to_contact_id=None,
        contact_number=None,
        account_number=None,
        contact_status=None,
        name=None,
        first_name=None,
        last_name=None,
        company_number=None,
        email_address=None,
        contact_persons=None,
        bank_account_details=None,
        tax_number=None,
        accounts_receivable_tax_type=None,
        accounts_payable_tax_type=None,
        addresses=None,
        phones=None,
        is_supplier=None,
        is_customer=None,
        sales_default_line_amount_type=None,
        purchases_default_line_amount_type=None,
        default_currency=None,
        xero_network_key=None,
        sales_default_account_code=None,
        purchases_default_account_code=None,
        sales_tracking_categories=None,
        purchases_tracking_categories=None,
        tracking_category_name=None,
        tracking_category_option=None,
        payment_terms=None,
        updated_date_utc=None,
        contact_groups=None,
        website=None,
        branding_theme=None,
        batch_payments=None,
        discount=None,
        balances=None,
        attachments=None,
        has_attachments=False,
        validation_errors=None,
        has_validation_errors=False,
        status_attribute_string=None,
    ):
        self._contact_id = None
        self._merged_to_contact_id = None
        self._contact_number = None
        self._account_number = None
        self._contact_status = None
        self._name = None
        self._first_name = None
        self._last_name = None
        self._company_number = None
        self._email_address = None
        self._contact_persons = None
        self._bank_account_details = None
        self._tax_number = None
        self._accounts_receivable_tax_type = None
        self._accounts_payable_tax_type = None
        self._addresses = None
        self._phones = None
        self._is_supplier = None
        self._is_customer = None
        self._sales_default_line_amount_type = None
        self._purchases_default_line_amount_type = None
        self._default_currency = None
        self._xero_network_key = None
        self._sales_default_account_code = None
        self._purchases_default_account_code = None
        self._sales_tracking_categories = None
        self._purchases_tracking_categories = None
        self._tracking_category_name = None
        self._tracking_category_option = None
        self._payment_terms = None
        self._updated_date_utc = None
        self._contact_groups = None
        self._website = None
        self._branding_theme = None
        self._batch_payments = None
        self._discount = None
        self._balances = None
        self._attachments = None
        self._has_attachments = None
        self._validation_errors = None
        self._has_validation_errors = None
        self._status_attribute_string = None
        self.discriminator = None
        if contact_id is not None:
            self.contact_id = contact_id
        if merged_to_contact_id is not None:
            self.merged_to_contact_id = merged_to_contact_id
        if contact_number is not None:
            self.contact_number = contact_number
        if account_number is not None:
            self.account_number = account_number
        if contact_status is not None:
            self.contact_status = contact_status
        if name is not None:
            self.name = name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if company_number is not None:
            self.company_number = company_number
        if email_address is not None:
            self.email_address = email_address
        if contact_persons is not None:
            self.contact_persons = contact_persons
        if bank_account_details is not None:
            self.bank_account_details = bank_account_details
        if tax_number is not None:
            self.tax_number = tax_number
        if accounts_receivable_tax_type is not None:
            self.accounts_receivable_tax_type = accounts_receivable_tax_type
        if accounts_payable_tax_type is not None:
            self.accounts_payable_tax_type = accounts_payable_tax_type
        if addresses is not None:
            self.addresses = addresses
        if phones is not None:
            self.phones = phones
        if is_supplier is not None:
            self.is_supplier = is_supplier
        if is_customer is not None:
            self.is_customer = is_customer
        if sales_default_line_amount_type is not None:
            self.sales_default_line_amount_type = sales_default_line_amount_type
        if purchases_default_line_amount_type is not None:
            self.purchases_default_line_amount_type = purchases_default_line_amount_type
        if default_currency is not None:
            self.default_currency = default_currency
        if xero_network_key is not None:
            self.xero_network_key = xero_network_key
        if sales_default_account_code is not None:
            self.sales_default_account_code = sales_default_account_code
        if purchases_default_account_code is not None:
            self.purchases_default_account_code = purchases_default_account_code
        if sales_tracking_categories is not None:
            self.sales_tracking_categories = sales_tracking_categories
        if purchases_tracking_categories is not None:
            self.purchases_tracking_categories = purchases_tracking_categories
        if tracking_category_name is not None:
            self.tracking_category_name = tracking_category_name
        if tracking_category_option is not None:
            self.tracking_category_option = tracking_category_option
        if payment_terms is not None:
            self.payment_terms = payment_terms
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if contact_groups is not None:
            self.contact_groups = contact_groups
        if website is not None:
            self.website = website
        if branding_theme is not None:
            self.branding_theme = branding_theme
        if batch_payments is not None:
            self.batch_payments = batch_payments
        if discount is not None:
            self.discount = discount
        if balances is not None:
            self.balances = balances
        if attachments is not None:
            self.attachments = attachments
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if has_validation_errors is not None:
            self.has_validation_errors = has_validation_errors
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def merged_to_contact_id(self):
        return self._merged_to_contact_id

    @merged_to_contact_id.setter
    def merged_to_contact_id(self, merged_to_contact_id):
        self._merged_to_contact_id = merged_to_contact_id

    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        if contact_number is not None and len(contact_number) > 50:
            raise ValueError(
                "Invalid value for `contact_number`, "
                "length must be less than or equal to `50`"
            )
        self._contact_number = contact_number

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        if account_number is not None and len(account_number) > 50:
            raise ValueError(
                "Invalid value for `account_number`, "
                "length must be less than or equal to `50`"
            )
        self._account_number = account_number

    @property
    def contact_status(self):
        return self._contact_status

    @contact_status.setter
    def contact_status(self, contact_status):
        allowed_values = ["ACTIVE", "ARCHIVED", "GDPRREQUEST", "None"]
        if contact_status:
            if contact_status not in allowed_values:
                raise ValueError(
                    "Invalid value for `contact_status` ({0}), must be one of {1}".format(
                        contact_status, allowed_values
                    )
                )
        self._contact_status = contact_status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 255:
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `255`"
            )
        self._name = name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name is not None and len(first_name) > 255:
            raise ValueError(
                "Invalid value for `first_name`, "
                "length must be less than or equal to `255`"
            )
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name is not None and len(last_name) > 255:
            raise ValueError(
                "Invalid value for `last_name`, "
                "length must be less than or equal to `255`"
            )
        self._last_name = last_name

    @property
    def company_number(self):
        return self._company_number

    @company_number.setter
    def company_number(self, company_number):
        if company_number is not None and len(company_number) > 50:
            raise ValueError(
                "Invalid value for `company_number`, "
                "length must be less than or equal to `50`"
            )
        self._company_number = company_number

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        if email_address is not None and len(email_address) > 255:
            raise ValueError(
                "Invalid value for `email_address`, "
                "length must be less than or equal to `255`"
            )
        self._email_address = email_address

    @property
    def contact_persons(self):
        return self._contact_persons

    @contact_persons.setter
    def contact_persons(self, contact_persons):
        self._contact_persons = contact_persons

    @property
    def bank_account_details(self):
        return self._bank_account_details

    @bank_account_details.setter
    def bank_account_details(self, bank_account_details):
        self._bank_account_details = bank_account_details

    @property
    def tax_number(self):
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        if tax_number is not None and len(tax_number) > 50:
            raise ValueError(
                "Invalid value for `tax_number`, "
                "length must be less than or equal to `50`"
            )
        self._tax_number = tax_number

    @property
    def accounts_receivable_tax_type(self):
        return self._accounts_receivable_tax_type

    @accounts_receivable_tax_type.setter
    def accounts_receivable_tax_type(self, accounts_receivable_tax_type):
        self._accounts_receivable_tax_type = accounts_receivable_tax_type

    @property
    def accounts_payable_tax_type(self):
        return self._accounts_payable_tax_type

    @accounts_payable_tax_type.setter
    def accounts_payable_tax_type(self, accounts_payable_tax_type):
        self._accounts_payable_tax_type = accounts_payable_tax_type

    @property
    def addresses(self):
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        self._addresses = addresses

    @property
    def phones(self):
        return self._phones

    @phones.setter
    def phones(self, phones):
        self._phones = phones

    @property
    def is_supplier(self):
        return self._is_supplier

    @is_supplier.setter
    def is_supplier(self, is_supplier):
        self._is_supplier = is_supplier

    @property
    def is_customer(self):
        return self._is_customer

    @is_customer.setter
    def is_customer(self, is_customer):
        self._is_customer = is_customer

    @property
    def sales_default_line_amount_type(self):
        return self._sales_default_line_amount_type

    @sales_default_line_amount_type.setter
    def sales_default_line_amount_type(self, sales_default_line_amount_type):
        allowed_values = ["INCLUSIVE", "EXCLUSIVE", "NONE", "None"]
        if sales_default_line_amount_type:
            if sales_default_line_amount_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `sales_default_line_amount_type` ({0}), must be one of {1}".format(
                        sales_default_line_amount_type, allowed_values
                    )
                )
        self._sales_default_line_amount_type = sales_default_line_amount_type

    @property
    def purchases_default_line_amount_type(self):
        return self._purchases_default_line_amount_type

    @purchases_default_line_amount_type.setter
    def purchases_default_line_amount_type(self, purchases_default_line_amount_type):
        allowed_values = ["INCLUSIVE", "EXCLUSIVE", "NONE", "None"]
        if purchases_default_line_amount_type:
            if purchases_default_line_amount_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `purchases_default_line_amount_type` ({0}), must be one of {1}".format(
                        purchases_default_line_amount_type, allowed_values
                    )
                )
        self._purchases_default_line_amount_type = purchases_default_line_amount_type

    @property
    def default_currency(self):
        return self._default_currency

    @default_currency.setter
    def default_currency(self, default_currency):
        self._default_currency = default_currency

    @property
    def xero_network_key(self):
        return self._xero_network_key

    @xero_network_key.setter
    def xero_network_key(self, xero_network_key):
        self._xero_network_key = xero_network_key

    @property
    def sales_default_account_code(self):
        return self._sales_default_account_code

    @sales_default_account_code.setter
    def sales_default_account_code(self, sales_default_account_code):
        self._sales_default_account_code = sales_default_account_code

    @property
    def purchases_default_account_code(self):
        return self._purchases_default_account_code

    @purchases_default_account_code.setter
    def purchases_default_account_code(self, purchases_default_account_code):
        self._purchases_default_account_code = purchases_default_account_code

    @property
    def sales_tracking_categories(self):
        return self._sales_tracking_categories

    @sales_tracking_categories.setter
    def sales_tracking_categories(self, sales_tracking_categories):
        self._sales_tracking_categories = sales_tracking_categories

    @property
    def purchases_tracking_categories(self):
        return self._purchases_tracking_categories

    @purchases_tracking_categories.setter
    def purchases_tracking_categories(self, purchases_tracking_categories):
        self._purchases_tracking_categories = purchases_tracking_categories

    @property
    def tracking_category_name(self):
        return self._tracking_category_name

    @tracking_category_name.setter
    def tracking_category_name(self, tracking_category_name):
        self._tracking_category_name = tracking_category_name

    @property
    def tracking_category_option(self):
        return self._tracking_category_option

    @tracking_category_option.setter
    def tracking_category_option(self, tracking_category_option):
        self._tracking_category_option = tracking_category_option

    @property
    def payment_terms(self):
        return self._payment_terms

    @payment_terms.setter
    def payment_terms(self, payment_terms):
        self._payment_terms = payment_terms

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def contact_groups(self):
        return self._contact_groups

    @contact_groups.setter
    def contact_groups(self, contact_groups):
        self._contact_groups = contact_groups

    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, website):
        self._website = website

    @property
    def branding_theme(self):
        return self._branding_theme

    @branding_theme.setter
    def branding_theme(self, branding_theme):
        self._branding_theme = branding_theme

    @property
    def batch_payments(self):
        return self._batch_payments

    @batch_payments.setter
    def batch_payments(self, batch_payments):
        self._batch_payments = batch_payments

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount

    @property
    def balances(self):
        return self._balances

    @balances.setter
    def balances(self, balances):
        self._balances = balances

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        self._attachments = attachments

    @property
    def has_attachments(self):
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        self._has_attachments = has_attachments

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors

    @property
    def has_validation_errors(self):
        return self._has_validation_errors

    @has_validation_errors.setter
    def has_validation_errors(self, has_validation_errors):
        self._has_validation_errors = has_validation_errors

    @property
    def status_attribute_string(self):
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        self._status_attribute_string = status_attribute_string
