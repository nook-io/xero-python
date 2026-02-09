from xero.models import BaseModel


class ProjectCreateOrUpdate(BaseModel):
    openapi_types = {
        "contact_id": "str",
        "name": "str",
        "estimate_amount": "float",
        "deadline_utc": "datetime",
    }
    attribute_map = {
        "contact_id": "contactId",
        "name": "name",
        "estimate_amount": "estimateAmount",
        "deadline_utc": "deadlineUtc",
    }

    def __init__(
        self, contact_id=None, name=None, estimate_amount=None, deadline_utc=None
    ):
        self._contact_id = None
        self._name = None
        self._estimate_amount = None
        self._deadline_utc = None
        self.discriminator = None
        if contact_id is not None:
            self.contact_id = contact_id
        self.name = name
        if estimate_amount is not None:
            self.estimate_amount = estimate_amount
        if deadline_utc is not None:
            self.deadline_utc = deadline_utc

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def estimate_amount(self):
        return self._estimate_amount

    @estimate_amount.setter
    def estimate_amount(self, estimate_amount):
        self._estimate_amount = estimate_amount

    @property
    def deadline_utc(self):
        return self._deadline_utc

    @deadline_utc.setter
    def deadline_utc(self, deadline_utc):
        self._deadline_utc = deadline_utc
