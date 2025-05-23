"""
    Xero AppStore API

    These endpoints are for Xero Partners to interact with the App Store Billing platform

    The version of the OpenAPI document: 6.3.0
    Contact: api@xero.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import importlib
import re  # noqa: F401
from typing import Optional

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from xero.api_client import ApiClient, ApiResponse, ModelFinder
from xero.appstore.models.create_usage_record import CreateUsageRecord
from xero.appstore.models.subscription import Subscription
from xero.appstore.models.update_usage_record import UpdateUsageRecord
from xero.appstore.models.usage_record import UsageRecord
from xero.appstore.models.usage_records_list import UsageRecordsList
from xero.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError,
)


class AppStoreApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

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
    ) -> Subscription:  # noqa: E501
        """Retrieves a subscription for a given subscriptionId  # noqa: E501


        :param subscription_id: Unique identifier for Subscription object (required)
        :type subscription_id: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Subscription
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_subscription_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.get_subscription_with_http_info(subscription_id, **kwargs)  # noqa: E501

    async def get_subscription_with_http_info(
        self,
        subscription_id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for Subscription object"),
        ],
        **kwargs,
    ) -> ApiResponse:  # noqa: E501
        """Retrieves a subscription for a given subscriptionId  # noqa: E501


        :param subscription_id: Unique identifier for Subscription object (required)
        :type subscription_id: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Subscription, status_code(int), headers(HTTPHeaderDict))
        """

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

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscription" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["subscription_id"] is not None:
            _path_params["subscriptionId"] = _params["subscription_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["OAuth2"]  # noqa: E501

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
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
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
    ) -> UsageRecordsList:  # noqa: E501
        """Gets all usage records related to the subscription  # noqa: E501


        :param subscription_id: Unique identifier for Subscription object (required)
        :type subscription_id: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UsageRecordsList
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_usage_records_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.get_usage_records_with_http_info(subscription_id, **kwargs)  # noqa: E501

    async def get_usage_records_with_http_info(
        self,
        subscription_id: Annotated[
            StrictStr,
            Field(..., description="Unique identifier for Subscription object"),
        ],
        **kwargs,
    ) -> ApiResponse:  # noqa: E501
        """Gets all usage records related to the subscription  # noqa: E501


        :param subscription_id: Unique identifier for Subscription object (required)
        :type subscription_id: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(UsageRecordsList, status_code(int), headers(HTTPHeaderDict))
        """

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

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_usage_records" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["subscription_id"] is not None:
            _path_params["subscriptionId"] = _params["subscription_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["OAuth2"]  # noqa: E501

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
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
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
    ) -> UsageRecord:  # noqa: E501
        """Send metered usage belonging to this subscription and subscription item  # noqa: E501


        :param subscription_id: Unique identifier for Subscription object (required)
        :type subscription_id: str
        :param subscription_item_id: The unique identifier of the subscriptionItem (required)
        :type subscription_item_id: str
        :param create_usage_record: Contains the quantity for the usage record to create (required)
        :type create_usage_record: CreateUsageRecord
        :param idempotency_key: This allows you to safely retry requests without the risk of duplicate processing. 128 character max.
        :type idempotency_key: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UsageRecord
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the post_usage_records_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.post_usage_records_with_http_info(
            subscription_id,
            subscription_item_id,
            create_usage_record,
            idempotency_key,
            **kwargs,
        )  # noqa: E501

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
    ) -> ApiResponse:  # noqa: E501
        """Send metered usage belonging to this subscription and subscription item  # noqa: E501


        :param subscription_id: Unique identifier for Subscription object (required)
        :type subscription_id: str
        :param subscription_item_id: The unique identifier of the subscriptionItem (required)
        :type subscription_item_id: str
        :param create_usage_record: Contains the quantity for the usage record to create (required)
        :type create_usage_record: CreateUsageRecord
        :param idempotency_key: This allows you to safely retry requests without the risk of duplicate processing. 128 character max.
        :type idempotency_key: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(UsageRecord, status_code(int), headers(HTTPHeaderDict))
        """

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

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_usage_records" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["subscription_id"] is not None:
            _path_params["subscriptionId"] = _params["subscription_id"]

        if _params["subscription_item_id"] is not None:
            _path_params["subscriptionItemId"] = _params["subscription_item_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params["create_usage_record"] is not None:
            _body_params = _params["create_usage_record"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = ["OAuth2"]  # noqa: E501

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
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
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
    ) -> UsageRecord:  # noqa: E501
        """Update and existing metered usage belonging to this subscription and subscription item  # noqa: E501


        :param subscription_id: Unique identifier for Subscription object (required)
        :type subscription_id: str
        :param subscription_item_id: The unique identifier of the subscriptionItem (required)
        :type subscription_item_id: str
        :param usage_record_id: The unique identifier of the usage record (required)
        :type usage_record_id: str
        :param update_usage_record: Contains the quantity for the usage record to update (required)
        :type update_usage_record: UpdateUsageRecord
        :param idempotency_key: This allows you to safely retry requests without the risk of duplicate processing. 128 character max.
        :type idempotency_key: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UsageRecord
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the put_usage_records_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.put_usage_records_with_http_info(
            subscription_id,
            subscription_item_id,
            usage_record_id,
            update_usage_record,
            idempotency_key,
            **kwargs,
        )  # noqa: E501

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
    ) -> ApiResponse:  # noqa: E501
        """Update and existing metered usage belonging to this subscription and subscription item  # noqa: E501


        :param subscription_id: Unique identifier for Subscription object (required)
        :type subscription_id: str
        :param subscription_item_id: The unique identifier of the subscriptionItem (required)
        :type subscription_item_id: str
        :param usage_record_id: The unique identifier of the usage record (required)
        :type usage_record_id: str
        :param update_usage_record: Contains the quantity for the usage record to update (required)
        :type update_usage_record: UpdateUsageRecord
        :param idempotency_key: This allows you to safely retry requests without the risk of duplicate processing. 128 character max.
        :type idempotency_key: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(UsageRecord, status_code(int), headers(HTTPHeaderDict))
        """

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

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_usage_records" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["subscription_id"] is not None:
            _path_params["subscriptionId"] = _params["subscription_id"]

        if _params["subscription_item_id"] is not None:
            _path_params["subscriptionItemId"] = _params["subscription_item_id"]

        if _params["usage_record_id"] is not None:
            _path_params["usageRecordId"] = _params["usage_record_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params["update_usage_record"] is not None:
            _body_params = _params["update_usage_record"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = ["OAuth2"]  # noqa: E501

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
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            _host=self.base_url,
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
