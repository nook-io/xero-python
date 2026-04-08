from typing import TYPE_CHECKING

from multidict import CIMultiDictProxy

if TYPE_CHECKING:
    from xero.rest import RESTResponse


class OpenApiException(Exception):
    pass


class HTTPStatusException(OpenApiException):
    def __init__(
        self,
        http_resp: "RESTResponse",
    ):
        self.http_resp = http_resp

    @property
    def status(self) -> int:
        return self.http_resp.status

    @property
    def reason(self) -> str | None:
        return self.http_resp.reason

    @property
    def body(self) -> str | None:
        data = self.http_resp.data
        if data is None:
            return None
        return data.decode("utf-8")

    @property
    def headers(self) -> CIMultiDictProxy[str]:
        return self.http_resp.getheaders()

    @property
    def error_message(self) -> str:
        return f"({self.status})\nReason: {self.reason}"

    def __str__(self) -> str:
        error_message = self.error_message + "\n"
        if self.headers:
            error_message += f"HTTP response headers: {self.headers}\n"
        if self.body:
            error_message += f"HTTP response body: {self.body}\n"
        return error_message


class OAuth2Error(OpenApiException):
    pass


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
            full_msg = f"{msg} at {render_path(path_to_item)}"
        super().__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None):
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = f"{msg} at {render_path(path_to_item)}"
        super().__init__(full_msg)


def render_path(path_to_item):
    result = ""
    for pth in path_to_item:
        if isinstance(pth, int):
            result += f"[{pth}]"
        else:
            result += f"['{pth}']"
    return result
