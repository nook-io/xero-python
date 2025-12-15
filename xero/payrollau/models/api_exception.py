from xero.models import BaseModel


class APIException(BaseModel):
    openapi_types = {"error_number": "float", "type": "str", "message": "str"}
    attribute_map = {
        "error_number": "ErrorNumber",
        "type": "Type",
        "message": "Message",
    }

    def __init__(self, error_number=None, type=None, message=None):
        self._error_number = None
        self._type = None
        self._message = None
        self.discriminator = None
        if error_number is not None:
            self.error_number = error_number
        if type is not None:
            self.type = type
        if message is not None:
            self.message = message

    @property
    def error_number(self):
        return self._error_number

    @error_number.setter
    def error_number(self, error_number):
        self._error_number = error_number

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message
