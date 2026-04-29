from __future__ import annotations

from typing import Any


class ApiResponse:
    status_code: int | None = None  # "HTTP status code"
    headers: dict[str, str] | None = None  # HTTP headers
    data: Any | None = None  # Deserialized data given the data type
    raw_data: Any | None = None  # Raw data (HTTP response body)

    def __init__(self, status_code=None, headers=None, data=None, raw_data=None) -> None:
        self.status_code = status_code
        self.headers = headers
        self.data = data
        self.raw_data = raw_data
