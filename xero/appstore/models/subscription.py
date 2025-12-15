from xero.models import BaseModel


class Subscription(BaseModel):
    openapi_types = {
        "current_period_end": "datetime",
        "end_date": "datetime",
        "id": "str",
        "organisation_id": "str",
        "plans": "list[Plan]",
        "start_date": "datetime",
        "status": "str",
        "test_mode": "bool",
    }
    attribute_map = {
        "current_period_end": "currentPeriodEnd",
        "end_date": "endDate",
        "id": "id",
        "organisation_id": "organisationId",
        "plans": "plans",
        "start_date": "startDate",
        "status": "status",
        "test_mode": "testMode",
    }

    def __init__(
        self,
        current_period_end=None,
        end_date=None,
        id=None,
        organisation_id=None,
        plans=None,
        start_date=None,
        status=None,
        test_mode=None,
    ):
        self._current_period_end = None
        self._end_date = None
        self._id = None
        self._organisation_id = None
        self._plans = None
        self._start_date = None
        self._status = None
        self._test_mode = None
        self.discriminator = None
        self.current_period_end = current_period_end
        if end_date is not None:
            self.end_date = end_date
        self.id = id
        self.organisation_id = organisation_id
        self.plans = plans
        self.start_date = start_date
        self.status = status
        if test_mode is not None:
            self.test_mode = test_mode

    @property
    def current_period_end(self):
        return self._current_period_end

    @current_period_end.setter
    def current_period_end(self, current_period_end):
        if current_period_end is None:
            raise ValueError(
                "Invalid value for `current_period_end`, must not be `None`"
            )
        self._current_period_end = current_period_end

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        self._id = id

    @property
    def organisation_id(self):
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        if organisation_id is None:
            raise ValueError("Invalid value for `organisation_id`, must not be `None`")
        self._organisation_id = organisation_id

    @property
    def plans(self):
        return self._plans

    @plans.setter
    def plans(self, plans):
        if plans is None:
            raise ValueError("Invalid value for `plans`, must not be `None`")
        self._plans = plans

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")
        self._start_date = start_date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        allowed_values = ["ACTIVE", "CANCELED", "PAST_DUE", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def test_mode(self):
        return self._test_mode

    @test_mode.setter
    def test_mode(self, test_mode):
        self._test_mode = test_mode
