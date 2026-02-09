import importlib
from typing import Optional, Union
from pydantic import (
    Field,
    StrictBytes,
    StrictStr,
    conint,
    conlist,
)
from typing_extensions import Annotated
from xero.api_client import ApiClient, ApiResponse, ModelFinder
from xero.exceptions import (
    ApiTypeError,
)
from xero.file.models.association import Association
from xero.file.models.file_object import FileObject
from xero.file.models.files import Files
from xero.file.models.folder import Folder


class FilesApi:
    base_url = "https://api.xero.com/files.xro/1.0"
    models_module = importlib.import_module("xero.file.models")

    def __init__(self, api_client=None, base_url: str | None = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    async def create_file_association(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        association: Association,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> Association:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_file_association_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_file_association_with_http_info(
            xero_tenant_id, file_id, association, idempotency_key, **kwargs
        )

    async def create_file_association_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        association: Association,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "file_id", "association", "idempotency_key"]
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
                    " to method create_file_association" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["file_id"] is not None:
            _path_params["FileId"] = _params["file_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["association"] is not None:
            _body_params = _params["association"]
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
            "201": "Association",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Files/{FileId}/Associations",
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

    async def create_folder(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        folder: Folder,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> Folder:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_folder_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_folder_with_http_info(
            xero_tenant_id, folder, idempotency_key, **kwargs
        )

    async def create_folder_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        folder: Folder,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "folder", "idempotency_key"]
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
                    " to method create_folder" % _key
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
        if _params["folder"] is not None:
            _body_params = _params["folder"]
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
            "200": "Folder",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Folders",
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

    async def delete_file(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_file_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.delete_file_with_http_info(xero_tenant_id, file_id, **kwargs)

    async def delete_file_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "file_id"]
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
                    " to method delete_file" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["file_id"] is not None:
            _path_params["FileId"] = _params["file_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _auth_settings = ["OAuth2"]
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Files/{FileId}",
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

    async def delete_file_association(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        object_id: Annotated[
            StrictStr, Field(..., description="Object id for single object")
        ],
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_file_association_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.delete_file_association_with_http_info(
            xero_tenant_id, file_id, object_id, **kwargs
        )

    async def delete_file_association_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        object_id: Annotated[
            StrictStr, Field(..., description="Object id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "file_id", "object_id"]
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
                    " to method delete_file_association" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["file_id"] is not None:
            _path_params["FileId"] = _params["file_id"]
        if _params["object_id"] is not None:
            _path_params["ObjectId"] = _params["object_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _auth_settings = ["OAuth2"]
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Files/{FileId}/Associations/{ObjectId}",
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

    async def delete_folder(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        folder_id: Annotated[
            StrictStr, Field(..., description="Folder id for single object")
        ],
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_folder_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.delete_folder_with_http_info(
            xero_tenant_id, folder_id, **kwargs
        )

    async def delete_folder_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        folder_id: Annotated[
            StrictStr, Field(..., description="Folder id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "folder_id"]
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
                    " to method delete_folder" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["folder_id"] is not None:
            _path_params["FolderId"] = _params["folder_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _auth_settings = ["OAuth2"]
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Folders/{FolderId}",
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

    async def get_associations_by_object(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        object_id: Annotated[
            StrictStr, Field(..., description="Object id for single object")
        ],
        pagesize: Annotated[
            Optional[conint(strict=True, le=100)],
            Field(description="pass an optional page size value"),
        ] = None,
        page: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="number of records to skip for pagination"),
        ] = None,
        sort: Annotated[
            Optional[StrictStr], Field(description="values to sort by")
        ] = None,
        direction: Annotated[
            Optional[StrictStr], Field(description="direction to sort by")
        ] = None,
        **kwargs,
    ) -> list[Association]:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_associations_by_object_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_associations_by_object_with_http_info(
            xero_tenant_id, object_id, pagesize, page, sort, direction, **kwargs
        )

    async def get_associations_by_object_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        object_id: Annotated[
            StrictStr, Field(..., description="Object id for single object")
        ],
        pagesize: Annotated[
            Optional[conint(strict=True, le=100)],
            Field(description="pass an optional page size value"),
        ] = None,
        page: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="number of records to skip for pagination"),
        ] = None,
        sort: Annotated[
            Optional[StrictStr], Field(description="values to sort by")
        ] = None,
        direction: Annotated[
            Optional[StrictStr], Field(description="direction to sort by")
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "object_id",
            "pagesize",
            "page",
            "sort",
            "direction",
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
                    " to method get_associations_by_object" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["object_id"] is not None:
            _path_params["ObjectId"] = _params["object_id"]
        _query_params = []
        if _params.get("pagesize") is not None:
            _query_params.append(("pagesize", _params["pagesize"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        if _params.get("sort") is not None:
            _query_params.append(("sort", _params["sort"]))
        if _params.get("direction") is not None:
            _query_params.append(("direction", _params["direction"]))
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
            "200": "list[Association]",
        }
        return await self.api_client.call_api(
            "/Associations/{ObjectId}",
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

    async def get_associations_count(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        object_ids: Annotated[
            conlist(StrictStr),
            Field(..., description="A comma-separated list of object ids"),
        ],
        **kwargs,
    ) -> object:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_associations_count_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_associations_count_with_http_info(
            xero_tenant_id, object_ids, **kwargs
        )

    async def get_associations_count_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        object_ids: Annotated[
            conlist(StrictStr),
            Field(..., description="A comma-separated list of object ids"),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "object_ids"]
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
                    " to method get_associations_count" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("object_ids") is not None:
            _query_params.append(("ObjectIds", _params["object_ids"]))
            _collection_formats["ObjectIds"] = "multi"
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
            "200": "object",
        }
        return await self.api_client.call_api(
            "/Associations/Count",
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

    async def get_file(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        **kwargs,
    ) -> FileObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_file_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_file_with_http_info(xero_tenant_id, file_id, **kwargs)

    async def get_file_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "file_id"]
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
                    "Got an unexpected keyword argument '%s' to method get_file" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["file_id"] is not None:
            _path_params["FileId"] = _params["file_id"]
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
            "200": "FileObject",
        }
        return await self.api_client.call_api(
            "/Files/{FileId}",
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

    async def get_file_associations(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        **kwargs,
    ) -> list[Association]:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_file_associations_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_file_associations_with_http_info(
            xero_tenant_id, file_id, **kwargs
        )

    async def get_file_associations_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "file_id"]
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
                    " to method get_file_associations" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["file_id"] is not None:
            _path_params["FileId"] = _params["file_id"]
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
            "200": "list[Association]",
        }
        return await self.api_client.call_api(
            "/Files/{FileId}/Associations",
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

    async def get_file_content(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        **kwargs,
    ) -> bytearray:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_file_content_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_file_content_with_http_info(
            xero_tenant_id, file_id, **kwargs
        )

    async def get_file_content_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "file_id"]
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
                    " to method get_file_content" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["file_id"] is not None:
            _path_params["FileId"] = _params["file_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/octet-stream"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "bytearray",
        }
        return await self.api_client.call_api(
            "/Files/{FileId}/Content",
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

    async def get_files(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pagesize: Annotated[
            Optional[conint(strict=True, le=100)],
            Field(description="pass an optional page size value"),
        ] = None,
        page: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="number of records to skip for pagination"),
        ] = None,
        sort: Annotated[
            Optional[StrictStr], Field(description="values to sort by")
        ] = None,
        **kwargs,
    ) -> Files:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_files_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_files_with_http_info(
            xero_tenant_id, pagesize, page, sort, **kwargs
        )

    async def get_files_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pagesize: Annotated[
            Optional[conint(strict=True, le=100)],
            Field(description="pass an optional page size value"),
        ] = None,
        page: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="number of records to skip for pagination"),
        ] = None,
        sort: Annotated[
            Optional[StrictStr], Field(description="values to sort by")
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "pagesize", "page", "sort"]
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
                    "Got an unexpected keyword argument '%s' to method get_files" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("pagesize") is not None:
            _query_params.append(("pagesize", _params["pagesize"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        if _params.get("sort") is not None:
            _query_params.append(("sort", _params["sort"]))
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
            "200": "Files",
        }
        return await self.api_client.call_api(
            "/Files",
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

    async def get_folder(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        folder_id: Annotated[
            StrictStr, Field(..., description="Folder id for single object")
        ],
        **kwargs,
    ) -> Folder:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_folder_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_folder_with_http_info(xero_tenant_id, folder_id, **kwargs)

    async def get_folder_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        folder_id: Annotated[
            StrictStr, Field(..., description="Folder id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "folder_id"]
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
                    " to method get_folder" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["folder_id"] is not None:
            _path_params["FolderId"] = _params["folder_id"]
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
            "200": "Folder",
        }
        return await self.api_client.call_api(
            "/Folders/{FolderId}",
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

    async def get_folders(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        sort: Annotated[
            Optional[StrictStr], Field(description="values to sort by")
        ] = None,
        **kwargs,
    ) -> list[Folder]:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_folders_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_folders_with_http_info(xero_tenant_id, sort, **kwargs)

    async def get_folders_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        sort: Annotated[
            Optional[StrictStr], Field(description="values to sort by")
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "sort"]
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
                    " to method get_folders" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("sort") is not None:
            _query_params.append(("sort", _params["sort"]))
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
            "200": "list[Folder]",
        }
        return await self.api_client.call_api(
            "/Folders",
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

    async def get_inbox(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        **kwargs,
    ) -> Folder:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_inbox_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_inbox_with_http_info(xero_tenant_id, **kwargs)

    async def get_inbox_with_http_info(
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
                    "Got an unexpected keyword argument '%s' to method get_inbox" % _key
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
            "200": "Folder",
        }
        return await self.api_client.call_api(
            "/Inbox",
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

    async def update_file(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        file_object: FileObject,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> FileObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_file_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_file_with_http_info(
            xero_tenant_id, file_id, file_object, idempotency_key, **kwargs
        )

    async def update_file_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        file_id: Annotated[
            StrictStr, Field(..., description="File id for single object")
        ],
        file_object: FileObject,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "file_id", "file_object", "idempotency_key"]
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
                    " to method update_file" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["file_id"] is not None:
            _path_params["FileId"] = _params["file_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["file_object"] is not None:
            _body_params = _params["file_object"]
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
            "200": "FileObject",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Files/{FileId}",
            "PUT",
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

    async def update_folder(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        folder_id: Annotated[
            StrictStr, Field(..., description="Folder id for single object")
        ],
        folder: Folder,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> Folder:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_folder_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_folder_with_http_info(
            xero_tenant_id, folder_id, folder, idempotency_key, **kwargs
        )

    async def update_folder_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        folder_id: Annotated[
            StrictStr, Field(..., description="Folder id for single object")
        ],
        folder: Folder,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "folder_id", "folder", "idempotency_key"]
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
                    " to method update_folder" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["folder_id"] is not None:
            _path_params["FolderId"] = _params["folder_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["folder"] is not None:
            _body_params = _params["folder"]
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
            "200": "Folder",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Folders/{FolderId}",
            "PUT",
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

    async def upload_file(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        body: Union[StrictBytes, StrictStr],
        name: Annotated[
            StrictStr,
            Field(..., description="exact name of the file you are uploading"),
        ],
        filename: StrictStr,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        mime_type: Optional[StrictStr] = None,
        **kwargs,
    ) -> FileObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the upload_file_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.upload_file_with_http_info(
            xero_tenant_id, body, name, filename, idempotency_key, mime_type, **kwargs
        )

    async def upload_file_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        body: Union[StrictBytes, StrictStr],
        name: Annotated[
            StrictStr,
            Field(..., description="exact name of the file you are uploading"),
        ],
        filename: StrictStr,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        mime_type: Optional[StrictStr] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "body",
            "name",
            "filename",
            "idempotency_key",
            "mime_type",
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
                    " to method upload_file" % _key
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
        if _params["body"] is not None:
            _form_params.append(("body", _params["body"]))
        if _params["name"] is not None:
            _form_params.append(("name", _params["name"]))
        if _params["filename"] is not None:
            _form_params.append(("filename", _params["filename"]))
        if _params["mime_type"] is not None:
            _form_params.append(("mimeType", _params["mime_type"]))
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["multipart/form-data"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "201": "FileObject",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Files",
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

    async def upload_file_to_folder(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        folder_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="pass required folder id to save file to specific folder",
            ),
        ],
        body: Union[StrictBytes, StrictStr],
        name: Annotated[
            StrictStr,
            Field(..., description="exact name of the file you are uploading"),
        ],
        filename: StrictStr,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        mime_type: Optional[StrictStr] = None,
        **kwargs,
    ) -> FileObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the upload_file_to_folder_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.upload_file_to_folder_with_http_info(
            xero_tenant_id,
            folder_id,
            body,
            name,
            filename,
            idempotency_key,
            mime_type,
            **kwargs,
        )

    async def upload_file_to_folder_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        folder_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="pass required folder id to save file to specific folder",
            ),
        ],
        body: Union[StrictBytes, StrictStr],
        name: Annotated[
            StrictStr,
            Field(..., description="exact name of the file you are uploading"),
        ],
        filename: StrictStr,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        mime_type: Optional[StrictStr] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "folder_id",
            "body",
            "name",
            "filename",
            "idempotency_key",
            "mime_type",
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
                    " to method upload_file_to_folder" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["folder_id"] is not None:
            _path_params["FolderId"] = _params["folder_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["xero-tenant-id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        if _params["body"] is not None:
            _form_params.append(("body", _params["body"]))
        if _params["name"] is not None:
            _form_params.append(("name", _params["name"]))
        if _params["filename"] is not None:
            _form_params.append(("filename", _params["filename"]))
        if _params["mime_type"] is not None:
            _form_params.append(("mimeType", _params["mime_type"]))
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["multipart/form-data"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "201": "FileObject",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Files/{FolderId}",
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
