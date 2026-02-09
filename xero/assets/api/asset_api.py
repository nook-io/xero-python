import importlib
from typing import Optional
from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated
from xero.api_client import ApiClient, ApiResponse, ModelFinder
from xero.assets.models.asset import Asset
from xero.assets.models.asset_status_query_param import AssetStatusQueryParam
from xero.assets.models.asset_type import AssetType
from xero.assets.models.assets import Assets
from xero.assets.models.setting import Setting
from xero.exceptions import (
    ApiTypeError,
)


class AssetApi:
    base_url = "https://api.xero.com/assets.xro/1.0"
    models_module = importlib.import_module("xero.assets.models")

    def __init__(self, api_client=None, base_url: str | None = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    async def create_asset(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        asset: Annotated[Asset, Field(..., description="Fixed asset you are creating")],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> Asset:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_asset_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_asset_with_http_info(
            xero_tenant_id, asset, idempotency_key, **kwargs
        )

    async def create_asset_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        asset: Annotated[Asset, Field(..., description="Fixed asset you are creating")],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "asset", "idempotency_key"]
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
                    " to method create_asset" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["asset"] is not None:
            _body_params = _params["asset"]
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "Asset",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Assets",
            "POST",
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

    async def create_asset_type(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        asset_type: Annotated[AssetType, Field(..., description="Asset type to add")],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> AssetType:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_asset_type_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_asset_type_with_http_info(
            xero_tenant_id, asset_type, idempotency_key, **kwargs
        )

    async def create_asset_type_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        asset_type: Annotated[AssetType, Field(..., description="Asset type to add")],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "asset_type", "idempotency_key"]
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
                    " to method create_asset_type" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["asset_type"] is not None:
            _body_params = _params["asset_type"]
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "AssetType",
            "400": None,
            "409": None,
        }
        return await self.api_client.call_api(
            "/AssetTypes",
            "POST",
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

    async def get_asset_by_id(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        id: Annotated[
            StrictStr, Field(..., description="fixed asset id for single object")
        ],
        **kwargs,
    ) -> Asset:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_asset_by_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_asset_by_id_with_http_info(xero_tenant_id, id, **kwargs)

    async def get_asset_by_id_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        id: Annotated[
            StrictStr, Field(..., description="fixed asset id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "id"]
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
                    " to method get_asset_by_id" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["id"] is not None:
            _path_params["id"] = _params["id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "Asset",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Assets/{id}",
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

    async def get_asset_settings(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        **kwargs,
    ) -> Setting:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_asset_settings_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_asset_settings_with_http_info(xero_tenant_id, **kwargs)

    async def get_asset_settings_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id"]
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
                    " to method get_asset_settings" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "Setting",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Settings",
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

    async def get_asset_types(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        **kwargs,
    ) -> list[AssetType]:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_asset_types_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_asset_types_with_http_info(xero_tenant_id, **kwargs)

    async def get_asset_types_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id"]
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
                    " to method get_asset_types" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "list[AssetType]",
            "400": None,
        }
        return await self.api_client.call_api(
            "/AssetTypes",
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

    async def get_assets(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        status: Annotated[
            AssetStatusQueryParam,
            Field(
                ...,
                description="Required when retrieving a collection of assets. See Asset Status Codes",
            ),
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Results are paged. This specifies which page of the results to return. The default page is 1."
            ),
        ] = None,
        page_size: Annotated[
            Optional[StrictInt],
            Field(
                description="The number of records returned per page. By default the number of records returned is 10."
            ),
        ] = None,
        order_by: Annotated[
            Optional[StrictStr],
            Field(
                description="Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice."
            ),
        ] = None,
        sort_direction: Annotated[
            Optional[StrictStr], Field(description="ASC or DESC")
        ] = None,
        filter_by: Annotated[
            Optional[StrictStr],
            Field(
                description="A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields."
            ),
        ] = None,
        **kwargs,
    ) -> Assets:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_assets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_assets_with_http_info(
            xero_tenant_id,
            status,
            page,
            page_size,
            order_by,
            sort_direction,
            filter_by,
            **kwargs,
        )

    async def get_assets_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        status: Annotated[
            AssetStatusQueryParam,
            Field(
                ...,
                description="Required when retrieving a collection of assets. See Asset Status Codes",
            ),
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Results are paged. This specifies which page of the results to return. The default page is 1."
            ),
        ] = None,
        page_size: Annotated[
            Optional[StrictInt],
            Field(
                description="The number of records returned per page. By default the number of records returned is 10."
            ),
        ] = None,
        order_by: Annotated[
            Optional[StrictStr],
            Field(
                description="Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice."
            ),
        ] = None,
        sort_direction: Annotated[
            Optional[StrictStr], Field(description="ASC or DESC")
        ] = None,
        filter_by: Annotated[
            Optional[StrictStr],
            Field(
                description="A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "status",
            "page",
            "page_size",
            "order_by",
            "sort_direction",
            "filter_by",
        ]
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
                    " to method get_assets" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("status") is not None:
            _query_params.append(("status", _params["status"].value))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        if _params.get("page_size") is not None:
            _query_params.append(("pageSize", _params["page_size"]))
        if _params.get("order_by") is not None:
            _query_params.append(("orderBy", _params["order_by"]))
        if _params.get("sort_direction") is not None:
            _query_params.append(("sortDirection", _params["sort_direction"]))
        if _params.get("filter_by") is not None:
            _query_params.append(("filterBy", _params["filter_by"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "Assets",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Assets",
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
