from xero.models import BaseModel


class Error(BaseModel):
    openapi_types = {
        "error_number": "int",
        "type": "str",
        "message": "str",
        "elements": "list[Element]",
    }
    attribute_map = {
        "error_number": "ErrorNumber",
        "type": "Type",
        "message": "Message",
        "elements": "Elements",
    }

    def __init__(self, error_number=None, type=None, message=None, elements=None):
        self._error_number = None
        self._type = None
        self._message = None
        self._elements = None
        self.discriminator = None
        if error_number is not None:
            self.error_number = error_number
        if type is not None:
            self.type = type
        if message is not None:
            self.message = message
        if elements is not None:
            self.elements = elements

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

    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self, elements):
        self._elements = elements
