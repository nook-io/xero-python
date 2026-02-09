from xero.models import BaseModel


class PurchaseOrders(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "warnings": "list[ValidationError]",
        "purchase_orders": "list[PurchaseOrder]",
    }
    attribute_map = {
        "pagination": "pagination",
        "warnings": "Warnings",
        "purchase_orders": "PurchaseOrders",
    }

    def __init__(self, pagination=None, warnings=None, purchase_orders=None):
        self._pagination = None
        self._warnings = None
        self._purchase_orders = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if warnings is not None:
            self.warnings = warnings
        if purchase_orders is not None:
            self.purchase_orders = purchase_orders

    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        self._pagination = pagination

    @property
    def warnings(self):
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        self._warnings = warnings

    @property
    def purchase_orders(self):
        return self._purchase_orders

    @purchase_orders.setter
    def purchase_orders(self, purchase_orders):
        self._purchase_orders = purchase_orders
