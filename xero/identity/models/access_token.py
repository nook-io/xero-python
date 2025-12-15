from xero.models import BaseModel


class AccessToken(BaseModel):
    openapi_types = {
        "id_token": "str",
        "access_token": "str",
        "expires_in": "int",
        "token_type": "str",
        "refresh_token": "str",
    }
    attribute_map = {
        "id_token": "id_token",
        "access_token": "access_token",
        "expires_in": "expires_in",
        "token_type": "token_type",
        "refresh_token": "refresh_token",
    }

    def __init__(
        self,
        id_token=None,
        access_token=None,
        expires_in=None,
        token_type=None,
        refresh_token=None,
    ):
        self._id_token = None
        self._access_token = None
        self._expires_in = None
        self._token_type = None
        self._refresh_token = None
        self.discriminator = None
        if id_token is not None:
            self.id_token = id_token
        if access_token is not None:
            self.access_token = access_token
        if expires_in is not None:
            self.expires_in = expires_in
        if token_type is not None:
            self.token_type = token_type
        if refresh_token is not None:
            self.refresh_token = refresh_token

    @property
    def id_token(self):
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        self._id_token = id_token

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        self._access_token = access_token

    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        self._expires_in = expires_in

    @property
    def token_type(self):
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        self._token_type = token_type

    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        self._refresh_token = refresh_token
