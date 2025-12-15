from xero.models import BaseModel


class TimesheetObject(BaseModel):
    openapi_types = {"timesheet": "Timesheet"}
    attribute_map = {"timesheet": "Timesheet"}

    def __init__(self, timesheet=None):
        self._timesheet = None
        self.discriminator = None
        if timesheet is not None:
            self.timesheet = timesheet

    @property
    def timesheet(self):
        return self._timesheet

    @timesheet.setter
    def timesheet(self, timesheet):
        self._timesheet = timesheet
