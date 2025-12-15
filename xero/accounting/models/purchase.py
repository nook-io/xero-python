from xero.models import BaseModel


class Purchase(BaseModel):
    openapi_types = {
        "unit_price": "float",
        "account_code": "str",
        "cogs_account_code": "str",
        "tax_type": "str",
    }
    attribute_map = {
        "unit_price": "UnitPrice",
        "account_code": "AccountCode",
        "cogs_account_code": "COGSAccountCode",
        "tax_type": "TaxType",
    }

    def __init__(
        self, unit_price=None, account_code=None, cogs_account_code=None, tax_type=None
    ):
        self._unit_price = None
        self._account_code = None
        self._cogs_account_code = None
        self._tax_type = None
        self.discriminator = None
        if unit_price is not None:
            self.unit_price = unit_price
        if account_code is not None:
            self.account_code = account_code
        if cogs_account_code is not None:
            self.cogs_account_code = cogs_account_code
        if tax_type is not None:
            self.tax_type = tax_type

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property
    def account_code(self):
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        self._account_code = account_code

    @property
    def cogs_account_code(self):
        return self._cogs_account_code

    @cogs_account_code.setter
    def cogs_account_code(self, cogs_account_code):
        self._cogs_account_code = cogs_account_code

    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        self._tax_type = tax_type
