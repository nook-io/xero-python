from xero.models import BaseModel


class BatchPayments(BaseModel):
    openapi_types = {"batch_payments": "list[BatchPayment]"}
    attribute_map = {"batch_payments": "BatchPayments"}

    def __init__(self, batch_payments=None):
        self._batch_payments = None
        self.discriminator = None
        if batch_payments is not None:
            self.batch_payments = batch_payments

    @property
    def batch_payments(self):
        return self._batch_payments

    @batch_payments.setter
    def batch_payments(self, batch_payments):
        self._batch_payments = batch_payments
