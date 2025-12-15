from xero.models import BaseModel


class Connection(BaseModel):
    openapi_types = {
        "id": "str",
        "tenant_id": "str",
        "auth_event_id": "str",
        "tenant_type": "str",
        "tenant_name": "str",
        "created_date_utc": "datetime",
        "updated_date_utc": "datetime",
    }
    attribute_map = {
        "id": "id",
        "tenant_id": "tenantId",
        "auth_event_id": "authEventId",
        "tenant_type": "tenantType",
        "tenant_name": "tenantName",
        "created_date_utc": "createdDateUtc",
        "updated_date_utc": "updatedDateUtc",
    }

    def __init__(
        self,
        id=None,
        tenant_id=None,
        auth_event_id=None,
        tenant_type=None,
        tenant_name=None,
        created_date_utc=None,
        updated_date_utc=None,
    ):
        self._id = None
        self._tenant_id = None
        self._auth_event_id = None
        self._tenant_type = None
        self._tenant_name = None
        self._created_date_utc = None
        self._updated_date_utc = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if auth_event_id is not None:
            self.auth_event_id = auth_event_id
        if tenant_type is not None:
            self.tenant_type = tenant_type
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        self._tenant_id = tenant_id

    @property
    def auth_event_id(self):
        return self._auth_event_id

    @auth_event_id.setter
    def auth_event_id(self, auth_event_id):
        self._auth_event_id = auth_event_id

    @property
    def tenant_type(self):
        return self._tenant_type

    @tenant_type.setter
    def tenant_type(self, tenant_type):
        self._tenant_type = tenant_type

    @property
    def tenant_name(self):
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        self._tenant_name = tenant_name

    @property
    def created_date_utc(self):
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        self._created_date_utc = created_date_utc

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc
