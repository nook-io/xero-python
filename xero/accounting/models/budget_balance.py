from xero.models import BaseModel


class BudgetBalance(BaseModel):
    openapi_types = {
        "period": "date[ms-format]",
        "amount": "float",
        "unit_amount": "float",
        "notes": "str",
    }
    attribute_map = {
        "period": "Period",
        "amount": "Amount",
        "unit_amount": "UnitAmount",
        "notes": "Notes",
    }

    def __init__(self, period=None, amount=None, unit_amount=None, notes=None):
        self._period = None
        self._amount = None
        self._unit_amount = None
        self._notes = None
        self.discriminator = None
        if period is not None:
            self.period = period
        if amount is not None:
            self.amount = amount
        if unit_amount is not None:
            self.unit_amount = unit_amount
        if notes is not None:
            self.notes = notes

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, period):
        self._period = period

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def unit_amount(self):
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, unit_amount):
        self._unit_amount = unit_amount

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        if notes is not None and len(notes) > 255:
            raise ValueError(
                "Invalid value for `notes`, length must be less than or equal to `255`"
            )
        self._notes = notes
