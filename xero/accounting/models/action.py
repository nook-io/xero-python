from xero.models import BaseModel


class Action(BaseModel):
    openapi_types = {"name": "str", "status": "str"}
    attribute_map = {"name": "Name", "status": "Status"}

    def __init__(self, name=None, status=None):
        self._name = None
        self._status = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["ALLOWED", "NOT-ALLOWED", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status
