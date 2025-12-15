from xero.models import BaseModel


class ValidationError(BaseModel):
    openapi_types = {"message": "str"}
    attribute_map = {"message": "Message"}

    def __init__(self, message=None):
        self._message = None
        self.discriminator = None
        if message is not None:
            self.message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message
