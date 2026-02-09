import importlib
from typing import Optional
from pydantic import (
    Field,
    StrictBool,
    StrictStr,
    conlist,
)
from typing_extensions import Annotated
from xero.api_client import ApiClient, ApiResponse, ModelFinder
from xero.exceptions import (
    ApiTypeError,
)
from xero.finance.models.account_usage_response import AccountUsageResponse
from xero.finance.models.balance_sheet_response import BalanceSheetResponse
from xero.finance.models.bank_statement_accounting_response import (
    BankStatementAccountingResponse,
)
from xero.finance.models.cash_validation_response import CashValidationResponse
from xero.finance.models.cashflow_response import CashflowResponse
from xero.finance.models.income_by_contact_response import (
    IncomeByContactResponse,
)
from xero.finance.models.lock_history_response import LockHistoryResponse
from xero.finance.models.profit_and_loss_response import ProfitAndLossResponse
from xero.finance.models.report_history_response import ReportHistoryResponse
from xero.finance.models.trial_balance_response import TrialBalanceResponse
from xero.finance.models.user_activities_response import UserActivitiesResponse


class FinanceApi:
    base_url = "https://api.xero.com/finance.xro/1.0"
    models_module = importlib.import_module("xero.finance.models")

    def __init__(self, api_client=None, base_url: str | None = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    async def get_accounting_activity_account_usage(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        start_month: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM                 If no parameter is provided, the month 12 months prior to the end month will be used.                Account usage for up to 12 months from this date will be returned."
            ),
        ] = None,
        end_month: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM                 If no parameter is provided, the current month will be used.                Account usage for up to 12 months prior to this date will be returned."
            ),
        ] = None,
        **kwargs,
    ) -> AccountUsageResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_accounting_activity_account_usage_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_accounting_activity_account_usage_with_http_info(
            xero_tenant_id, start_month, end_month, **kwargs
        )

    async def get_accounting_activity_account_usage_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        start_month: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM                 If no parameter is provided, the month 12 months prior to the end month will be used.                Account usage for up to 12 months from this date will be returned."
            ),
        ] = None,
        end_month: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM                 If no parameter is provided, the current month will be used.                Account usage for up to 12 months prior to this date will be returned."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "start_month", "end_month"]
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
                    " to method get_accounting_activity_account_usage" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("start_month") is not None:
            _query_params.append(("startMonth", _params["start_month"]))
        if _params.get("end_month") is not None:
            _query_params.append(("endMonth", _params["end_month"]))
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
            "200": "AccountUsageResponse",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/AccountingActivities/AccountUsage",
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

    async def get_accounting_activity_lock_history(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM-dd                 If no parameter is provided, the current date will be used.                Any changes to hard or soft lock dates that were made within the period up to 12 months before this date will be returned.                Please be aware that there may be a delay of up to 3 days before a change is visible from this API."
            ),
        ] = None,
        **kwargs,
    ) -> LockHistoryResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_accounting_activity_lock_history_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_accounting_activity_lock_history_with_http_info(
            xero_tenant_id, end_date, **kwargs
        )

    async def get_accounting_activity_lock_history_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM-dd                 If no parameter is provided, the current date will be used.                Any changes to hard or soft lock dates that were made within the period up to 12 months before this date will be returned.                Please be aware that there may be a delay of up to 3 days before a change is visible from this API."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "end_date"]
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
                    " to method get_accounting_activity_lock_history" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("end_date") is not None:
            _query_params.append(("endDate", _params["end_date"]))
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
            "200": "LockHistoryResponse",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/AccountingActivities/LockHistory",
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

    async def get_accounting_activity_report_history(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM-dd                 If no parameter is provided, the current date will be used.                Any reports that were published within the period up to 12 months before this date will be returned.                Please be aware that there may be a delay of up to 3 days before a published report is visible from this API."
            ),
        ] = None,
        **kwargs,
    ) -> ReportHistoryResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_accounting_activity_report_history_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_accounting_activity_report_history_with_http_info(
            xero_tenant_id, end_date, **kwargs
        )

    async def get_accounting_activity_report_history_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM-dd                 If no parameter is provided, the current date will be used.                Any reports that were published within the period up to 12 months before this date will be returned.                Please be aware that there may be a delay of up to 3 days before a published report is visible from this API."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "end_date"]
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
                    " to method get_accounting_activity_report_history" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("end_date") is not None:
            _query_params.append(("endDate", _params["end_date"]))
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
            "200": "ReportHistoryResponse",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/AccountingActivities/ReportHistory",
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

    async def get_accounting_activity_user_activities(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        data_month: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM                 The specified month must be complete (in the past); The current month cannot be specified since it is not complete.                If no parameter is provided, the month immediately previous to the current month will be used.                Any user activities occurring within the specified month will be returned.                Please be aware that there may be a delay of up to 3 days before a user activity is visible from this API."
            ),
        ] = None,
        **kwargs,
    ) -> UserActivitiesResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_accounting_activity_user_activities_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_accounting_activity_user_activities_with_http_info(
            xero_tenant_id, data_month, **kwargs
        )

    async def get_accounting_activity_user_activities_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        data_month: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM                 The specified month must be complete (in the past); The current month cannot be specified since it is not complete.                If no parameter is provided, the month immediately previous to the current month will be used.                Any user activities occurring within the specified month will be returned.                Please be aware that there may be a delay of up to 3 days before a user activity is visible from this API."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "data_month"]
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
                    " to method get_accounting_activity_user_activities" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("data_month") is not None:
            _query_params.append(("dataMonth", _params["data_month"]))
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
            "200": "UserActivitiesResponse",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/AccountingActivities/UserActivities",
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

    async def get_bank_statement_accounting(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        bank_account_id: Annotated[
            StrictStr, Field(..., description="string, GUID    Bank account Id")
        ],
        from_date: Annotated[
            StrictStr,
            Field(
                ...,
                description="date, yyyy-MM-dd     Specifies the start date of the query period.   The maximum range of the query period is 12 months. If the specified query period is more than 12 months the request will be rejected.",
            ),
        ],
        to_date: Annotated[
            StrictStr,
            Field(
                ...,
                description="date, yyyy-MM-dd     Specifies the end date of the query period.   If the end date is a future date, the request will be rejected.",
            ),
        ],
        summary_only: Annotated[
            Optional[StrictBool],
            Field(
                description="boolean, true/false    The default value is true if no parameter is provided.    In summary mode, the response will exclude the computation-heavy LineItems fields from bank transaction, invoice, credit note, prepayment and overpayment data, making the API calls quicker and more efficient."
            ),
        ] = None,
        **kwargs,
    ) -> BankStatementAccountingResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_bank_statement_accounting_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_bank_statement_accounting_with_http_info(
            xero_tenant_id, bank_account_id, from_date, to_date, summary_only, **kwargs
        )

    async def get_bank_statement_accounting_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        bank_account_id: Annotated[
            StrictStr, Field(..., description="string, GUID    Bank account Id")
        ],
        from_date: Annotated[
            StrictStr,
            Field(
                ...,
                description="date, yyyy-MM-dd     Specifies the start date of the query period.   The maximum range of the query period is 12 months. If the specified query period is more than 12 months the request will be rejected.",
            ),
        ],
        to_date: Annotated[
            StrictStr,
            Field(
                ...,
                description="date, yyyy-MM-dd     Specifies the end date of the query period.   If the end date is a future date, the request will be rejected.",
            ),
        ],
        summary_only: Annotated[
            Optional[StrictBool],
            Field(
                description="boolean, true/false    The default value is true if no parameter is provided.    In summary mode, the response will exclude the computation-heavy LineItems fields from bank transaction, invoice, credit note, prepayment and overpayment data, making the API calls quicker and more efficient."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "bank_account_id",
            "from_date",
            "to_date",
            "summary_only",
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
                    " to method get_bank_statement_accounting" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("bank_account_id") is not None:
            _query_params.append(("BankAccountID", _params["bank_account_id"]))
        if _params.get("from_date") is not None:
            _query_params.append(("FromDate", _params["from_date"]))
        if _params.get("to_date") is not None:
            _query_params.append(("ToDate", _params["to_date"]))
        if _params.get("summary_only") is not None:
            _query_params.append(("SummaryOnly", _params["summary_only"]))
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
            "200": "BankStatementAccountingResponse",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/BankStatementsPlus/statements",
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

    async def get_cash_validation(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        balance_date: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM-dd     If no parameter is provided, the current date will be used.    The ‘balance date’ will return transactions based on the accounting date entered by the user.  Transactions before the balanceDate will be included.  The user has discretion as to which accounting period the transaction relates to.    The ‘balance date’  will control the latest maximum date of transactions included in the aggregate numbers.  Balance date does not affect the CurrentStatement object, as this will always return the most recent statement before asAtSystemDate (if specified)"
            ),
        ] = None,
        as_at_system_date: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM-dd     If no parameter is provided, the current date will be used.    The ‘as at’ date will return transactions based on the  creation date.  It reflects the date the transactions were entered into Xero, not the accounting date.  The ‘as at’ date can not be overridden by the user.  This can be used to estimate a ‘historical frequency of reconciliation’.    The ‘as at’ date will affect the current statement in the response, as any candidate statements created after this date will be filtered out.  Thus the current statement returned will be the most recent statement prior to the specified ‘as at’ date.  Be aware that neither the begin date, nor the balance date, will affect the current statement.    Note;  information is only presented when system architecture allows, meaning historical cash validation information will be an estimate. In addition, delete events are not aware of the ‘as at’ functionality in this endpoint, meaning that transactions deleted at the time the API is accessed will be considered to always have been deleted."
            ),
        ] = None,
        begin_date: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM-dd     If no parameter is provided, the aggregate results will be drawn from the user’s total history.    The ‘begin date’ will return transactions based on the accounting date entered by the user. Transactions after the beginDate will be included.  The user has discretion as to which accounting period the transaction relates to."
            ),
        ] = None,
        **kwargs,
    ) -> list[CashValidationResponse]:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_cash_validation_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_cash_validation_with_http_info(
            xero_tenant_id, balance_date, as_at_system_date, begin_date, **kwargs
        )

    async def get_cash_validation_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        balance_date: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM-dd     If no parameter is provided, the current date will be used.    The ‘balance date’ will return transactions based on the accounting date entered by the user.  Transactions before the balanceDate will be included.  The user has discretion as to which accounting period the transaction relates to.    The ‘balance date’  will control the latest maximum date of transactions included in the aggregate numbers.  Balance date does not affect the CurrentStatement object, as this will always return the most recent statement before asAtSystemDate (if specified)"
            ),
        ] = None,
        as_at_system_date: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM-dd     If no parameter is provided, the current date will be used.    The ‘as at’ date will return transactions based on the  creation date.  It reflects the date the transactions were entered into Xero, not the accounting date.  The ‘as at’ date can not be overridden by the user.  This can be used to estimate a ‘historical frequency of reconciliation’.    The ‘as at’ date will affect the current statement in the response, as any candidate statements created after this date will be filtered out.  Thus the current statement returned will be the most recent statement prior to the specified ‘as at’ date.  Be aware that neither the begin date, nor the balance date, will affect the current statement.    Note;  information is only presented when system architecture allows, meaning historical cash validation information will be an estimate. In addition, delete events are not aware of the ‘as at’ functionality in this endpoint, meaning that transactions deleted at the time the API is accessed will be considered to always have been deleted."
            ),
        ] = None,
        begin_date: Annotated[
            Optional[StrictStr],
            Field(
                description="date, yyyy-MM-dd     If no parameter is provided, the aggregate results will be drawn from the user’s total history.    The ‘begin date’ will return transactions based on the accounting date entered by the user. Transactions after the beginDate will be included.  The user has discretion as to which accounting period the transaction relates to."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "balance_date",
            "as_at_system_date",
            "begin_date",
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
                    " to method get_cash_validation" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("balance_date") is not None:
            _query_params.append(("balanceDate", _params["balance_date"]))
        if _params.get("as_at_system_date") is not None:
            _query_params.append(("asAtSystemDate", _params["as_at_system_date"]))
        if _params.get("begin_date") is not None:
            _query_params.append(("beginDate", _params["begin_date"]))
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
            "200": "list[CashValidationResponse]",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/CashValidation",
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

    async def get_financial_statement_balance_sheet(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        balance_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Specifies the date for balance sheet report.    Format yyyy-MM-dd. If no parameter is provided, the current date will be used."
            ),
        ] = None,
        **kwargs,
    ) -> BalanceSheetResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_financial_statement_balance_sheet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_financial_statement_balance_sheet_with_http_info(
            xero_tenant_id, balance_date, **kwargs
        )

    async def get_financial_statement_balance_sheet_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        balance_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Specifies the date for balance sheet report.    Format yyyy-MM-dd. If no parameter is provided, the current date will be used."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "balance_date"]
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
                    " to method get_financial_statement_balance_sheet" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("balance_date") is not None:
            _query_params.append(("balanceDate", _params["balance_date"]))
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
            "200": "BalanceSheetResponse",
            "400": "Problem",
            "503": "Problem",
        }
        return await self.api_client.call_api(
            "/FinancialStatements/BalanceSheet",
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

    async def get_financial_statement_cashflow(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        start_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date e.g. yyyy-MM-dd    Specifies the start date for cash flow report.    If no parameter is provided, the date of 12 months before the end date will be used."
            ),
        ] = None,
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date e.g. yyyy-MM-dd    Specifies the end date for cash flow report.    If no parameter is provided, the current date will be used."
            ),
        ] = None,
        **kwargs,
    ) -> CashflowResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_financial_statement_cashflow_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_financial_statement_cashflow_with_http_info(
            xero_tenant_id, start_date, end_date, **kwargs
        )

    async def get_financial_statement_cashflow_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        start_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date e.g. yyyy-MM-dd    Specifies the start date for cash flow report.    If no parameter is provided, the date of 12 months before the end date will be used."
            ),
        ] = None,
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date e.g. yyyy-MM-dd    Specifies the end date for cash flow report.    If no parameter is provided, the current date will be used."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "start_date", "end_date"]
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
                    " to method get_financial_statement_cashflow" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("start_date") is not None:
            _query_params.append(("startDate", _params["start_date"]))
        if _params.get("end_date") is not None:
            _query_params.append(("endDate", _params["end_date"]))
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
            "200": "CashflowResponse",
            "400": "Problem",
            "503": "Problem",
        }
        return await self.api_client.call_api(
            "/FinancialStatements/Cashflow",
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

    async def get_financial_statement_contacts_expense(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        contact_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="Specifies the customer contacts to be included in the report.    If no parameter is provided, all customer contacts will be included"
            ),
        ] = None,
        include_manual_journals: Annotated[
            Optional[StrictBool],
            Field(
                description="Specifies whether to include the manual journals in the report.                If no parameter is provided, manual journals will not be included."
            ),
        ] = None,
        start_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date yyyy-MM-dd    Specifies the start date for the report.                If no parameter is provided, the date of 12 months before the end date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency."
            ),
        ] = None,
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date yyyy-MM-dd    Specifies the end date for the report.    If no parameter is provided, the current date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency."
            ),
        ] = None,
        **kwargs,
    ) -> IncomeByContactResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_financial_statement_contacts_expense_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_financial_statement_contacts_expense_with_http_info(
            xero_tenant_id,
            contact_ids,
            include_manual_journals,
            start_date,
            end_date,
            **kwargs,
        )

    async def get_financial_statement_contacts_expense_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        contact_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="Specifies the customer contacts to be included in the report.    If no parameter is provided, all customer contacts will be included"
            ),
        ] = None,
        include_manual_journals: Annotated[
            Optional[StrictBool],
            Field(
                description="Specifies whether to include the manual journals in the report.                If no parameter is provided, manual journals will not be included."
            ),
        ] = None,
        start_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date yyyy-MM-dd    Specifies the start date for the report.                If no parameter is provided, the date of 12 months before the end date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency."
            ),
        ] = None,
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date yyyy-MM-dd    Specifies the end date for the report.    If no parameter is provided, the current date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "contact_ids",
            "include_manual_journals",
            "start_date",
            "end_date",
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
                    " to method get_financial_statement_contacts_expense" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("contact_ids") is not None:
            _query_params.append(("contactIds", _params["contact_ids"]))
            _collection_formats["contactIds"] = "multi"
        if _params.get("include_manual_journals") is not None:
            _query_params.append(
                ("includeManualJournals", _params["include_manual_journals"])
            )
        if _params.get("start_date") is not None:
            _query_params.append(("startDate", _params["start_date"]))
        if _params.get("end_date") is not None:
            _query_params.append(("endDate", _params["end_date"]))
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
            "200": "IncomeByContactResponse",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/FinancialStatements/contacts/expense",
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

    async def get_financial_statement_contacts_revenue(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        contact_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="Specifies the customer contacts to be included in the report.    If no parameter is provided, all customer contacts will be included"
            ),
        ] = None,
        include_manual_journals: Annotated[
            Optional[StrictBool],
            Field(
                description="Specifies whether to include the manual journals in the report.                If no parameter is provided, manual journals will not be included."
            ),
        ] = None,
        start_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date yyyy-MM-dd    Specifies the start date for the report.                If no parameter is provided, the date of 12 months before the end date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency."
            ),
        ] = None,
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date yyyy-MM-dd    Specifies the end date for the report.    If no parameter is provided, the current date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency."
            ),
        ] = None,
        **kwargs,
    ) -> IncomeByContactResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_financial_statement_contacts_revenue_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_financial_statement_contacts_revenue_with_http_info(
            xero_tenant_id,
            contact_ids,
            include_manual_journals,
            start_date,
            end_date,
            **kwargs,
        )

    async def get_financial_statement_contacts_revenue_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        contact_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="Specifies the customer contacts to be included in the report.    If no parameter is provided, all customer contacts will be included"
            ),
        ] = None,
        include_manual_journals: Annotated[
            Optional[StrictBool],
            Field(
                description="Specifies whether to include the manual journals in the report.                If no parameter is provided, manual journals will not be included."
            ),
        ] = None,
        start_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date yyyy-MM-dd    Specifies the start date for the report.                If no parameter is provided, the date of 12 months before the end date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency."
            ),
        ] = None,
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date yyyy-MM-dd    Specifies the end date for the report.    If no parameter is provided, the current date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "contact_ids",
            "include_manual_journals",
            "start_date",
            "end_date",
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
                    " to method get_financial_statement_contacts_revenue" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("contact_ids") is not None:
            _query_params.append(("contactIds", _params["contact_ids"]))
            _collection_formats["contactIds"] = "multi"
        if _params.get("include_manual_journals") is not None:
            _query_params.append(
                ("includeManualJournals", _params["include_manual_journals"])
            )
        if _params.get("start_date") is not None:
            _query_params.append(("startDate", _params["start_date"]))
        if _params.get("end_date") is not None:
            _query_params.append(("endDate", _params["end_date"]))
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
            "200": "IncomeByContactResponse",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/FinancialStatements/contacts/revenue",
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

    async def get_financial_statement_profit_and_loss(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        start_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date e.g. yyyy-MM-dd    Specifies the start date for profit and loss report    If no parameter is provided, the date of 12 months before the end date will be used."
            ),
        ] = None,
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date e.g. yyyy-MM-dd    Specifies the end date for profit and loss report     If no parameter is provided, the current date will be used."
            ),
        ] = None,
        **kwargs,
    ) -> ProfitAndLossResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_financial_statement_profit_and_loss_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_financial_statement_profit_and_loss_with_http_info(
            xero_tenant_id, start_date, end_date, **kwargs
        )

    async def get_financial_statement_profit_and_loss_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        start_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date e.g. yyyy-MM-dd    Specifies the start date for profit and loss report    If no parameter is provided, the date of 12 months before the end date will be used."
            ),
        ] = None,
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date e.g. yyyy-MM-dd    Specifies the end date for profit and loss report     If no parameter is provided, the current date will be used."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "start_date", "end_date"]
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
                    " to method get_financial_statement_profit_and_loss" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("start_date") is not None:
            _query_params.append(("startDate", _params["start_date"]))
        if _params.get("end_date") is not None:
            _query_params.append(("endDate", _params["end_date"]))
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
            "200": "ProfitAndLossResponse",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/FinancialStatements/ProfitAndLoss",
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

    async def get_financial_statement_trial_balance(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date e.g. yyyy-MM-dd     Specifies the end date for trial balance report     If no parameter is provided, the current date will be used."
            ),
        ] = None,
        **kwargs,
    ) -> TrialBalanceResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_financial_statement_trial_balance_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_financial_statement_trial_balance_with_http_info(
            xero_tenant_id, end_date, **kwargs
        )

    async def get_financial_statement_trial_balance_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="Date e.g. yyyy-MM-dd     Specifies the end date for trial balance report     If no parameter is provided, the current date will be used."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "end_date"]
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
                    " to method get_financial_statement_trial_balance" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("end_date") is not None:
            _query_params.append(("endDate", _params["end_date"]))
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
            "200": "TrialBalanceResponse",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/FinancialStatements/TrialBalance",
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
