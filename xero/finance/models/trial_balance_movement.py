from xero.models import BaseModel


class TrialBalanceMovement(BaseModel):
    openapi_types = {
        "debits": "float",
        "credits": "float",
        "movement": "TrialBalanceEntry",
        "signed_movement": "float",
    }
    attribute_map = {
        "debits": "debits",
        "credits": "credits",
        "movement": "movement",
        "signed_movement": "signedMovement",
    }

    def __init__(self, debits=None, credits=None, movement=None, signed_movement=None):
        self._debits = None
        self._credits = None
        self._movement = None
        self._signed_movement = None
        self.discriminator = None
        if debits is not None:
            self.debits = debits
        if credits is not None:
            self.credits = credits
        if movement is not None:
            self.movement = movement
        if signed_movement is not None:
            self.signed_movement = signed_movement

    @property
    def debits(self):
        return self._debits

    @debits.setter
    def debits(self, debits):
        self._debits = debits

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, credits):
        self._credits = credits

    @property
    def movement(self):
        return self._movement

    @movement.setter
    def movement(self, movement):
        self._movement = movement

    @property
    def signed_movement(self):
        return self._signed_movement

    @signed_movement.setter
    def signed_movement(self, signed_movement):
        self._signed_movement = signed_movement
