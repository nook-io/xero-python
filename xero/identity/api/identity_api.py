import importlib
from typing import Optional
from pydantic import Field, StrictStr
from typing_extensions import Annotated
from xero.api_client import ApiClient, ApiResponse, ModelFinder
from xero.exceptions import (
    ApiTypeError,
)
from xero.identity.models.connection import Connection


class IdentityApi:
    base_url = "https://api.xero.com"
    models_module = importlib.import_module("xero.identity.models")

    def __init__(self, api_client=None, base_url: str | None = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    async def delete_connection(
        self,
        id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for retrieving single object"),
        ],
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_connection_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.delete_connection_with_http_info(id, **kwargs)

    async def delete_connection_with_http_info(
        self,
        id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for retrieving single object"),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["id"]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_connection" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["id"] is not None:
            _path_params["id"] = _params["id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        _form_params = []
        _files = {}
        _body_params = None
        _auth_settings = ["OAuth2"]
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Connections/{id}",
            "DELETE",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            response_model_finder=self.get_model_finder(),
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            _host=self.base_url,
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    async def get_connections(
        self,
        auth_event_id: Annotated[
            Optional[StrictStr], Field(description="Filter by authEventId")
        ] = None,
        **kwargs,
    ) -> list[Connection]:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_connections_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_connections_with_http_info(auth_event_id, **kwargs)

    async def get_connections_with_http_info(
        self,
        auth_event_id: Annotated[
            Optional[StrictStr], Field(description="Filter by authEventId")
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["auth_event_id"]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_connections" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("auth_event_id") is not None:
            _query_params.append(("authEventId", _params["auth_event_id"]))
        _header_params = dict(_params.get("_headers", {}))
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "list[Connection]",
        }
        return await self.api_client.call_api(
            "/Connections",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            response_model_finder=self.get_model_finder(),
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            _host=self.base_url,
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
