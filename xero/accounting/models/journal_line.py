from xero.models import BaseModel


class JournalLine(BaseModel):
    openapi_types = {
        "journal_line_id": "str",
        "account_id": "str",
        "account_code": "str",
        "account_type": "AccountType",
        "account_name": "str",
        "description": "str",
        "net_amount": "float",
        "gross_amount": "float",
        "tax_amount": "float",
        "tax_type": "str",
        "tax_name": "str",
        "tracking_categories": "list[TrackingCategory]",
    }
    attribute_map = {
        "journal_line_id": "JournalLineID",
        "account_id": "AccountID",
        "account_code": "AccountCode",
        "account_type": "AccountType",
        "account_name": "AccountName",
        "description": "Description",
        "net_amount": "NetAmount",
        "gross_amount": "GrossAmount",
        "tax_amount": "TaxAmount",
        "tax_type": "TaxType",
        "tax_name": "TaxName",
        "tracking_categories": "TrackingCategories",
    }

    def __init__(
        self,
        journal_line_id=None,
        account_id=None,
        account_code=None,
        account_type=None,
        account_name=None,
        description=None,
        net_amount=None,
        gross_amount=None,
        tax_amount=None,
        tax_type=None,
        tax_name=None,
        tracking_categories=None,
    ):
        self._journal_line_id = None
        self._account_id = None
        self._account_code = None
        self._account_type = None
        self._account_name = None
        self._description = None
        self._net_amount = None
        self._gross_amount = None
        self._tax_amount = None
        self._tax_type = None
        self._tax_name = None
        self._tracking_categories = None
        self.discriminator = None
        if journal_line_id is not None:
            self.journal_line_id = journal_line_id
        if account_id is not None:
            self.account_id = account_id
        if account_code is not None:
            self.account_code = account_code
        if account_type is not None:
            self.account_type = account_type
        if account_name is not None:
            self.account_name = account_name
        if description is not None:
            self.description = description
        if net_amount is not None:
            self.net_amount = net_amount
        if gross_amount is not None:
            self.gross_amount = gross_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if tax_type is not None:
            self.tax_type = tax_type
        if tax_name is not None:
            self.tax_name = tax_name
        if tracking_categories is not None:
            self.tracking_categories = tracking_categories

    @property
    def journal_line_id(self):
        return self._journal_line_id

    @journal_line_id.setter
    def journal_line_id(self, journal_line_id):
        self._journal_line_id = journal_line_id

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def account_code(self):
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        self._account_code = account_code

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        self._account_type = account_type

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        self._account_name = account_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def net_amount(self):
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        self._net_amount = net_amount

    @property
    def gross_amount(self):
        return self._gross_amount

    @gross_amount.setter
    def gross_amount(self, gross_amount):
        self._gross_amount = gross_amount

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        self._tax_amount = tax_amount

    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        self._tax_type = tax_type

    @property
    def tax_name(self):
        return self._tax_name

    @tax_name.setter
    def tax_name(self, tax_name):
        self._tax_name = tax_name

    @property
    def tracking_categories(self):
        return self._tracking_categories

    @tracking_categories.setter
    def tracking_categories(self, tracking_categories):
        self._tracking_categories = tracking_categories
