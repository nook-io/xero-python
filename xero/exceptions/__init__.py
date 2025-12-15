from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from xero.rest import RESTResponse


class OpenApiException(Exception):
    pass


class ApiException(OpenApiException):
    def __init__(
        self,
        status: int | None = None,
        reason: str | None = None,
        http_resp: "RESTResponse | None" = None,
    ):
        self._status = status
        self._reason = reason
        self.http_resp = http_resp

    @property
    def status(self) -> int | None:
        return self._status or getattr(self.http_resp, "status", None)

    @property
    def reason(self) -> str | None:
        return self._reason or getattr(self.http_resp, "reason", None)

    @property
    def body(self) -> str | None:
        data = getattr(self.http_resp, "data", None)
        if data is not None:
            return data.decode("utf-8")
        return None

    @property
    def headers(self) -> list[tuple[str, str]] | None:
        return self.http_resp.getheaders() if self.http_resp else None

    @property
    def error_message(self) -> str:
        return "({0})\nReason: {1}".format(self.status, self.reason)

    def __str__(self) -> str:
        error_message = self.error_message + "\n"
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)
        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)
        return error_message


class ApiSSLException(ApiException):
    pass


class OAuth2Error(OpenApiException):
    pass


from .http_status_exceptions import *


class AccessTokenExpiredError(OAuth2Error):
    pass


class OAuth2TokenGetterError(OAuth2Error):
    pass


class OAuth2TokenSaverError(OAuth2Error):
    pass


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None, key_type=None):
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None):
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None):
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


def render_path(path_to_item):
    result = ""
    for pth in path_to_item:
        if isinstance(pth, int):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result
