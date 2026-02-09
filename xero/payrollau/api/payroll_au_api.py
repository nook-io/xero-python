import importlib
from datetime import datetime
from typing import Optional
from pydantic import (
    Field,
    StrictInt,
    StrictStr,
    conlist,
)
from typing_extensions import Annotated
from xero.api_client import ApiClient, ApiResponse, ModelFinder
from xero.exceptions import (
    ApiTypeError,
)
from xero.payrollau.models.employee import Employee
from xero.payrollau.models.employees import Employees
from xero.payrollau.models.leave_application import LeaveApplication
from xero.payrollau.models.leave_applications import LeaveApplications
from xero.payrollau.models.pay_item import PayItem
from xero.payrollau.models.pay_items import PayItems
from xero.payrollau.models.pay_run import PayRun
from xero.payrollau.models.pay_runs import PayRuns
from xero.payrollau.models.payroll_calendar import PayrollCalendar
from xero.payrollau.models.payroll_calendars import PayrollCalendars
from xero.payrollau.models.payslip_lines import PayslipLines
from xero.payrollau.models.payslip_object import PayslipObject
from xero.payrollau.models.payslips import Payslips
from xero.payrollau.models.settings_object import SettingsObject
from xero.payrollau.models.super_fund import SuperFund
from xero.payrollau.models.super_fund_products import SuperFundProducts
from xero.payrollau.models.super_funds import SuperFunds
from xero.payrollau.models.timesheet import Timesheet
from xero.payrollau.models.timesheet_object import TimesheetObject
from xero.payrollau.models.timesheets import Timesheets


