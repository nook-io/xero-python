from xero.models import BaseModel


class RefreshToken(BaseModel):
    openapi_types = {
        "grant_type": "str",
        "refresh_token": "str",
        "client_id": "str",
        "client_secret": "str",
    }
    attribute_map = {
        "grant_type": "grant_type",
        "refresh_token": "refresh_token",
        "client_id": "client_id",
        "client_secret": "client_secret",
    }

    def __init__(
        self, grant_type=None, refresh_token=None, client_id=None, client_secret=None
    ):
        self._grant_type = None
        self._refresh_token = None
        self._client_id = None
        self._client_secret = None
        self.discriminator = None
        if grant_type is not None:
            self.grant_type = grant_type
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret

    @property
    def grant_type(self):
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        self._grant_type = grant_type

    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        self._refresh_token = refresh_token

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        self._client_id = client_id

    @property
    def client_secret(self):
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        self._client_secret = client_secret
