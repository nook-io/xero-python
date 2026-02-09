from xero.models import BaseModel


class EmployeeWorkingPatternWithWorkingWeeksRequest(BaseModel):
    openapi_types = {"effective_from": "date", "working_weeks": "list[WorkingWeek]"}
    attribute_map = {"effective_from": "effectiveFrom", "working_weeks": "workingWeeks"}

    def __init__(self, effective_from=None, working_weeks=None):
        self._effective_from = None
        self._working_weeks = None
        self.discriminator = None
        self.effective_from = effective_from
        self.working_weeks = working_weeks

    @property
    def effective_from(self):
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        if effective_from is None:
            raise ValueError("Invalid value for `effective_from`, must not be `None`")
        self._effective_from = effective_from

    @property
    def working_weeks(self):
        return self._working_weeks

    @working_weeks.setter
    def working_weeks(self, working_weeks):
        if working_weeks is None:
            raise ValueError("Invalid value for `working_weeks`, must not be `None`")
        self._working_weeks = working_weeks
