import importlib
from typing import Optional
from pydantic import Field, StrictStr
from typing_extensions import Annotated
from xero.api_client import ApiClient, ApiResponse, ModelFinder
from xero.appstore.models.create_usage_record import CreateUsageRecord
from xero.appstore.models.subscription import Subscription
from xero.appstore.models.update_usage_record import UpdateUsageRecord
from xero.appstore.models.usage_record import UsageRecord
from xero.appstore.models.usage_records_list import UsageRecordsList
from xero.exceptions import (
    ApiTypeError,
)


class AppStoreApi:
    base_url = "https://api.xero.com/appstore/2.0"
    models_module = importlib.import_module("xero.appstore.models")

    def __init__(self, api_client=None, base_url: str | None = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    async def get_subscription(
        self,
        subscription_id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for Subscription object"),
        ],
        **kwargs,
    ) -> Subscription:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_subscription_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_subscription_with_http_info(subscription_id, **kwargs)

    async def get_subscription_with_http_info(
        self,
        subscription_id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for Subscription object"),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["subscription_id"]
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
                    " to method get_subscription" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["subscription_id"] is not None:
            _path_params["subscriptionId"] = _params["subscription_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "Subscription",
            "404": "ProblemDetails",
        }
        return await self.api_client.call_api(
            "/subscriptions/{subscriptionId}",
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

    async def get_usage_records(
        self,
        subscription_id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for Subscription object"),
        ],
        **kwargs,
    ) -> UsageRecordsList:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_usage_records_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_usage_records_with_http_info(subscription_id, **kwargs)

    async def get_usage_records_with_http_info(
        self,
        subscription_id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for Subscription object"),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["subscription_id"]
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
                    " to method get_usage_records" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["subscription_id"] is not None:
            _path_params["subscriptionId"] = _params["subscription_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "UsageRecordsList",
            "404": "ProblemDetails",
        }
        return await self.api_client.call_api(
            "/subscriptions/{subscriptionId}/usage-records",
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

    async def post_usage_records(
        self,
        subscription_id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for Subscription object"),
        ],
        subscription_item_id: Annotated[
            StrictStr,
            Field(..., description="The unique identifier of the subscriptionItem"),
        ],
        create_usage_record: Annotated[
            CreateUsageRecord,
            Field(
                ..., description="Contains the quantity for the usage record to create"
            ),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> UsageRecord:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the post_usage_records_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.post_usage_records_with_http_info(
            subscription_id,
            subscription_item_id,
            create_usage_record,
            idempotency_key,
            **kwargs,
        )

    async def post_usage_records_with_http_info(
        self,
        subscription_id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for Subscription object"),
        ],
        subscription_item_id: Annotated[
            StrictStr,
            Field(..., description="The unique identifier of the subscriptionItem"),
        ],
        create_usage_record: Annotated[
            CreateUsageRecord,
            Field(
                ..., description="Contains the quantity for the usage record to create"
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
        _all_params = [
            "subscription_id",
            "subscription_item_id",
            "create_usage_record",
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
                    " to method post_usage_records" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["subscription_id"] is not None:
            _path_params["subscriptionId"] = _params["subscription_id"]
        if _params["subscription_item_id"] is not None:
            _path_params["subscriptionItemId"] = _params["subscription_item_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["create_usage_record"] is not None:
            _body_params = _params["create_usage_record"]
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
            "200": "UsageRecord",
            "404": "ProblemDetails",
        }
        return await self.api_client.call_api(
            "/subscriptions/{subscriptionId}/items/{subscriptionItemId}/usage-records",
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

    async def put_usage_records(
        self,
        subscription_id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for Subscription object"),
        ],
        subscription_item_id: Annotated[
            StrictStr,
            Field(..., description="The unique identifier of the subscriptionItem"),
        ],
        usage_record_id: Annotated[
            StrictStr,
            Field(..., description="The unique identifier of the usage record"),
        ],
        update_usage_record: Annotated[
            UpdateUsageRecord,
            Field(
                ..., description="Contains the quantity for the usage record to update"
            ),
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> UsageRecord:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the put_usage_records_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.put_usage_records_with_http_info(
            subscription_id,
            subscription_item_id,
            usage_record_id,
            update_usage_record,
            idempotency_key,
            **kwargs,
        )

    async def put_usage_records_with_http_info(
        self,
        subscription_id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for Subscription object"),
        ],
        subscription_item_id: Annotated[
            StrictStr,
            Field(..., description="The unique identifier of the subscriptionItem"),
        ],
        usage_record_id: Annotated[
            StrictStr,
            Field(..., description="The unique identifier of the usage record"),
        ],
        update_usage_record: Annotated[
            UpdateUsageRecord,
            Field(
                ..., description="Contains the quantity for the usage record to update"
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
        _all_params = [
            "subscription_id",
            "subscription_item_id",
            "usage_record_id",
            "update_usage_record",
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
                    " to method put_usage_records" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["subscription_id"] is not None:
            _path_params["subscriptionId"] = _params["subscription_id"]
        if _params["subscription_item_id"] is not None:
            _path_params["subscriptionItemId"] = _params["subscription_item_id"]
        if _params["usage_record_id"] is not None:
            _path_params["usageRecordId"] = _params["usage_record_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["update_usage_record"] is not None:
            _body_params = _params["update_usage_record"]
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
            "200": "UsageRecord",
            "404": "ProblemDetails",
        }
        return await self.api_client.call_api(
            "/subscriptions/{subscriptionId}/items/{subscriptionItemId}/usage-records/{usageRecordId}",
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
