from xero.models import BaseModel


class Timesheets(BaseModel):
    openapi_types = {"timesheets": "list[Timesheet]"}
    attribute_map = {"timesheets": "Timesheets"}

    def __init__(self, timesheets=None):
        self._timesheets = None
        self.discriminator = None
        if timesheets is not None:
            self.timesheets = timesheets

    @property
    def timesheets(self):
        return self._timesheets

    @timesheets.setter
    def timesheets(self, timesheets):
        self._timesheets = timesheets
