from xero.models import BaseModel


class Task(BaseModel):
    openapi_types = {
        "task_id": "str",
        "name": "str",
        "rate": "Amount",
        "charge_type": "ChargeType",
        "estimate_minutes": "int",
        "project_id": "str",
        "total_minutes": "int",
        "total_amount": "Amount",
        "minutes_invoiced": "int",
        "minutes_to_be_invoiced": "int",
        "fixed_minutes": "int",
        "non_chargeable_minutes": "int",
        "amount_to_be_invoiced": "Amount",
        "amount_invoiced": "Amount",
        "status": "str",
    }
    attribute_map = {
        "task_id": "taskId",
        "name": "name",
        "rate": "rate",
        "charge_type": "chargeType",
        "estimate_minutes": "estimateMinutes",
        "project_id": "projectId",
        "total_minutes": "totalMinutes",
        "total_amount": "totalAmount",
        "minutes_invoiced": "minutesInvoiced",
        "minutes_to_be_invoiced": "minutesToBeInvoiced",
        "fixed_minutes": "fixedMinutes",
        "non_chargeable_minutes": "nonChargeableMinutes",
        "amount_to_be_invoiced": "amountToBeInvoiced",
        "amount_invoiced": "amountInvoiced",
        "status": "status",
    }

    def __init__(
        self,
        task_id=None,
        name=None,
        rate=None,
        charge_type=None,
        estimate_minutes=None,
        project_id=None,
        total_minutes=None,
        total_amount=None,
        minutes_invoiced=None,
        minutes_to_be_invoiced=None,
        fixed_minutes=None,
        non_chargeable_minutes=None,
        amount_to_be_invoiced=None,
        amount_invoiced=None,
        status=None,
    ):
        self._task_id = None
        self._name = None
        self._rate = None
        self._charge_type = None
        self._estimate_minutes = None
        self._project_id = None
        self._total_minutes = None
        self._total_amount = None
        self._minutes_invoiced = None
        self._minutes_to_be_invoiced = None
        self._fixed_minutes = None
        self._non_chargeable_minutes = None
        self._amount_to_be_invoiced = None
        self._amount_invoiced = None
        self._status = None
        self.discriminator = None
        if task_id is not None:
            self.task_id = task_id
        if name is not None:
            self.name = name
        if rate is not None:
            self.rate = rate
        if charge_type is not None:
            self.charge_type = charge_type
        if estimate_minutes is not None:
            self.estimate_minutes = estimate_minutes
        if project_id is not None:
            self.project_id = project_id
        if total_minutes is not None:
            self.total_minutes = total_minutes
        if total_amount is not None:
            self.total_amount = total_amount
        if minutes_invoiced is not None:
            self.minutes_invoiced = minutes_invoiced
        if minutes_to_be_invoiced is not None:
            self.minutes_to_be_invoiced = minutes_to_be_invoiced
        if fixed_minutes is not None:
            self.fixed_minutes = fixed_minutes
        if non_chargeable_minutes is not None:
            self.non_chargeable_minutes = non_chargeable_minutes
        if amount_to_be_invoiced is not None:
            self.amount_to_be_invoiced = amount_to_be_invoiced
        if amount_invoiced is not None:
            self.amount_invoiced = amount_invoiced
        if status is not None:
            self.status = status

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        self._task_id = task_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        self._rate = rate

    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        self._charge_type = charge_type

    @property
    def estimate_minutes(self):
        return self._estimate_minutes

    @estimate_minutes.setter
    def estimate_minutes(self, estimate_minutes):
        self._estimate_minutes = estimate_minutes

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        self._project_id = project_id

    @property
    def total_minutes(self):
        return self._total_minutes

    @total_minutes.setter
    def total_minutes(self, total_minutes):
        self._total_minutes = total_minutes

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

    @property
    def minutes_invoiced(self):
        return self._minutes_invoiced

    @minutes_invoiced.setter
    def minutes_invoiced(self, minutes_invoiced):
        self._minutes_invoiced = minutes_invoiced

    @property
    def minutes_to_be_invoiced(self):
        return self._minutes_to_be_invoiced

    @minutes_to_be_invoiced.setter
    def minutes_to_be_invoiced(self, minutes_to_be_invoiced):
        self._minutes_to_be_invoiced = minutes_to_be_invoiced

    @property
    def fixed_minutes(self):
        return self._fixed_minutes

    @fixed_minutes.setter
    def fixed_minutes(self, fixed_minutes):
        self._fixed_minutes = fixed_minutes

    @property
    def non_chargeable_minutes(self):
        return self._non_chargeable_minutes

    @non_chargeable_minutes.setter
    def non_chargeable_minutes(self, non_chargeable_minutes):
        self._non_chargeable_minutes = non_chargeable_minutes

    @property
    def amount_to_be_invoiced(self):
        return self._amount_to_be_invoiced

    @amount_to_be_invoiced.setter
    def amount_to_be_invoiced(self, amount_to_be_invoiced):
        self._amount_to_be_invoiced = amount_to_be_invoiced

    @property
    def amount_invoiced(self):
        return self._amount_invoiced

    @amount_invoiced.setter
    def amount_invoiced(self, amount_invoiced):
        self._amount_invoiced = amount_invoiced

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["ACTIVE", "INVOICED", "LOCKED", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status
