from xero.models import BaseModel


class TimeEntry(BaseModel):
    openapi_types = {
        "time_entry_id": "str",
        "user_id": "str",
        "project_id": "str",
        "task_id": "str",
        "date_utc": "datetime",
        "date_entered_utc": "datetime",
        "duration": "int",
        "description": "str",
        "status": "str",
    }
    attribute_map = {
        "time_entry_id": "timeEntryId",
        "user_id": "userId",
        "project_id": "projectId",
        "task_id": "taskId",
        "date_utc": "dateUtc",
        "date_entered_utc": "dateEnteredUtc",
        "duration": "duration",
        "description": "description",
        "status": "status",
    }

    def __init__(
        self,
        time_entry_id=None,
        user_id=None,
        project_id=None,
        task_id=None,
        date_utc=None,
        date_entered_utc=None,
        duration=None,
        description=None,
        status=None,
    ):
        self._time_entry_id = None
        self._user_id = None
        self._project_id = None
        self._task_id = None
        self._date_utc = None
        self._date_entered_utc = None
        self._duration = None
        self._description = None
        self._status = None
        self.discriminator = None
        if time_entry_id is not None:
            self.time_entry_id = time_entry_id
        if user_id is not None:
            self.user_id = user_id
        if project_id is not None:
            self.project_id = project_id
        if task_id is not None:
            self.task_id = task_id
        if date_utc is not None:
            self.date_utc = date_utc
        if date_entered_utc is not None:
            self.date_entered_utc = date_entered_utc
        if duration is not None:
            self.duration = duration
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status

    @property
    def time_entry_id(self):
        return self._time_entry_id

    @time_entry_id.setter
    def time_entry_id(self, time_entry_id):
        self._time_entry_id = time_entry_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        self._project_id = project_id

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        self._task_id = task_id

    @property
    def date_utc(self):
        return self._date_utc

    @date_utc.setter
    def date_utc(self, date_utc):
        self._date_utc = date_utc

    @property
    def date_entered_utc(self):
        return self._date_entered_utc

    @date_entered_utc.setter
    def date_entered_utc(self, date_entered_utc):
        self._date_entered_utc = date_entered_utc

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["ACTIVE", "LOCKED", "INVOICED", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status
