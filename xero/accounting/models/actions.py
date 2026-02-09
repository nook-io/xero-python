from xero.models import BaseModel


class Actions(BaseModel):
    openapi_types = {"actions": "list[Action]"}
    attribute_map = {"actions": "Actions"}

    def __init__(self, actions=None):
        self._actions = None
        self.discriminator = None
        if actions is not None:
            self.actions = actions

    @property
    def actions(self):
        return self._actions

    @actions.setter
    def actions(self, actions):
        self._actions = actions
