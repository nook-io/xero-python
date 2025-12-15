from xero.models import BaseModel


class ManualJournalLine(BaseModel):
    openapi_types = {
        "line_amount": "float",
        "account_code": "str",
        "account_id": "str",
        "description": "str",
        "tax_type": "str",
        "tracking": "list[TrackingCategory]",
        "tax_amount": "float",
        "is_blank": "bool",
    }
    attribute_map = {
        "line_amount": "LineAmount",
        "account_code": "AccountCode",
        "account_id": "AccountID",
        "description": "Description",
        "tax_type": "TaxType",
        "tracking": "Tracking",
        "tax_amount": "TaxAmount",
        "is_blank": "IsBlank",
    }

    def __init__(
        self,
        line_amount=None,
        account_code=None,
        account_id=None,
        description=None,
        tax_type=None,
        tracking=None,
        tax_amount=None,
        is_blank=None,
    ):
        self._line_amount = None
        self._account_code = None
        self._account_id = None
        self._description = None
        self._tax_type = None
        self._tracking = None
        self._tax_amount = None
        self._is_blank = None
        self.discriminator = None
        if line_amount is not None:
            self.line_amount = line_amount
        if account_code is not None:
            self.account_code = account_code
        if account_id is not None:
            self.account_id = account_id
        if description is not None:
            self.description = description
        if tax_type is not None:
            self.tax_type = tax_type
        if tracking is not None:
            self.tracking = tracking
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if is_blank is not None:
            self.is_blank = is_blank

    @property
    def line_amount(self):
        return self._line_amount

    @line_amount.setter
    def line_amount(self, line_amount):
        self._line_amount = line_amount

    @property
    def account_code(self):
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        self._account_code = account_code

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        self._tax_type = tax_type

    @property
    def tracking(self):
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        self._tracking = tracking

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        self._tax_amount = tax_amount

    @property
    def is_blank(self):
        return self._is_blank

    @is_blank.setter
    def is_blank(self, is_blank):
        self._is_blank = is_blank
