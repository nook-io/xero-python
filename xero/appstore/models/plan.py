from xero.models import BaseModel


class Plan(BaseModel):
    openapi_types = {
        "id": "str",
        "name": "str",
        "status": "str",
        "subscription_items": "list[SubscriptionItem]",
    }
    attribute_map = {
        "id": "id",
        "name": "name",
        "status": "status",
        "subscription_items": "subscriptionItems",
    }

    def __init__(self, id=None, name=None, status=None, subscription_items=None):
        self._id = None
        self._name = None
        self._status = None
        self._subscription_items = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.status = status
        self.subscription_items = subscription_items

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        allowed_values = [
            "ACTIVE",
            "CANCELED",
            "PENDING_ACTIVATION",
            "None",
        ]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def subscription_items(self):
        return self._subscription_items

    @subscription_items.setter
    def subscription_items(self, subscription_items):
        if subscription_items is None:
            raise ValueError(
                "Invalid value for `subscription_items`, must not be `None`"
            )
        self._subscription_items = subscription_items
