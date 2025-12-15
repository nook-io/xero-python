from xero.models import BaseModel


class Error(BaseModel):
    openapi_types = {"message": "str", "model_state": "object"}
    attribute_map = {"message": "message", "model_state": "modelState"}

    def __init__(self, message=None, model_state=None):
        self._message = None
        self._model_state = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if model_state is not None:
            self.model_state = model_state

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def model_state(self):
        return self._model_state

    @model_state.setter
    def model_state(self, model_state):
        self._model_state = model_state
