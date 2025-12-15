from xero.models import BaseModel


class RequestEmpty(BaseModel):
    openapi_types = {"status": "str"}
    attribute_map = {"status": "Status"}

    def __init__(self, status=None):
        self._status = None
        self.discriminator = None
        if status is not None:
            self.status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
