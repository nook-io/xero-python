from xero.models import BaseModel


class BatchPaymentDelete(BaseModel):
    openapi_types = {"batch_payment_id": "str", "status": "str"}
    attribute_map = {"batch_payment_id": "BatchPaymentID", "status": "Status"}

    def __init__(self, batch_payment_id=None, status="DELETED"):
        self._batch_payment_id = None
        self._status = None
        self.discriminator = None
        self.batch_payment_id = batch_payment_id
        self.status = status

    @property
    def batch_payment_id(self):
        return self._batch_payment_id

    @batch_payment_id.setter
    def batch_payment_id(self, batch_payment_id):
        if batch_payment_id is None:
            raise ValueError("Invalid value for `batch_payment_id`, must not be `None`")
        self._batch_payment_id = batch_payment_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        self._status = status
