from xero.models import BaseModel


class TimeEntryCreateOrUpdate(BaseModel):
    openapi_types = {
        "user_id": "str",
        "task_id": "str",
        "date_utc": "datetime",
        "duration": "int",
        "description": "str",
    }
    attribute_map = {
        "user_id": "userId",
        "task_id": "taskId",
        "date_utc": "dateUtc",
        "duration": "duration",
        "description": "description",
    }

    def __init__(
        self, user_id=None, task_id=None, date_utc=None, duration=None, description=None
    ):
        self._user_id = None
        self._task_id = None
        self._date_utc = None
        self._duration = None
        self._description = None
        self.discriminator = None
        self.user_id = user_id
        self.task_id = task_id
        self.date_utc = date_utc
        self.duration = duration
        if description is not None:
            self.description = description

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")
        self._user_id = user_id

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        if task_id is None:
            raise ValueError("Invalid value for `task_id`, must not be `None`")
        self._task_id = task_id

    @property
    def date_utc(self):
        return self._date_utc

    @date_utc.setter
    def date_utc(self, date_utc):
        if date_utc is None:
            raise ValueError("Invalid value for `date_utc`, must not be `None`")
        self._date_utc = date_utc

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")
        self._duration = duration

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description
