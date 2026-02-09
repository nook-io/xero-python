import importlib
from datetime import datetime
from typing import Optional
from pydantic import (
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    conint,
    conlist,
)
from typing_extensions import Annotated
from xero.api_client import ApiClient, ApiResponse, ModelFinder
from xero.exceptions import (
    ApiTypeError,
)
from xero.project.models.charge_type import ChargeType
from xero.project.models.project import Project
from xero.project.models.project_create_or_update import ProjectCreateOrUpdate
from xero.project.models.project_patch import ProjectPatch
from xero.project.models.project_users import ProjectUsers
from xero.project.models.projects import Projects
from xero.project.models.task import Task
from xero.project.models.task_create_or_update import TaskCreateOrUpdate
from xero.project.models.tasks import Tasks
from xero.project.models.time_entries import TimeEntries
from xero.project.models.time_entry import TimeEntry
from xero.project.models.time_entry_create_or_update import (
    TimeEntryCreateOrUpdate,
)


class ProjectApi:
    base_url = "https://api.xero.com/projects.xro/2.0"
    models_module = importlib.import_module("xero.project.models")

    def __init__(self, api_client=None, base_url: str | None = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    async def create_project(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_create_or_update: Annotated[
            ProjectCreateOrUpdate,
            Field(
                ...,
                description="Create a new project with ProjectCreateOrUpdate object",
            ),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> Project:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_project_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_project_with_http_info(
            xero_tenant_id, project_create_or_update, idempotency_key, **kwargs
        )

    async def create_project_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_create_or_update: Annotated[
            ProjectCreateOrUpdate,
            Field(
                ...,
                description="Create a new project with ProjectCreateOrUpdate object",
            ),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "project_create_or_update", "idempotency_key"]
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
                    " to method create_project" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["project_create_or_update"] is not None:
            _body_params = _params["project_create_or_update"]
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
            "201": "Project",
            "400": "Error",
        }
        return await self.api_client.call_api(
            "/Projects",
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

    async def create_task(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(..., description="You can create a task on a specified projectId"),
        ],
        task_create_or_update: Annotated[
            TaskCreateOrUpdate,
            Field(..., description="The task object you are creating"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> Task:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_task_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_task_with_http_info(
            xero_tenant_id, project_id, task_create_or_update, idempotency_key, **kwargs
        )

    async def create_task_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(..., description="You can create a task on a specified projectId"),
        ],
        task_create_or_update: Annotated[
            TaskCreateOrUpdate,
            Field(..., description="The task object you are creating"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "project_id",
            "task_create_or_update",
            "idempotency_key",
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
                    " to method create_task" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["task_create_or_update"] is not None:
            _body_params = _params["task_create_or_update"]
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
            "201": "Task",
            "400": "Error",
        }
        return await self.api_client.call_api(
            "/Projects/{projectId}/Tasks",
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

    async def create_time_entry(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        time_entry_create_or_update: Annotated[
            TimeEntryCreateOrUpdate,
            Field(..., description="The time entry object you are creating"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> TimeEntry:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_time_entry_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_time_entry_with_http_info(
            xero_tenant_id,
            project_id,
            time_entry_create_or_update,
            idempotency_key,
            **kwargs,
        )

    async def create_time_entry_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        time_entry_create_or_update: Annotated[
            TimeEntryCreateOrUpdate,
            Field(..., description="The time entry object you are creating"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "project_id",
            "time_entry_create_or_update",
            "idempotency_key",
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
                    " to method create_time_entry" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["time_entry_create_or_update"] is not None:
            _body_params = _params["time_entry_create_or_update"]
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
            "200": "TimeEntry",
            "400": "Error",
        }
        return await self.api_client.call_api(
            "/Projects/{projectId}/Time",
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

    async def delete_task(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        task_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual task by appending the id to the endpoint",
            ),
        ],
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_task_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.delete_task_with_http_info(
            xero_tenant_id, project_id, task_id, **kwargs
        )

    async def delete_task_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        task_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual task by appending the id to the endpoint",
            ),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "project_id", "task_id"]
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
                    " to method delete_task" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        if _params["task_id"] is not None:
            _path_params["taskId"] = _params["task_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Projects/{projectId}/Tasks/{taskId}",
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

    async def delete_time_entry(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        time_entry_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual task by appending the id to the endpoint",
            ),
        ],
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_time_entry_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.delete_time_entry_with_http_info(
            xero_tenant_id, project_id, time_entry_id, **kwargs
        )

    async def delete_time_entry_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        time_entry_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual task by appending the id to the endpoint",
            ),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "project_id", "time_entry_id"]
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
                    " to method delete_time_entry" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        if _params["time_entry_id"] is not None:
            _path_params["timeEntryId"] = _params["time_entry_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Projects/{projectId}/Time/{timeEntryId}",
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

    async def get_project(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        **kwargs,
    ) -> Project:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_project_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_project_with_http_info(
            xero_tenant_id, project_id, **kwargs
        )

    async def get_project_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "project_id"]
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
                    " to method get_project" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "Project",
            "400": "Error",
        }
        return await self.api_client.call_api(
            "/Projects/{projectId}",
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

    async def get_project_users(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0."
            ),
        ] = None,
        page_size: Annotated[
            Optional[conint(strict=True, le=500, ge=1)],
            Field(
                description="Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500."
            ),
        ] = None,
        **kwargs,
    ) -> ProjectUsers:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_project_users_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_project_users_with_http_info(
            xero_tenant_id, page, page_size, **kwargs
        )

    async def get_project_users_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0."
            ),
        ] = None,
        page_size: Annotated[
            Optional[conint(strict=True, le=500, ge=1)],
            Field(
                description="Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "page", "page_size"]
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
                    " to method get_project_users" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        if _params.get("page_size") is not None:
            _query_params.append(("pageSize", _params["page_size"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "ProjectUsers",
            "400": "Error",
        }
        return await self.api_client.call_api(
            "/ProjectsUsers",
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

    async def get_projects(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="Search for all projects that match a comma separated list of projectIds"
            ),
        ] = None,
        contact_id: Annotated[
            Optional[StrictStr],
            Field(description="Filter for projects for a specific contact"),
        ] = None,
        states: Annotated[
            Optional[StrictStr],
            Field(
                description="Filter for projects in a particular state (INPROGRESS or CLOSED)"
            ),
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0."
            ),
        ] = None,
        page_size: Annotated[
            Optional[conint(strict=True, le=500, ge=1)],
            Field(
                description="Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500."
            ),
        ] = None,
        **kwargs,
    ) -> Projects:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_projects_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_projects_with_http_info(
            xero_tenant_id, project_ids, contact_id, states, page, page_size, **kwargs
        )

    async def get_projects_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="Search for all projects that match a comma separated list of projectIds"
            ),
        ] = None,
        contact_id: Annotated[
            Optional[StrictStr],
            Field(description="Filter for projects for a specific contact"),
        ] = None,
        states: Annotated[
            Optional[StrictStr],
            Field(
                description="Filter for projects in a particular state (INPROGRESS or CLOSED)"
            ),
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0."
            ),
        ] = None,
        page_size: Annotated[
            Optional[conint(strict=True, le=500, ge=1)],
            Field(
                description="Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "project_ids",
            "contact_id",
            "states",
            "page",
            "page_size",
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
                    " to method get_projects" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("project_ids") is not None:
            _query_params.append(("projectIds", _params["project_ids"]))
            _collection_formats["projectIds"] = "multi"
        if _params.get("contact_id") is not None:
            _query_params.append(("contactID", _params["contact_id"]))
        if _params.get("states") is not None:
            _query_params.append(("states", _params["states"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        if _params.get("page_size") is not None:
            _query_params.append(("pageSize", _params["page_size"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "Projects",
            "400": "Error",
        }
        return await self.api_client.call_api(
            "/Projects",
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

    async def get_task(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        task_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual task by appending the taskId to the endpoint, i.e. GET https://.../tasks/{taskID}",
            ),
        ],
        **kwargs,
    ) -> Task:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_task_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_task_with_http_info(
            xero_tenant_id, project_id, task_id, **kwargs
        )

    async def get_task_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        task_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual task by appending the taskId to the endpoint, i.e. GET https://.../tasks/{taskID}",
            ),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "project_id", "task_id"]
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
                    "Got an unexpected keyword argument '%s' to method get_task" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        if _params["task_id"] is not None:
            _path_params["taskId"] = _params["task_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "Task",
            "400": "Error",
        }
        return await self.api_client.call_api(
            "/Projects/{projectId}/Tasks/{taskId}",
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

    async def get_tasks(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0."
            ),
        ] = None,
        page_size: Annotated[
            Optional[StrictInt],
            Field(
                description="Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500."
            ),
        ] = None,
        task_ids: Annotated[
            Optional[StrictStr],
            Field(
                description="Search for all tasks that match a comma separated list of taskIds, i.e. GET https://.../tasks?taskIds={taskID},{taskID}"
            ),
        ] = None,
        charge_type: Optional[ChargeType] = None,
        **kwargs,
    ) -> Tasks:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_tasks_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_tasks_with_http_info(
            xero_tenant_id, project_id, page, page_size, task_ids, charge_type, **kwargs
        )

    async def get_tasks_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0."
            ),
        ] = None,
        page_size: Annotated[
            Optional[StrictInt],
            Field(
                description="Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500."
            ),
        ] = None,
        task_ids: Annotated[
            Optional[StrictStr],
            Field(
                description="Search for all tasks that match a comma separated list of taskIds, i.e. GET https://.../tasks?taskIds={taskID},{taskID}"
            ),
        ] = None,
        charge_type: Optional[ChargeType] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "project_id",
            "page",
            "page_size",
            "task_ids",
            "charge_type",
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
                    "Got an unexpected keyword argument '%s' to method get_tasks" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        if _params.get("page_size") is not None:
            _query_params.append(("pageSize", _params["page_size"]))
        if _params.get("task_ids") is not None:
            _query_params.append(("taskIds", _params["task_ids"]))
        if _params.get("charge_type") is not None:
            _query_params.append(("chargeType", _params["charge_type"].value))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "Tasks",
            "400": "Error",
        }
        return await self.api_client.call_api(
            "/Projects/{projectId}/Tasks",
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

    async def get_time_entries(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="Identifier of the project, that the task (which the time entry is logged against) belongs to.",
            ),
        ],
        user_id: Annotated[
            Optional[StrictStr],
            Field(
                description="The xero user identifier of the person who logged time."
            ),
        ] = None,
        task_id: Annotated[
            Optional[StrictStr],
            Field(
                description="Identifier of the task that time entry is logged against."
            ),
        ] = None,
        invoice_id: Annotated[
            Optional[StrictStr],
            Field(description="Finds all time entries for this invoice."),
        ] = None,
        contact_id: Annotated[
            Optional[StrictStr],
            Field(description="Finds all time entries for this contact identifier."),
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0."
            ),
        ] = None,
        page_size: Annotated[
            Optional[StrictInt],
            Field(
                description="Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500."
            ),
        ] = None,
        states: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="Comma-separated list of states to find. Will find all time entries that are in the status of whatever is specified."
            ),
        ] = None,
        is_chargeable: Annotated[
            Optional[StrictBool],
            Field(
                description="Finds all time entries which relate to tasks with the charge type `TIME` or `FIXED`."
            ),
        ] = None,
        date_after_utc: Annotated[
            Optional[datetime],
            Field(
                description="ISO 8601 UTC date. Finds all time entries on or after this date filtered on the `dateUtc` field."
            ),
        ] = None,
        date_before_utc: Annotated[
            Optional[datetime],
            Field(
                description="ISO 8601 UTC date. Finds all time entries on or before this date filtered on the `dateUtc` field."
            ),
        ] = None,
        **kwargs,
    ) -> TimeEntries:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_time_entries_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_time_entries_with_http_info(
            xero_tenant_id,
            project_id,
            user_id,
            task_id,
            invoice_id,
            contact_id,
            page,
            page_size,
            states,
            is_chargeable,
            date_after_utc,
            date_before_utc,
            **kwargs,
        )

    async def get_time_entries_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="Identifier of the project, that the task (which the time entry is logged against) belongs to.",
            ),
        ],
        user_id: Annotated[
            Optional[StrictStr],
            Field(
                description="The xero user identifier of the person who logged time."
            ),
        ] = None,
        task_id: Annotated[
            Optional[StrictStr],
            Field(
                description="Identifier of the task that time entry is logged against."
            ),
        ] = None,
        invoice_id: Annotated[
            Optional[StrictStr],
            Field(description="Finds all time entries for this invoice."),
        ] = None,
        contact_id: Annotated[
            Optional[StrictStr],
            Field(description="Finds all time entries for this contact identifier."),
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0."
            ),
        ] = None,
        page_size: Annotated[
            Optional[StrictInt],
            Field(
                description="Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500."
            ),
        ] = None,
        states: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="Comma-separated list of states to find. Will find all time entries that are in the status of whatever is specified."
            ),
        ] = None,
        is_chargeable: Annotated[
            Optional[StrictBool],
            Field(
                description="Finds all time entries which relate to tasks with the charge type `TIME` or `FIXED`."
            ),
        ] = None,
        date_after_utc: Annotated[
            Optional[datetime],
            Field(
                description="ISO 8601 UTC date. Finds all time entries on or after this date filtered on the `dateUtc` field."
            ),
        ] = None,
        date_before_utc: Annotated[
            Optional[datetime],
            Field(
                description="ISO 8601 UTC date. Finds all time entries on or before this date filtered on the `dateUtc` field."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "project_id",
            "user_id",
            "task_id",
            "invoice_id",
            "contact_id",
            "page",
            "page_size",
            "states",
            "is_chargeable",
            "date_after_utc",
            "date_before_utc",
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
                    " to method get_time_entries" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        _query_params = []
        if _params.get("user_id") is not None:
            _query_params.append(("userId", _params["user_id"]))
        if _params.get("task_id") is not None:
            _query_params.append(("taskId", _params["task_id"]))
        if _params.get("invoice_id") is not None:
            _query_params.append(("invoiceId", _params["invoice_id"]))
        if _params.get("contact_id") is not None:
            _query_params.append(("contactId", _params["contact_id"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        if _params.get("page_size") is not None:
            _query_params.append(("pageSize", _params["page_size"]))
        if _params.get("states") is not None:
            _query_params.append(("states", _params["states"]))
            _collection_formats["states"] = "multi"
        if _params.get("is_chargeable") is not None:
            _query_params.append(("isChargeable", _params["is_chargeable"]))
        if _params.get("date_after_utc") is not None:
            if isinstance(_params["date_after_utc"], datetime):
                _query_params.append(
                    (
                        "dateAfterUtc",
                        _params["date_after_utc"].strftime(
                            self.api_client.configuration.datetime_format
                        ),
                    )
                )
            else:
                _query_params.append(("dateAfterUtc", _params["date_after_utc"]))
        if _params.get("date_before_utc") is not None:
            if isinstance(_params["date_before_utc"], datetime):
                _query_params.append(
                    (
                        "dateBeforeUtc",
                        _params["date_before_utc"].strftime(
                            self.api_client.configuration.datetime_format
                        ),
                    )
                )
            else:
                _query_params.append(("dateBeforeUtc", _params["date_before_utc"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "TimeEntries",
            "400": "Error",
        }
        return await self.api_client.call_api(
            "/Projects/{projectId}/Time",
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

    async def get_time_entry(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        time_entry_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual time entry by appending the id to the endpoint",
            ),
        ],
        **kwargs,
    ) -> TimeEntry:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_time_entry_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_time_entry_with_http_info(
            xero_tenant_id, project_id, time_entry_id, **kwargs
        )

    async def get_time_entry_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        time_entry_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual time entry by appending the id to the endpoint",
            ),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "project_id", "time_entry_id"]
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
                    " to method get_time_entry" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        if _params["time_entry_id"] is not None:
            _path_params["timeEntryId"] = _params["time_entry_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "TimeEntry",
            "400": "Error",
        }
        return await self.api_client.call_api(
            "/Projects/{projectId}/Time/{timeEntryId}",
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

    async def patch_project(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        project_patch: Annotated[
            ProjectPatch,
            Field(..., description="Update the status of an existing Project"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the patch_project_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.patch_project_with_http_info(
            xero_tenant_id, project_id, project_patch, idempotency_key, **kwargs
        )

    async def patch_project_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        project_patch: Annotated[
            ProjectPatch,
            Field(..., description="Update the status of an existing Project"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "project_id",
            "project_patch",
            "idempotency_key",
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
                    " to method patch_project" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["project_patch"] is not None:
            _body_params = _params["project_patch"]
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
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Projects/{projectId}",
            "PATCH",
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

    async def update_project(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        project_create_or_update: Annotated[
            ProjectCreateOrUpdate,
            Field(..., description="Request of type ProjectCreateOrUpdate"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_project_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_project_with_http_info(
            xero_tenant_id,
            project_id,
            project_create_or_update,
            idempotency_key,
            **kwargs,
        )

    async def update_project_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        project_create_or_update: Annotated[
            ProjectCreateOrUpdate,
            Field(..., description="Request of type ProjectCreateOrUpdate"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "project_id",
            "project_create_or_update",
            "idempotency_key",
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
                    " to method update_project" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["project_create_or_update"] is not None:
            _body_params = _params["project_create_or_update"]
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
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Projects/{projectId}",
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

    async def update_task(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        task_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual task by appending the id to the endpoint",
            ),
        ],
        task_create_or_update: Annotated[
            TaskCreateOrUpdate,
            Field(..., description="The task object you are updating"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_task_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_task_with_http_info(
            xero_tenant_id,
            project_id,
            task_id,
            task_create_or_update,
            idempotency_key,
            **kwargs,
        )

    async def update_task_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        task_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual task by appending the id to the endpoint",
            ),
        ],
        task_create_or_update: Annotated[
            TaskCreateOrUpdate,
            Field(..., description="The task object you are updating"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "project_id",
            "task_id",
            "task_create_or_update",
            "idempotency_key",
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
                    " to method update_task" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        if _params["task_id"] is not None:
            _path_params["taskId"] = _params["task_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["task_create_or_update"] is not None:
            _body_params = _params["task_create_or_update"]
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
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Projects/{projectId}/Tasks/{taskId}",
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

    async def update_time_entry(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        time_entry_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual time entry by appending the id to the endpoint",
            ),
        ],
        time_entry_create_or_update: Annotated[
            TimeEntryCreateOrUpdate,
            Field(..., description="The time entry object you are updating"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_time_entry_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_time_entry_with_http_info(
            xero_tenant_id,
            project_id,
            time_entry_id,
            time_entry_create_or_update,
            idempotency_key,
            **kwargs,
        )

    async def update_time_entry_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        project_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual project by appending the projectId to the endpoint",
            ),
        ],
        time_entry_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="You can specify an individual time entry by appending the id to the endpoint",
            ),
        ],
        time_entry_create_or_update: Annotated[
            TimeEntryCreateOrUpdate,
            Field(..., description="The time entry object you are updating"),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "project_id",
            "time_entry_id",
            "time_entry_create_or_update",
            "idempotency_key",
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
                    " to method update_time_entry" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["project_id"] is not None:
            _path_params["projectId"] = _params["project_id"]
        if _params["time_entry_id"] is not None:
            _path_params["timeEntryId"] = _params["time_entry_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["time_entry_create_or_update"] is not None:
            _body_params = _params["time_entry_create_or_update"]
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
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Projects/{projectId}/Time/{timeEntryId}",
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