class PayrollAuApi:
    base_url = "https://api.xero.com/payroll.xro/1.0"
    models_module = importlib.import_module("xero.payrollau.models")

    def __init__(self, api_client=None, base_url: str | None = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    async def approve_leave_application(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_application_id: Annotated[
            StrictStr, Field(..., description="Leave Application id for single object")
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> LeaveApplications:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the approve_leave_application_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.approve_leave_application_with_http_info(
            xero_tenant_id, leave_application_id, idempotency_key, **kwargs
        )

    async def approve_leave_application_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_application_id: Annotated[
            StrictStr, Field(..., description="Leave Application id for single object")
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
        _all_params = ["xero_tenant_id", "leave_application_id", "idempotency_key"]
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
                    " to method approve_leave_application" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["leave_application_id"] is not None:
            _path_params["LeaveApplicationID"] = _params["leave_application_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "LeaveApplications",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/LeaveApplications/{LeaveApplicationID}/approve",
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

    async def create_employee(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee: conlist(Employee),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> Employees:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_employee_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_employee_with_http_info(
            xero_tenant_id, employee, idempotency_key, **kwargs
        )

    async def create_employee_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee: conlist(Employee),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee", "idempotency_key"]
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
                    " to method create_employee" % _key
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
        if _params["employee"] is not None:
            _body_params = _params["employee"]
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
            "200": "Employees",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Employees",
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

    async def create_leave_application(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_application: conlist(LeaveApplication),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> LeaveApplications:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_leave_application_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_leave_application_with_http_info(
            xero_tenant_id, leave_application, idempotency_key, **kwargs
        )

    async def create_leave_application_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_application: conlist(LeaveApplication),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "leave_application", "idempotency_key"]
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
                    " to method create_leave_application" % _key
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
        if _params["leave_application"] is not None:
            _body_params = _params["leave_application"]
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
            "200": "LeaveApplications",
            "400": None,
        }
        return await self.api_client.call_api(
            "/LeaveApplications",
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

    async def create_pay_item(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_item: PayItem,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> PayItems:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_pay_item_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_pay_item_with_http_info(
            xero_tenant_id, pay_item, idempotency_key, **kwargs
        )

    async def create_pay_item_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_item: PayItem,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "pay_item", "idempotency_key"]
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
                    " to method create_pay_item" % _key
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
        if _params["pay_item"] is not None:
            _body_params = _params["pay_item"]
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
            "200": "PayItems",
            "400": None,
        }
        return await self.api_client.call_api(
            "/PayItems",
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

    async def create_pay_run(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run: conlist(PayRun),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> PayRuns:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_pay_run_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_pay_run_with_http_info(
            xero_tenant_id, pay_run, idempotency_key, **kwargs
        )

    async def create_pay_run_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run: conlist(PayRun),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "pay_run", "idempotency_key"]
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
                    " to method create_pay_run" % _key
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
        if _params["pay_run"] is not None:
            _body_params = _params["pay_run"]
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
            "200": "PayRuns",
            "400": None,
        }
        return await self.api_client.call_api(
            "/PayRuns",
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

    async def create_payroll_calendar(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        payroll_calendar: conlist(PayrollCalendar),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> PayrollCalendars:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_payroll_calendar_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_payroll_calendar_with_http_info(
            xero_tenant_id, payroll_calendar, idempotency_key, **kwargs
        )

    async def create_payroll_calendar_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        payroll_calendar: conlist(PayrollCalendar),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "payroll_calendar", "idempotency_key"]
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
                    " to method create_payroll_calendar" % _key
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
        if _params["payroll_calendar"] is not None:
            _body_params = _params["payroll_calendar"]
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
            "200": "PayrollCalendars",
            "400": None,
        }
        return await self.api_client.call_api(
            "/PayrollCalendars",
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

    async def create_superfund(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        super_fund: conlist(SuperFund),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> SuperFunds:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_superfund_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_superfund_with_http_info(
            xero_tenant_id, super_fund, idempotency_key, **kwargs
        )

    async def create_superfund_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        super_fund: conlist(SuperFund),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "super_fund", "idempotency_key"]
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
                    " to method create_superfund" % _key
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
        if _params["super_fund"] is not None:
            _body_params = _params["super_fund"]
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
            "200": "SuperFunds",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Superfunds",
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

    async def create_timesheet(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet: conlist(Timesheet),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> Timesheets:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_timesheet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_timesheet_with_http_info(
            xero_tenant_id, timesheet, idempotency_key, **kwargs
        )

    async def create_timesheet_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet: conlist(Timesheet),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "timesheet", "idempotency_key"]
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
                    " to method create_timesheet" % _key
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
        if _params["timesheet"] is not None:
            _body_params = _params["timesheet"]
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
            "200": "Timesheets",
            "400": None,
        }
        return await self.api_client.call_api(
            "/Timesheets",
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

    async def get_employee(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        **kwargs,
    ) -> Employees:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_with_http_info(
            xero_tenant_id, employee_id, **kwargs
        )

    async def get_employee_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id"]
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
                    " to method get_employee" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
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
            "200": "Employees",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}",
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

    async def get_employees(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 employees will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> Employees:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employees_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employees_with_http_info(
            xero_tenant_id, if_modified_since, where, order, page, **kwargs
        )

    async def get_employees_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 employees will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "if_modified_since", "where", "order", "page"]
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
                    " to method get_employees" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("where") is not None:
            _query_params.append(("where", _params["where"]))
        if _params.get("order") is not None:
            _query_params.append(("order", _params["order"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["if_modified_since"] is not None:
            _header_params["If-Modified-Since"] = _params["if_modified_since"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "Employees",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/Employees",
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

    async def get_leave_application(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_application_id: Annotated[
            StrictStr, Field(..., description="Leave Application id for single object")
        ],
        **kwargs,
    ) -> LeaveApplications:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_leave_application_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_leave_application_with_http_info(
            xero_tenant_id, leave_application_id, **kwargs
        )

    async def get_leave_application_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_application_id: Annotated[
            StrictStr, Field(..., description="Leave Application id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "leave_application_id"]
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
                    " to method get_leave_application" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["leave_application_id"] is not None:
            _path_params["LeaveApplicationID"] = _params["leave_application_id"]
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
            "200": "LeaveApplications",
        }
        return await self.api_client.call_api(
            "/LeaveApplications/{LeaveApplicationID}",
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

    async def get_leave_applications(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 objects will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> LeaveApplications:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_leave_applications_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_leave_applications_with_http_info(
            xero_tenant_id, if_modified_since, where, order, page, **kwargs
        )

    async def get_leave_applications_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 objects will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "if_modified_since", "where", "order", "page"]
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
                    " to method get_leave_applications" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("where") is not None:
            _query_params.append(("where", _params["where"]))
        if _params.get("order") is not None:
            _query_params.append(("order", _params["order"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["if_modified_since"] is not None:
            _header_params["If-Modified-Since"] = _params["if_modified_since"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "LeaveApplications",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/LeaveApplications",
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

    async def get_leave_applications_v2(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 objects will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> LeaveApplications:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_leave_applications_v2_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_leave_applications_v2_with_http_info(
            xero_tenant_id, if_modified_since, where, order, page, **kwargs
        )

    async def get_leave_applications_v2_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 objects will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "if_modified_since", "where", "order", "page"]
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
                    " to method get_leave_applications_v2" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("where") is not None:
            _query_params.append(("where", _params["where"]))
        if _params.get("order") is not None:
            _query_params.append(("order", _params["order"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["if_modified_since"] is not None:
            _header_params["If-Modified-Since"] = _params["if_modified_since"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "LeaveApplications",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/LeaveApplications/v2",
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

    async def get_pay_items(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 objects will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> PayItems:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_pay_items_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_pay_items_with_http_info(
            xero_tenant_id, if_modified_since, where, order, page, **kwargs
        )

    async def get_pay_items_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 objects will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "if_modified_since", "where", "order", "page"]
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
                    " to method get_pay_items" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("where") is not None:
            _query_params.append(("where", _params["where"]))
        if _params.get("order") is not None:
            _query_params.append(("order", _params["order"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["if_modified_since"] is not None:
            _header_params["If-Modified-Since"] = _params["if_modified_since"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "PayItems",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/PayItems",
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

    async def get_pay_run(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run_id: Annotated[
            StrictStr, Field(..., description="PayRun id for single object")
        ],
        **kwargs,
    ) -> PayRuns:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_pay_run_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_pay_run_with_http_info(
            xero_tenant_id, pay_run_id, **kwargs
        )

    async def get_pay_run_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run_id: Annotated[
            StrictStr, Field(..., description="PayRun id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "pay_run_id"]
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
                    " to method get_pay_run" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["pay_run_id"] is not None:
            _path_params["PayRunID"] = _params["pay_run_id"]
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
            "200": "PayRuns",
        }
        return await self.api_client.call_api(
            "/PayRuns/{PayRunID}",
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

    async def get_pay_runs(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 PayRuns will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> PayRuns:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_pay_runs_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_pay_runs_with_http_info(
            xero_tenant_id, if_modified_since, where, order, page, **kwargs
        )

    async def get_pay_runs_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 PayRuns will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "if_modified_since", "where", "order", "page"]
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
                    " to method get_pay_runs" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("where") is not None:
            _query_params.append(("where", _params["where"]))
        if _params.get("order") is not None:
            _query_params.append(("order", _params["order"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["if_modified_since"] is not None:
            _header_params["If-Modified-Since"] = _params["if_modified_since"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "PayRuns",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/PayRuns",
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

    async def get_payroll_calendar(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        payroll_calendar_id: Annotated[
            StrictStr, Field(..., description="Payroll Calendar id for single object")
        ],
        **kwargs,
    ) -> PayrollCalendars:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_payroll_calendar_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_payroll_calendar_with_http_info(
            xero_tenant_id, payroll_calendar_id, **kwargs
        )

    async def get_payroll_calendar_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        payroll_calendar_id: Annotated[
            StrictStr, Field(..., description="Payroll Calendar id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "payroll_calendar_id"]
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
                    " to method get_payroll_calendar" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["payroll_calendar_id"] is not None:
            _path_params["PayrollCalendarID"] = _params["payroll_calendar_id"]
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
            "200": "PayrollCalendars",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/PayrollCalendars/{PayrollCalendarID}",
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

    async def get_payroll_calendars(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 objects will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> PayrollCalendars:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_payroll_calendars_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_payroll_calendars_with_http_info(
            xero_tenant_id, if_modified_since, where, order, page, **kwargs
        )

    async def get_payroll_calendars_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 objects will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "if_modified_since", "where", "order", "page"]
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
                    " to method get_payroll_calendars" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("where") is not None:
            _query_params.append(("where", _params["where"]))
        if _params.get("order") is not None:
            _query_params.append(("order", _params["order"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["if_modified_since"] is not None:
            _header_params["If-Modified-Since"] = _params["if_modified_since"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "PayrollCalendars",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/PayrollCalendars",
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

    async def get_payslip(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        payslip_id: Annotated[
            StrictStr, Field(..., description="Payslip id for single object")
        ],
        **kwargs,
    ) -> PayslipObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_payslip_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_payslip_with_http_info(
            xero_tenant_id, payslip_id, **kwargs
        )

    async def get_payslip_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        payslip_id: Annotated[
            StrictStr, Field(..., description="Payslip id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "payslip_id"]
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
                    " to method get_payslip" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["payslip_id"] is not None:
            _path_params["PayslipID"] = _params["payslip_id"]
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
            "200": "PayslipObject",
        }
        return await self.api_client.call_api(
            "/Payslip/{PayslipID}",
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

    async def get_settings(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        **kwargs,
    ) -> SettingsObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_settings_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_settings_with_http_info(xero_tenant_id, **kwargs)

    async def get_settings_with_http_info(
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
                    " to method get_settings" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
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
            "200": "SettingsObject",
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

    async def get_superfund(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        super_fund_id: Annotated[
            StrictStr, Field(..., description="Superfund id for single object")
        ],
        **kwargs,
    ) -> SuperFunds:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_superfund_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_superfund_with_http_info(
            xero_tenant_id, super_fund_id, **kwargs
        )

    async def get_superfund_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        super_fund_id: Annotated[
            StrictStr, Field(..., description="Superfund id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "super_fund_id"]
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
                    " to method get_superfund" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["super_fund_id"] is not None:
            _path_params["SuperFundID"] = _params["super_fund_id"]
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
            "200": "SuperFunds",
        }
        return await self.api_client.call_api(
            "/Superfunds/{SuperFundID}",
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

    async def get_superfund_products(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        abn: Annotated[
            Optional[StrictStr], Field(description="The ABN of the Regulated SuperFund")
        ] = None,
        usi: Annotated[
            Optional[StrictStr], Field(description="The USI of the Regulated SuperFund")
        ] = None,
        **kwargs,
    ) -> SuperFundProducts:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_superfund_products_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_superfund_products_with_http_info(
            xero_tenant_id, abn, usi, **kwargs
        )

    async def get_superfund_products_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        abn: Annotated[
            Optional[StrictStr], Field(description="The ABN of the Regulated SuperFund")
        ] = None,
        usi: Annotated[
            Optional[StrictStr], Field(description="The USI of the Regulated SuperFund")
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "abn", "usi"]
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
                    " to method get_superfund_products" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("abn") is not None:
            _query_params.append(("ABN", _params["abn"]))
        if _params.get("usi") is not None:
            _query_params.append(("USI", _params["usi"]))
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
            "200": "SuperFundProducts",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/SuperfundProducts",
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

    async def get_superfunds(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 SuperFunds will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> SuperFunds:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_superfunds_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_superfunds_with_http_info(
            xero_tenant_id, if_modified_since, where, order, page, **kwargs
        )

    async def get_superfunds_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 SuperFunds will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "if_modified_since", "where", "order", "page"]
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
                    " to method get_superfunds" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("where") is not None:
            _query_params.append(("where", _params["where"]))
        if _params.get("order") is not None:
            _query_params.append(("order", _params["order"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["if_modified_since"] is not None:
            _header_params["If-Modified-Since"] = _params["if_modified_since"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "SuperFunds",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/Superfunds",
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

    async def get_timesheet(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Timesheet id for single object")
        ],
        **kwargs,
    ) -> TimesheetObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_timesheet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_timesheet_with_http_info(
            xero_tenant_id, timesheet_id, **kwargs
        )

    async def get_timesheet_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Timesheet id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "timesheet_id"]
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
                    " to method get_timesheet" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["timesheet_id"] is not None:
            _path_params["TimesheetID"] = _params["timesheet_id"]
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
            "200": "TimesheetObject",
        }
        return await self.api_client.call_api(
            "/Timesheets/{TimesheetID}",
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

    async def get_timesheets(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 timesheets will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> Timesheets:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_timesheets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_timesheets_with_http_info(
            xero_tenant_id, if_modified_since, where, order, page, **kwargs
        )

    async def get_timesheets_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        if_modified_since: Annotated[
            Optional[datetime],
            Field(
                description="Only records created or modified since this timestamp will be returned"
            ),
        ] = None,
        where: Annotated[
            Optional[StrictStr], Field(description="Filter by an any element")
        ] = None,
        order: Annotated[
            Optional[StrictStr], Field(description="Order by an any element")
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="e.g. page=1 – Up to 100 timesheets will be returned in a single API call"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "if_modified_since", "where", "order", "page"]
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
                    " to method get_timesheets" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("where") is not None:
            _query_params.append(("where", _params["where"]))
        if _params.get("order") is not None:
            _query_params.append(("order", _params["order"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["if_modified_since"] is not None:
            _header_params["If-Modified-Since"] = _params["if_modified_since"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "Timesheets",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/Timesheets",
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

    async def reject_leave_application(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_application_id: Annotated[
            StrictStr, Field(..., description="Leave Application id for single object")
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> LeaveApplications:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the reject_leave_application_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.reject_leave_application_with_http_info(
            xero_tenant_id, leave_application_id, idempotency_key, **kwargs
        )

    async def reject_leave_application_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_application_id: Annotated[
            StrictStr, Field(..., description="Leave Application id for single object")
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
        _all_params = ["xero_tenant_id", "leave_application_id", "idempotency_key"]
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
                    " to method reject_leave_application" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["leave_application_id"] is not None:
            _path_params["LeaveApplicationID"] = _params["leave_application_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "LeaveApplications",
            "400": "APIException",
        }
        return await self.api_client.call_api(
            "/LeaveApplications/{LeaveApplicationID}/reject",
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

    async def update_employee(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employee: conlist(Employee),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> Employees:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_employee_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_employee_with_http_info(
            xero_tenant_id, employee_id, employee, idempotency_key, **kwargs
        )

    async def update_employee_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employee: conlist(Employee),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id", "employee", "idempotency_key"]
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
                    " to method update_employee" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["employee"] is not None:
            _body_params = _params["employee"]
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
            "200": "Employees",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}",
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

    async def update_leave_application(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_application_id: Annotated[
            StrictStr, Field(..., description="Leave Application id for single object")
        ],
        leave_application: conlist(LeaveApplication),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> LeaveApplications:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_leave_application_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_leave_application_with_http_info(
            xero_tenant_id,
            leave_application_id,
            leave_application,
            idempotency_key,
            **kwargs,
        )

    async def update_leave_application_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_application_id: Annotated[
            StrictStr, Field(..., description="Leave Application id for single object")
        ],
        leave_application: conlist(LeaveApplication),
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
            "leave_application_id",
            "leave_application",
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
                    " to method update_leave_application" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["leave_application_id"] is not None:
            _path_params["LeaveApplicationID"] = _params["leave_application_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["leave_application"] is not None:
            _body_params = _params["leave_application"]
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
            "200": "LeaveApplications",
            "400": None,
        }
        return await self.api_client.call_api(
            "/LeaveApplications/{LeaveApplicationID}",
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

    async def update_pay_run(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run_id: Annotated[
            StrictStr, Field(..., description="PayRun id for single object")
        ],
        pay_run: conlist(PayRun),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> PayRuns:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_pay_run_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_pay_run_with_http_info(
            xero_tenant_id, pay_run_id, pay_run, idempotency_key, **kwargs
        )

    async def update_pay_run_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run_id: Annotated[
            StrictStr, Field(..., description="PayRun id for single object")
        ],
        pay_run: conlist(PayRun),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "pay_run_id", "pay_run", "idempotency_key"]
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
                    " to method update_pay_run" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["pay_run_id"] is not None:
            _path_params["PayRunID"] = _params["pay_run_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["pay_run"] is not None:
            _body_params = _params["pay_run"]
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
            "200": "PayRuns",
        }
        return await self.api_client.call_api(
            "/PayRuns/{PayRunID}",
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

    async def update_payslip(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        payslip_id: Annotated[
            StrictStr, Field(..., description="Payslip id for single object")
        ],
        payslip_lines: conlist(PayslipLines),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> Payslips:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_payslip_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_payslip_with_http_info(
            xero_tenant_id, payslip_id, payslip_lines, idempotency_key, **kwargs
        )

    async def update_payslip_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        payslip_id: Annotated[
            StrictStr, Field(..., description="Payslip id for single object")
        ],
        payslip_lines: conlist(PayslipLines),
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
            "payslip_id",
            "payslip_lines",
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
                    " to method update_payslip" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["payslip_id"] is not None:
            _path_params["PayslipID"] = _params["payslip_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["payslip_lines"] is not None:
            _body_params = _params["payslip_lines"]
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
            "200": "Payslips",
        }
        return await self.api_client.call_api(
            "/Payslip/{PayslipID}",
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

    async def update_superfund(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        super_fund_id: Annotated[
            StrictStr, Field(..., description="Superfund id for single object")
        ],
        super_fund: conlist(SuperFund),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> SuperFunds:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_superfund_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_superfund_with_http_info(
            xero_tenant_id, super_fund_id, super_fund, idempotency_key, **kwargs
        )

    async def update_superfund_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        super_fund_id: Annotated[
            StrictStr, Field(..., description="Superfund id for single object")
        ],
        super_fund: conlist(SuperFund),
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
            "super_fund_id",
            "super_fund",
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
                    " to method update_superfund" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["super_fund_id"] is not None:
            _path_params["SuperFundID"] = _params["super_fund_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["super_fund"] is not None:
            _body_params = _params["super_fund"]
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
            "200": "SuperFunds",
        }
        return await self.api_client.call_api(
            "/Superfunds/{SuperFundID}",
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

    async def update_timesheet(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Timesheet id for single object")
        ],
        timesheet: conlist(Timesheet),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> Timesheets:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_timesheet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_timesheet_with_http_info(
            xero_tenant_id, timesheet_id, timesheet, idempotency_key, **kwargs
        )

    async def update_timesheet_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Timesheet id for single object")
        ],
        timesheet: conlist(Timesheet),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "timesheet_id", "timesheet", "idempotency_key"]
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
                    " to method update_timesheet" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["timesheet_id"] is not None:
            _path_params["TimesheetID"] = _params["timesheet_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["timesheet"] is not None:
            _body_params = _params["timesheet"]
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
            "200": "Timesheets",
        }
        return await self.api_client.call_api(
            "/Timesheets/{TimesheetID}",
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
