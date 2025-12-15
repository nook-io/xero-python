from xero.models import BaseModel


class LineItem(BaseModel):
    openapi_types = {
        "line_item_id": "str",
        "description": "str",
        "quantity": "float",
        "unit_amount": "float",
        "item_code": "str",
        "account_code": "str",
        "account_id": "str",
        "tax_type": "str",
        "tax_amount": "float",
        "item": "LineItemItem",
        "line_amount": "float",
        "tracking": "list[LineItemTracking]",
        "discount_rate": "float",
        "discount_amount": "float",
        "repeating_invoice_id": "str",
        "taxability": "str",
        "sales_tax_code_id": "float",
        "tax_breakdown": "list[TaxBreakdownComponent]",
    }
    attribute_map = {
        "line_item_id": "LineItemID",
        "description": "Description",
        "quantity": "Quantity",
        "unit_amount": "UnitAmount",
        "item_code": "ItemCode",
        "account_code": "AccountCode",
        "account_id": "AccountID",
        "tax_type": "TaxType",
        "tax_amount": "TaxAmount",
        "item": "Item",
        "line_amount": "LineAmount",
        "tracking": "Tracking",
        "discount_rate": "DiscountRate",
        "discount_amount": "DiscountAmount",
        "repeating_invoice_id": "RepeatingInvoiceID",
        "taxability": "Taxability",
        "sales_tax_code_id": "SalesTaxCodeId",
        "tax_breakdown": "TaxBreakdown",
    }

    def __init__(
        self,
        line_item_id=None,
        description=None,
        quantity=None,
        unit_amount=None,
        item_code=None,
        account_code=None,
        account_id=None,
        tax_type=None,
        tax_amount=None,
        item=None,
        line_amount=None,
        tracking=None,
        discount_rate=None,
        discount_amount=None,
        repeating_invoice_id=None,
        taxability=None,
        sales_tax_code_id=None,
        tax_breakdown=None,
    ):
        self._line_item_id = None
        self._description = None
        self._quantity = None
        self._unit_amount = None
        self._item_code = None
        self._account_code = None
        self._account_id = None
        self._tax_type = None
        self._tax_amount = None
        self._item = None
        self._line_amount = None
        self._tracking = None
        self._discount_rate = None
        self._discount_amount = None
        self._repeating_invoice_id = None
        self._taxability = None
        self._sales_tax_code_id = None
        self._tax_breakdown = None
        self.discriminator = None
        if line_item_id is not None:
            self.line_item_id = line_item_id
        if description is not None:
            self.description = description
        if quantity is not None:
            self.quantity = quantity
        if unit_amount is not None:
            self.unit_amount = unit_amount
        if item_code is not None:
            self.item_code = item_code
        if account_code is not None:
            self.account_code = account_code
        if account_id is not None:
            self.account_id = account_id
        if tax_type is not None:
            self.tax_type = tax_type
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if item is not None:
            self.item = item
        if line_amount is not None:
            self.line_amount = line_amount
        if tracking is not None:
            self.tracking = tracking
        if discount_rate is not None:
            self.discount_rate = discount_rate
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if repeating_invoice_id is not None:
            self.repeating_invoice_id = repeating_invoice_id
        if taxability is not None:
            self.taxability = taxability
        if sales_tax_code_id is not None:
            self.sales_tax_code_id = sales_tax_code_id
        if tax_breakdown is not None:
            self.tax_breakdown = tax_breakdown

    @property
    def line_item_id(self):
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        self._line_item_id = line_item_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def unit_amount(self):
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, unit_amount):
        self._unit_amount = unit_amount

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        self._item_code = item_code

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
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        self._tax_type = tax_type

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        self._tax_amount = tax_amount

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def line_amount(self):
        return self._line_amount

    @line_amount.setter
    def line_amount(self, line_amount):
        self._line_amount = line_amount

    @property
    def tracking(self):
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        self._tracking = tracking

    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, discount_rate):
        self._discount_rate = discount_rate

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        self._discount_amount = discount_amount

    @property
    def repeating_invoice_id(self):
        return self._repeating_invoice_id

    @repeating_invoice_id.setter
    def repeating_invoice_id(self, repeating_invoice_id):
        self._repeating_invoice_id = repeating_invoice_id

    @property
    def taxability(self):
        return self._taxability

    @taxability.setter
    def taxability(self, taxability):
        allowed_values = [
            "TAXABLE",
            "NON_TAXABLE",
            "EXEMPT",
            "PART_TAXABLE",
            "NOT_APPLICABLE",
            "None",
        ]
        if taxability:
            if taxability not in allowed_values:
                raise ValueError(
                    "Invalid value for `taxability` ({0}), must be one of {1}".format(
                        taxability, allowed_values
                    )
                )
        self._taxability = taxability

    @property
    def sales_tax_code_id(self):
        return self._sales_tax_code_id

    @sales_tax_code_id.setter
    def sales_tax_code_id(self, sales_tax_code_id):
        self._sales_tax_code_id = sales_tax_code_id

    @property
    def tax_breakdown(self):
        return self._tax_breakdown

    @tax_breakdown.setter
    def tax_breakdown(self, tax_breakdown):
        self._tax_breakdown = tax_breakdown
