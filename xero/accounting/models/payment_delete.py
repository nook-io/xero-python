from xero.models import BaseModel


class PaymentDelete(BaseModel):
    openapi_types = {"status": "str"}
    attribute_map = {"status": "Status"}

    def __init__(self, status="DELETED"):
        self._status = None
        self.discriminator = None
        self.status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        self._status = status
