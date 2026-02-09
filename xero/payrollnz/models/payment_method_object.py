from xero.models import BaseModel


class PaymentMethodObject(BaseModel):
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "payment_method": "PaymentMethod",
    }
    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "payment_method": "paymentMethod",
    }

    def __init__(self, pagination=None, problem=None, payment_method=None):
        self._pagination = None
        self._problem = None
        self._payment_method = None
        self.discriminator = None
        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if payment_method is not None:
            self.payment_method = payment_method

    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        self._pagination = pagination

    @property
    def problem(self):
        return self._problem

    @problem.setter
    def problem(self, problem):
        self._problem = problem

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        self._payment_method = payment_method
