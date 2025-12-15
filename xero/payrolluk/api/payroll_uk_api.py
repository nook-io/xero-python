import importlib
from datetime import date
from typing import Optional
from pydantic import (
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    conlist,
)
from typing_extensions import Annotated
from xero.api_client import ApiClient, ApiResponse, ModelFinder
from xero.exceptions import (
    ApiTypeError,
)
from xero.payrolluk.models.benefit import Benefit
from xero.payrolluk.models.benefit_object import BenefitObject
from xero.payrolluk.models.benefits import Benefits
from xero.payrolluk.models.deduction import Deduction
from xero.payrolluk.models.deduction_object import DeductionObject
from xero.payrolluk.models.deductions import Deductions
from xero.payrolluk.models.earnings_order_object import EarningsOrderObject
from xero.payrolluk.models.earnings_orders import EarningsOrders
from xero.payrolluk.models.earnings_rate import EarningsRate
from xero.payrolluk.models.earnings_rate_object import EarningsRateObject
from xero.payrolluk.models.earnings_rates import EarningsRates
from xero.payrolluk.models.earnings_template import EarningsTemplate
from xero.payrolluk.models.earnings_template_object import EarningsTemplateObject
from xero.payrolluk.models.employee import Employee
from xero.payrolluk.models.employee_leave import EmployeeLeave
from xero.payrolluk.models.employee_leave_balances import EmployeeLeaveBalances
from xero.payrolluk.models.employee_leave_object import EmployeeLeaveObject
from xero.payrolluk.models.employee_leave_type import EmployeeLeaveType
from xero.payrolluk.models.employee_leave_type_object import (
    EmployeeLeaveTypeObject,
)
from xero.payrolluk.models.employee_leave_types import EmployeeLeaveTypes
from xero.payrolluk.models.employee_leaves import EmployeeLeaves
from xero.payrolluk.models.employee_object import EmployeeObject
from xero.payrolluk.models.employee_opening_balances import (
    EmployeeOpeningBalances,
)
from xero.payrolluk.models.employee_opening_balances_object import (
    EmployeeOpeningBalancesObject,
)
from xero.payrolluk.models.employee_pay_template_object import (
    EmployeePayTemplateObject,
)
from xero.payrolluk.models.employee_pay_templates import EmployeePayTemplates
from xero.payrolluk.models.employee_statutory_leave_balance_object import (
    EmployeeStatutoryLeaveBalanceObject,
)
from xero.payrolluk.models.employee_statutory_leaves_summaries import (
    EmployeeStatutoryLeavesSummaries,
)
from xero.payrolluk.models.employee_statutory_sick_leave import (
    EmployeeStatutorySickLeave,
)
from xero.payrolluk.models.employee_statutory_sick_leave_object import (
    EmployeeStatutorySickLeaveObject,
)
from xero.payrolluk.models.employee_tax_object import EmployeeTaxObject
from xero.payrolluk.models.employees import Employees
from xero.payrolluk.models.employment import Employment
from xero.payrolluk.models.employment_object import EmploymentObject
from xero.payrolluk.models.leave_periods import LeavePeriods
from xero.payrolluk.models.leave_type import LeaveType
from xero.payrolluk.models.leave_type_object import LeaveTypeObject
from xero.payrolluk.models.leave_types import LeaveTypes
from xero.payrolluk.models.pay_run import PayRun
from xero.payrolluk.models.pay_run_calendar import PayRunCalendar
from xero.payrolluk.models.pay_run_calendar_object import PayRunCalendarObject
from xero.payrolluk.models.pay_run_calendars import PayRunCalendars
from xero.payrolluk.models.pay_run_object import PayRunObject
from xero.payrolluk.models.pay_runs import PayRuns
from xero.payrolluk.models.payment_method import PaymentMethod
from xero.payrolluk.models.payment_method_object import PaymentMethodObject
from xero.payrolluk.models.payslip_object import PayslipObject
from xero.payrolluk.models.payslips import Payslips
from xero.payrolluk.models.reimbursement import Reimbursement
from xero.payrolluk.models.reimbursement_object import ReimbursementObject
from xero.payrolluk.models.reimbursements import Reimbursements
from xero.payrolluk.models.salary_and_wage import SalaryAndWage
from xero.payrolluk.models.salary_and_wage_object import SalaryAndWageObject
from xero.payrolluk.models.salary_and_wages import SalaryAndWages
from xero.payrolluk.models.settings import Settings
from xero.payrolluk.models.timesheet import Timesheet
from xero.payrolluk.models.timesheet_line import TimesheetLine
from xero.payrolluk.models.timesheet_line_object import TimesheetLineObject
from xero.payrolluk.models.timesheet_object import TimesheetObject
from xero.payrolluk.models.timesheets import Timesheets
from xero.payrolluk.models.tracking_categories import TrackingCategories


class PayrollUkApi:
    base_url = "https://api.xero.com/payroll.xro/2.0"
    models_module = importlib.import_module("xero.payrolluk.models")

    def __init__(self, api_client=None, base_url: str | None = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    async def approve_timesheet(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> TimesheetObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the approve_timesheet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.approve_timesheet_with_http_info(
            xero_tenant_id, timesheet_id, idempotency_key, **kwargs
        )

    async def approve_timesheet_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
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
        _all_params = ["xero_tenant_id", "timesheet_id", "idempotency_key"]
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
                    " to method approve_timesheet" % _key
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
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "TimesheetObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Timesheets/{TimesheetID}/Approve",
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

    async def create_benefit(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        benefit: Benefit,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> BenefitObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_benefit_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_benefit_with_http_info(
            xero_tenant_id, benefit, idempotency_key, **kwargs
        )

    async def create_benefit_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        benefit: Benefit,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "benefit", "idempotency_key"]
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
                    " to method create_benefit" % _key
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
        if _params["benefit"] is not None:
            _body_params = _params["benefit"]
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
            "200": "BenefitObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Benefits",
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

    async def create_deduction(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        deduction: Deduction,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> DeductionObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_deduction_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_deduction_with_http_info(
            xero_tenant_id, deduction, idempotency_key, **kwargs
        )

    async def create_deduction_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        deduction: Deduction,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "deduction", "idempotency_key"]
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
                    " to method create_deduction" % _key
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
        if _params["deduction"] is not None:
            _body_params = _params["deduction"]
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
            "200": "DeductionObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Deductions",
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

    async def create_earnings_rate(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        earnings_rate: EarningsRate,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EarningsRateObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_earnings_rate_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_earnings_rate_with_http_info(
            xero_tenant_id, earnings_rate, idempotency_key, **kwargs
        )

    async def create_earnings_rate_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        earnings_rate: EarningsRate,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "earnings_rate", "idempotency_key"]
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
                    " to method create_earnings_rate" % _key
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
        if _params["earnings_rate"] is not None:
            _body_params = _params["earnings_rate"]
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
            "200": "EarningsRateObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/EarningsRates",
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
        employee: Employee,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EmployeeObject:
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
        employee: Employee,
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
            "200": "EmployeeObject",
            "400": "Problem",
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

    async def create_employee_earnings_template(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        earnings_template: EarningsTemplate,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EarningsTemplateObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_employee_earnings_template_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_employee_earnings_template_with_http_info(
            xero_tenant_id, employee_id, earnings_template, idempotency_key, **kwargs
        )

    async def create_employee_earnings_template_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        earnings_template: EarningsTemplate,
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
            "employee_id",
            "earnings_template",
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
                    " to method create_employee_earnings_template" % _key
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
        if _params["earnings_template"] is not None:
            _body_params = _params["earnings_template"]
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
            "200": "EarningsTemplateObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/PayTemplates/earnings",
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

    async def create_employee_leave(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employee_leave: EmployeeLeave,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EmployeeLeaveObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_employee_leave_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_employee_leave_with_http_info(
            xero_tenant_id, employee_id, employee_leave, idempotency_key, **kwargs
        )

    async def create_employee_leave_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employee_leave: EmployeeLeave,
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
            "employee_id",
            "employee_leave",
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
                    " to method create_employee_leave" % _key
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
        if _params["employee_leave"] is not None:
            _body_params = _params["employee_leave"]
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
            "200": "EmployeeLeaveObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/Leave",
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

    async def create_employee_leave_type(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employee_leave_type: EmployeeLeaveType,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EmployeeLeaveTypeObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_employee_leave_type_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_employee_leave_type_with_http_info(
            xero_tenant_id, employee_id, employee_leave_type, idempotency_key, **kwargs
        )

    async def create_employee_leave_type_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employee_leave_type: EmployeeLeaveType,
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
            "employee_id",
            "employee_leave_type",
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
                    " to method create_employee_leave_type" % _key
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
        if _params["employee_leave_type"] is not None:
            _body_params = _params["employee_leave_type"]
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
            "200": "EmployeeLeaveTypeObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/LeaveTypes",
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

    async def create_employee_opening_balances(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employee_opening_balances: EmployeeOpeningBalances,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EmployeeOpeningBalancesObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_employee_opening_balances_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_employee_opening_balances_with_http_info(
            xero_tenant_id,
            employee_id,
            employee_opening_balances,
            idempotency_key,
            **kwargs,
        )

    async def create_employee_opening_balances_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employee_opening_balances: EmployeeOpeningBalances,
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
            "employee_id",
            "employee_opening_balances",
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
                    " to method create_employee_opening_balances" % _key
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
        if _params["employee_opening_balances"] is not None:
            _body_params = _params["employee_opening_balances"]
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
            "200": "EmployeeOpeningBalancesObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/ukopeningbalances",
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

    async def create_employee_payment_method(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        payment_method: PaymentMethod,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> PaymentMethodObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_employee_payment_method_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_employee_payment_method_with_http_info(
            xero_tenant_id, employee_id, payment_method, idempotency_key, **kwargs
        )

    async def create_employee_payment_method_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        payment_method: PaymentMethod,
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
            "employee_id",
            "payment_method",
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
                    " to method create_employee_payment_method" % _key
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
        if _params["payment_method"] is not None:
            _body_params = _params["payment_method"]
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
            "200": "PaymentMethodObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/PaymentMethods",
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

    async def create_employee_salary_and_wage(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        salary_and_wage: SalaryAndWage,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> SalaryAndWageObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_employee_salary_and_wage_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_employee_salary_and_wage_with_http_info(
            xero_tenant_id, employee_id, salary_and_wage, idempotency_key, **kwargs
        )

    async def create_employee_salary_and_wage_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        salary_and_wage: SalaryAndWage,
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
            "employee_id",
            "salary_and_wage",
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
                    " to method create_employee_salary_and_wage" % _key
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
        if _params["salary_and_wage"] is not None:
            _body_params = _params["salary_and_wage"]
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
            "200": "SalaryAndWageObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/SalaryAndWages",
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

    async def create_employee_statutory_sick_leave(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_statutory_sick_leave: EmployeeStatutorySickLeave,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EmployeeStatutorySickLeaveObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_employee_statutory_sick_leave_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_employee_statutory_sick_leave_with_http_info(
            xero_tenant_id, employee_statutory_sick_leave, idempotency_key, **kwargs
        )

    async def create_employee_statutory_sick_leave_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_statutory_sick_leave: EmployeeStatutorySickLeave,
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
            "employee_statutory_sick_leave",
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
                    " to method create_employee_statutory_sick_leave" % _key
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
        if _params["employee_statutory_sick_leave"] is not None:
            _body_params = _params["employee_statutory_sick_leave"]
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
            "200": "EmployeeStatutorySickLeaveObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/StatutoryLeaves/Sick",
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

    async def create_employment(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employment: Employment,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EmploymentObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_employment_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_employment_with_http_info(
            xero_tenant_id, employee_id, employment, idempotency_key, **kwargs
        )

    async def create_employment_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employment: Employment,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id", "employment", "idempotency_key"]
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
                    " to method create_employment" % _key
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
        if _params["employment"] is not None:
            _body_params = _params["employment"]
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
            "200": "EmploymentObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/Employment",
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

    async def create_leave_type(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_type: LeaveType,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> LeaveTypeObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_leave_type_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_leave_type_with_http_info(
            xero_tenant_id, leave_type, idempotency_key, **kwargs
        )

    async def create_leave_type_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_type: LeaveType,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "leave_type", "idempotency_key"]
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
                    " to method create_leave_type" % _key
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
        if _params["leave_type"] is not None:
            _body_params = _params["leave_type"]
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
            "200": "LeaveTypeObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/LeaveTypes",
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

    async def create_multiple_employee_earnings_template(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        earnings_template: conlist(EarningsTemplate),
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EmployeePayTemplates:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_multiple_employee_earnings_template_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_multiple_employee_earnings_template_with_http_info(
            xero_tenant_id, employee_id, earnings_template, idempotency_key, **kwargs
        )

    async def create_multiple_employee_earnings_template_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        earnings_template: conlist(EarningsTemplate),
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
            "employee_id",
            "earnings_template",
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
                    " to method create_multiple_employee_earnings_template" % _key
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
        if _params["earnings_template"] is not None:
            _body_params = _params["earnings_template"]
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
            "200": "EmployeePayTemplates",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/paytemplateearnings",
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

    async def create_pay_run_calendar(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run_calendar: PayRunCalendar,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> PayRunCalendarObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_pay_run_calendar_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_pay_run_calendar_with_http_info(
            xero_tenant_id, pay_run_calendar, idempotency_key, **kwargs
        )

    async def create_pay_run_calendar_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run_calendar: PayRunCalendar,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "pay_run_calendar", "idempotency_key"]
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
                    " to method create_pay_run_calendar" % _key
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
        if _params["pay_run_calendar"] is not None:
            _body_params = _params["pay_run_calendar"]
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
            "200": "PayRunCalendarObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/PayRunCalendars",
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

    async def create_reimbursement(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        reimbursement: Reimbursement,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ReimbursementObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_reimbursement_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_reimbursement_with_http_info(
            xero_tenant_id, reimbursement, idempotency_key, **kwargs
        )

    async def create_reimbursement_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        reimbursement: Reimbursement,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "reimbursement", "idempotency_key"]
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
                    " to method create_reimbursement" % _key
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
        if _params["reimbursement"] is not None:
            _body_params = _params["reimbursement"]
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
            "200": "ReimbursementObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Reimbursements",
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
        timesheet: Timesheet,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> TimesheetObject:
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
        timesheet: Timesheet,
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
            "200": "TimesheetObject",
            "400": "Problem",
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

    async def create_timesheet_line(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
        ],
        timesheet_line: TimesheetLine,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> TimesheetLineObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_timesheet_line_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.create_timesheet_line_with_http_info(
            xero_tenant_id, timesheet_id, timesheet_line, idempotency_key, **kwargs
        )

    async def create_timesheet_line_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
        ],
        timesheet_line: TimesheetLine,
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
            "timesheet_id",
            "timesheet_line",
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
                    " to method create_timesheet_line" % _key
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
        if _params["timesheet_line"] is not None:
            _body_params = _params["timesheet_line"]
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
            "200": "TimesheetLineObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Timesheets/{TimesheetID}/Lines",
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

    async def delete_employee_earnings_template(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        pay_template_earning_id: Annotated[
            StrictStr,
            Field(..., description="Id for single pay template earnings object"),
        ],
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_employee_earnings_template_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.delete_employee_earnings_template_with_http_info(
            xero_tenant_id, employee_id, pay_template_earning_id, **kwargs
        )

    async def delete_employee_earnings_template_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        pay_template_earning_id: Annotated[
            StrictStr,
            Field(..., description="Id for single pay template earnings object"),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id", "pay_template_earning_id"]
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
                    " to method delete_employee_earnings_template" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        if _params["pay_template_earning_id"] is not None:
            _path_params["PayTemplateEarningID"] = _params["pay_template_earning_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _auth_settings = ["OAuth2"]
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/PayTemplates/earnings/{PayTemplateEarningID}",
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

    async def delete_employee_leave(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        leave_id: Annotated[
            StrictStr, Field(..., description="Leave id for single object")
        ],
        **kwargs,
    ) -> EmployeeLeaveObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_employee_leave_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.delete_employee_leave_with_http_info(
            xero_tenant_id, employee_id, leave_id, **kwargs
        )

    async def delete_employee_leave_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        leave_id: Annotated[
            StrictStr, Field(..., description="Leave id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id", "leave_id"]
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
                    " to method delete_employee_leave" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        if _params["leave_id"] is not None:
            _path_params["LeaveID"] = _params["leave_id"]
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
            "200": "EmployeeLeaveObject",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/Leave/{LeaveID}",
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

    async def delete_employee_salary_and_wage(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        salary_and_wages_id: Annotated[
            StrictStr, Field(..., description="Id for single salary and wages object")
        ],
        **kwargs,
    ) -> None:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_employee_salary_and_wage_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.delete_employee_salary_and_wage_with_http_info(
            xero_tenant_id, employee_id, salary_and_wages_id, **kwargs
        )

    async def delete_employee_salary_and_wage_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        salary_and_wages_id: Annotated[
            StrictStr, Field(..., description="Id for single salary and wages object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id", "salary_and_wages_id"]
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
                    " to method delete_employee_salary_and_wage" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        if _params["salary_and_wages_id"] is not None:
            _path_params["SalaryAndWagesID"] = _params["salary_and_wages_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _auth_settings = ["OAuth2"]
        _response_types_map = {}
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/SalaryAndWages/{SalaryAndWagesID}",
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

    async def delete_timesheet(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
        ],
        **kwargs,
    ) -> TimesheetLine:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_timesheet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.delete_timesheet_with_http_info(
            xero_tenant_id, timesheet_id, **kwargs
        )

    async def delete_timesheet_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
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
                    " to method delete_timesheet" % _key
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
            "200": "TimesheetLine",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Timesheets/{TimesheetID}",
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

    async def delete_timesheet_line(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
        ],
        timesheet_line_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet line")
        ],
        **kwargs,
    ) -> TimesheetLine:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_timesheet_line_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.delete_timesheet_line_with_http_info(
            xero_tenant_id, timesheet_id, timesheet_line_id, **kwargs
        )

    async def delete_timesheet_line_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
        ],
        timesheet_line_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet line")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "timesheet_id", "timesheet_line_id"]
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
                    " to method delete_timesheet_line" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["timesheet_id"] is not None:
            _path_params["TimesheetID"] = _params["timesheet_id"]
        if _params["timesheet_line_id"] is not None:
            _path_params["TimesheetLineID"] = _params["timesheet_line_id"]
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
            "200": "TimesheetLine",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Timesheets/{TimesheetID}/Lines/{TimesheetLineID}",
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

    async def get_benefit(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        id: Annotated[StrictStr, Field(..., description="Identifier for the benefit")],
        **kwargs,
    ) -> BenefitObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_benefit_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_benefit_with_http_info(xero_tenant_id, id, **kwargs)

    async def get_benefit_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        id: Annotated[StrictStr, Field(..., description="Identifier for the benefit")],
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
                    " to method get_benefit" % _key
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
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "BenefitObject",
        }
        return await self.api_client.call_api(
            "/Benefits/{id}",
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

    async def get_benefits(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> Benefits:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_benefits_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_benefits_with_http_info(xero_tenant_id, page, **kwargs)

    async def get_benefits_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "page"]
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
                    " to method get_benefits" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
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
            "200": "Benefits",
        }
        return await self.api_client.call_api(
            "/Benefits",
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

    async def get_deduction(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        deduction_id: Annotated[
            StrictStr, Field(..., description="Identifier for the deduction")
        ],
        **kwargs,
    ) -> DeductionObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_deduction_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_deduction_with_http_info(
            xero_tenant_id, deduction_id, **kwargs
        )

    async def get_deduction_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        deduction_id: Annotated[
            StrictStr, Field(..., description="Identifier for the deduction")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "deduction_id"]
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
                    " to method get_deduction" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["deduction_id"] is not None:
            _path_params["deductionId"] = _params["deduction_id"]
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
            "200": "DeductionObject",
        }
        return await self.api_client.call_api(
            "/Deductions/{deductionId}",
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

    async def get_deductions(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> Deductions:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_deductions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_deductions_with_http_info(xero_tenant_id, page, **kwargs)

    async def get_deductions_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "page"]
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
                    " to method get_deductions" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
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
            "200": "Deductions",
        }
        return await self.api_client.call_api(
            "/Deductions",
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

    async def get_earnings_order(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        id: Annotated[
            StrictStr, Field(..., description="Identifier for the deduction")
        ],
        **kwargs,
    ) -> EarningsOrderObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_earnings_order_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_earnings_order_with_http_info(
            xero_tenant_id, id, **kwargs
        )

    async def get_earnings_order_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        id: Annotated[
            StrictStr, Field(..., description="Identifier for the deduction")
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
                    " to method get_earnings_order" % _key
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
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "EarningsOrderObject",
        }
        return await self.api_client.call_api(
            "/EarningsOrders/{id}",
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

    async def get_earnings_orders(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> EarningsOrders:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_earnings_orders_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_earnings_orders_with_http_info(
            xero_tenant_id, page, **kwargs
        )

    async def get_earnings_orders_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "page"]
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
                    " to method get_earnings_orders" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
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
            "200": "EarningsOrders",
        }
        return await self.api_client.call_api(
            "/EarningsOrders",
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

    async def get_earnings_rate(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        earnings_rate_id: Annotated[
            StrictStr, Field(..., description="Identifier for the earnings rate")
        ],
        **kwargs,
    ) -> EarningsRateObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_earnings_rate_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_earnings_rate_with_http_info(
            xero_tenant_id, earnings_rate_id, **kwargs
        )

    async def get_earnings_rate_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        earnings_rate_id: Annotated[
            StrictStr, Field(..., description="Identifier for the earnings rate")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "earnings_rate_id"]
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
                    " to method get_earnings_rate" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["earnings_rate_id"] is not None:
            _path_params["EarningsRateID"] = _params["earnings_rate_id"]
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
            "200": "EarningsRateObject",
        }
        return await self.api_client.call_api(
            "/EarningsRates/{EarningsRateID}",
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

    async def get_earnings_rates(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> EarningsRates:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_earnings_rates_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_earnings_rates_with_http_info(
            xero_tenant_id, page, **kwargs
        )

    async def get_earnings_rates_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "page"]
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
                    " to method get_earnings_rates" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
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
            "200": "EarningsRates",
        }
        return await self.api_client.call_api(
            "/EarningsRates",
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

    async def get_employee(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        **kwargs,
    ) -> EmployeeObject:
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
            "200": "EmployeeObject",
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

    async def get_employee_leave(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        leave_id: Annotated[
            StrictStr, Field(..., description="Leave id for single object")
        ],
        **kwargs,
    ) -> EmployeeLeaveObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_leave_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_leave_with_http_info(
            xero_tenant_id, employee_id, leave_id, **kwargs
        )

    async def get_employee_leave_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        leave_id: Annotated[
            StrictStr, Field(..., description="Leave id for single object")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id", "leave_id"]
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
                    " to method get_employee_leave" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        if _params["leave_id"] is not None:
            _path_params["LeaveID"] = _params["leave_id"]
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
            "200": "EmployeeLeaveObject",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/Leave/{LeaveID}",
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

    async def get_employee_leave_balances(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        **kwargs,
    ) -> EmployeeLeaveBalances:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_leave_balances_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_leave_balances_with_http_info(
            xero_tenant_id, employee_id, **kwargs
        )

    async def get_employee_leave_balances_with_http_info(
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
                    " to method get_employee_leave_balances" % _key
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
            "200": "EmployeeLeaveBalances",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/LeaveBalances",
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

    async def get_employee_leave_periods(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        start_date: Annotated[
            Optional[date], Field(description="Filter by start date")
        ] = None,
        end_date: Annotated[
            Optional[date], Field(description="Filter by end date")
        ] = None,
        **kwargs,
    ) -> LeavePeriods:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_leave_periods_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_leave_periods_with_http_info(
            xero_tenant_id, employee_id, start_date, end_date, **kwargs
        )

    async def get_employee_leave_periods_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        start_date: Annotated[
            Optional[date], Field(description="Filter by start date")
        ] = None,
        end_date: Annotated[
            Optional[date], Field(description="Filter by end date")
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id", "start_date", "end_date"]
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
                    " to method get_employee_leave_periods" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        _query_params = []
        if _params.get("start_date") is not None:
            if isinstance(_params["start_date"], date):
                _query_params.append(
                    (
                        "startDate",
                        _params["start_date"].strftime(
                            self.api_client.configuration.date_format
                        ),
                    )
                )
            else:
                _query_params.append(("startDate", _params["start_date"]))
        if _params.get("end_date") is not None:
            if isinstance(_params["end_date"], date):
                _query_params.append(
                    (
                        "endDate",
                        _params["end_date"].strftime(
                            self.api_client.configuration.date_format
                        ),
                    )
                )
            else:
                _query_params.append(("endDate", _params["end_date"]))
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
            "200": "LeavePeriods",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/LeavePeriods",
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

    async def get_employee_leave_types(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        **kwargs,
    ) -> EmployeeLeaveTypes:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_leave_types_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_leave_types_with_http_info(
            xero_tenant_id, employee_id, **kwargs
        )

    async def get_employee_leave_types_with_http_info(
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
                    " to method get_employee_leave_types" % _key
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
            "200": "EmployeeLeaveTypes",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/LeaveTypes",
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

    async def get_employee_leaves(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        **kwargs,
    ) -> EmployeeLeaves:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_leaves_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_leaves_with_http_info(
            xero_tenant_id, employee_id, **kwargs
        )

    async def get_employee_leaves_with_http_info(
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
                    " to method get_employee_leaves" % _key
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
            "200": "EmployeeLeaves",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/Leave",
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

    async def get_employee_opening_balances(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        **kwargs,
    ) -> EmployeeOpeningBalancesObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_opening_balances_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_opening_balances_with_http_info(
            xero_tenant_id, employee_id, **kwargs
        )

    async def get_employee_opening_balances_with_http_info(
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
                    " to method get_employee_opening_balances" % _key
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
            "200": "EmployeeOpeningBalancesObject",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/ukopeningbalances",
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

    async def get_employee_pay_template(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        **kwargs,
    ) -> EmployeePayTemplateObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_pay_template_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_pay_template_with_http_info(
            xero_tenant_id, employee_id, **kwargs
        )

    async def get_employee_pay_template_with_http_info(
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
                    " to method get_employee_pay_template" % _key
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
            "200": "EmployeePayTemplateObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/PayTemplates",
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

    async def get_employee_payment_method(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        **kwargs,
    ) -> PaymentMethodObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_payment_method_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_payment_method_with_http_info(
            xero_tenant_id, employee_id, **kwargs
        )

    async def get_employee_payment_method_with_http_info(
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
                    " to method get_employee_payment_method" % _key
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
            "200": "PaymentMethodObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/PaymentMethods",
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

    async def get_employee_salary_and_wage(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        salary_and_wages_id: Annotated[
            StrictStr,
            Field(..., description="Id for single pay template earnings object"),
        ],
        **kwargs,
    ) -> SalaryAndWages:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_salary_and_wage_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_salary_and_wage_with_http_info(
            xero_tenant_id, employee_id, salary_and_wages_id, **kwargs
        )

    async def get_employee_salary_and_wage_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        salary_and_wages_id: Annotated[
            StrictStr,
            Field(..., description="Id for single pay template earnings object"),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id", "salary_and_wages_id"]
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
                    " to method get_employee_salary_and_wage" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        if _params["salary_and_wages_id"] is not None:
            _path_params["SalaryAndWagesID"] = _params["salary_and_wages_id"]
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
            "200": "SalaryAndWages",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/SalaryAndWages/{SalaryAndWagesID}",
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

    async def get_employee_salary_and_wages(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> SalaryAndWages:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_salary_and_wages_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_salary_and_wages_with_http_info(
            xero_tenant_id, employee_id, page, **kwargs
        )

    async def get_employee_salary_and_wages_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id", "page"]
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
                    " to method get_employee_salary_and_wages" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
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
            "200": "SalaryAndWages",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/SalaryAndWages",
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

    async def get_employee_statutory_leave_balances(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        leave_type: Annotated[
            Optional[StrictStr],
            Field(description="Filter by the type of statutory leave"),
        ] = None,
        as_of_date: Annotated[
            Optional[date],
            Field(
                description="The date from which to calculate balance remaining. If not specified, current date UTC is used."
            ),
        ] = None,
        **kwargs,
    ) -> EmployeeStatutoryLeaveBalanceObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_statutory_leave_balances_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_statutory_leave_balances_with_http_info(
            xero_tenant_id, employee_id, leave_type, as_of_date, **kwargs
        )

    async def get_employee_statutory_leave_balances_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        leave_type: Annotated[
            Optional[StrictStr],
            Field(description="Filter by the type of statutory leave"),
        ] = None,
        as_of_date: Annotated[
            Optional[date],
            Field(
                description="The date from which to calculate balance remaining. If not specified, current date UTC is used."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id", "leave_type", "as_of_date"]
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
                    " to method get_employee_statutory_leave_balances" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        _query_params = []
        if _params.get("leave_type") is not None:
            _query_params.append(("LeaveType", _params["leave_type"]))
        if _params.get("as_of_date") is not None:
            if isinstance(_params["as_of_date"], date):
                _query_params.append(
                    (
                        "AsOfDate",
                        _params["as_of_date"].strftime(
                            self.api_client.configuration.date_format
                        ),
                    )
                )
            else:
                _query_params.append(("AsOfDate", _params["as_of_date"]))
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
            "200": "EmployeeStatutoryLeaveBalanceObject",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/StatutoryLeaveBalance",
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

    async def get_employee_statutory_sick_leave(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        statutory_sick_leave_id: Annotated[
            StrictStr,
            Field(..., description="Statutory sick leave id for single object"),
        ],
        **kwargs,
    ) -> EmployeeStatutorySickLeaveObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_statutory_sick_leave_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_statutory_sick_leave_with_http_info(
            xero_tenant_id, statutory_sick_leave_id, **kwargs
        )

    async def get_employee_statutory_sick_leave_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        statutory_sick_leave_id: Annotated[
            StrictStr,
            Field(..., description="Statutory sick leave id for single object"),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "statutory_sick_leave_id"]
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
                    " to method get_employee_statutory_sick_leave" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["statutory_sick_leave_id"] is not None:
            _path_params["StatutorySickLeaveID"] = _params["statutory_sick_leave_id"]
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
            "200": "EmployeeStatutorySickLeaveObject",
        }
        return await self.api_client.call_api(
            "/StatutoryLeaves/Sick/{StatutorySickLeaveID}",
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

    async def get_employee_tax(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        **kwargs,
    ) -> EmployeeTaxObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employee_tax_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employee_tax_with_http_info(
            xero_tenant_id, employee_id, **kwargs
        )

    async def get_employee_tax_with_http_info(
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
                    " to method get_employee_tax" % _key
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
            "200": "EmployeeTaxObject",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/Tax",
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
        filter: Annotated[
            Optional[StrictStr],
            Field(
                description="Filter by first name, lastname, and/or whether they are an off-payroll worker"
            ),
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> Employees:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_employees_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_employees_with_http_info(
            xero_tenant_id, filter, page, **kwargs
        )

    async def get_employees_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        filter: Annotated[
            Optional[StrictStr],
            Field(
                description="Filter by first name, lastname, and/or whether they are an off-payroll worker"
            ),
        ] = None,
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "filter", "page"]
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
        if _params.get("filter") is not None:
            _query_params.append(("filter", _params["filter"]))
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
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
            "400": "Problem",
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

    async def get_leave_type(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_type_id: Annotated[
            StrictStr, Field(..., description="Identifier for the leave type")
        ],
        **kwargs,
    ) -> LeaveTypeObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_leave_type_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_leave_type_with_http_info(
            xero_tenant_id, leave_type_id, **kwargs
        )

    async def get_leave_type_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        leave_type_id: Annotated[
            StrictStr, Field(..., description="Identifier for the leave type")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "leave_type_id"]
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
                    " to method get_leave_type" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["leave_type_id"] is not None:
            _path_params["LeaveTypeID"] = _params["leave_type_id"]
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
            "200": "LeaveTypeObject",
        }
        return await self.api_client.call_api(
            "/LeaveTypes/{LeaveTypeID}",
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

    async def get_leave_types(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        active_only: Annotated[
            Optional[StrictBool],
            Field(
                description="Filters leave types by active status. By default the API returns all leave types."
            ),
        ] = None,
        **kwargs,
    ) -> LeaveTypes:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_leave_types_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_leave_types_with_http_info(
            xero_tenant_id, page, active_only, **kwargs
        )

    async def get_leave_types_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        active_only: Annotated[
            Optional[StrictBool],
            Field(
                description="Filters leave types by active status. By default the API returns all leave types."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "page", "active_only"]
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
                    " to method get_leave_types" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        if _params.get("active_only") is not None:
            _query_params.append(("ActiveOnly", _params["active_only"]))
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
            "200": "LeaveTypes",
        }
        return await self.api_client.call_api(
            "/LeaveTypes",
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
            StrictStr, Field(..., description="Identifier for the pay run")
        ],
        **kwargs,
    ) -> PayRunObject:
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
            StrictStr, Field(..., description="Identifier for the pay run")
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
            "200": "PayRunObject",
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

    async def get_pay_run_calendar(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run_calendar_id: Annotated[
            StrictStr, Field(..., description="Identifier for the payrun calendars")
        ],
        **kwargs,
    ) -> PayRunCalendarObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_pay_run_calendar_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_pay_run_calendar_with_http_info(
            xero_tenant_id, pay_run_calendar_id, **kwargs
        )

    async def get_pay_run_calendar_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run_calendar_id: Annotated[
            StrictStr, Field(..., description="Identifier for the payrun calendars")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "pay_run_calendar_id"]
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
                    " to method get_pay_run_calendar" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["pay_run_calendar_id"] is not None:
            _path_params["PayRunCalendarID"] = _params["pay_run_calendar_id"]
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
            "200": "PayRunCalendarObject",
        }
        return await self.api_client.call_api(
            "/PayRunCalendars/{PayRunCalendarID}",
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

    async def get_pay_run_calendars(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> PayRunCalendars:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_pay_run_calendars_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_pay_run_calendars_with_http_info(
            xero_tenant_id, page, **kwargs
        )

    async def get_pay_run_calendars_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "page"]
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
                    " to method get_pay_run_calendars" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
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
            "200": "PayRunCalendars",
        }
        return await self.api_client.call_api(
            "/PayRunCalendars",
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
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        status: Annotated[
            Optional[StrictStr],
            Field(
                description="By default get payruns will return all the payruns for an organization. You can add GET https://api.xero.com/payroll.xro/2.0/payRuns?statu={PayRunStatus} to filter the payruns by status."
            ),
        ] = None,
        **kwargs,
    ) -> PayRuns:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_pay_runs_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_pay_runs_with_http_info(
            xero_tenant_id, page, status, **kwargs
        )

    async def get_pay_runs_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        status: Annotated[
            Optional[StrictStr],
            Field(
                description="By default get payruns will return all the payruns for an organization. You can add GET https://api.xero.com/payroll.xro/2.0/payRuns?statu={PayRunStatus} to filter the payruns by status."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "page", "status"]
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
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        if _params.get("status") is not None:
            _query_params.append(("status", _params["status"]))
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

    async def get_pay_slip(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        payslip_id: Annotated[
            StrictStr, Field(..., description="Identifier for the payslip")
        ],
        **kwargs,
    ) -> PayslipObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_pay_slip_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_pay_slip_with_http_info(
            xero_tenant_id, payslip_id, **kwargs
        )

    async def get_pay_slip_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        payslip_id: Annotated[
            StrictStr, Field(..., description="Identifier for the payslip")
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
                    " to method get_pay_slip" % _key
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
            "/Payslips/{PayslipID}",
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

    async def get_pay_slips(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="PayrunID which specifies the containing payrun of payslips to retrieve. By default, the API does not group payslips by payrun.",
            ),
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> Payslips:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_pay_slips_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_pay_slips_with_http_info(
            xero_tenant_id, pay_run_id, page, **kwargs
        )

    async def get_pay_slips_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run_id: Annotated[
            StrictStr,
            Field(
                ...,
                description="PayrunID which specifies the containing payrun of payslips to retrieve. By default, the API does not group payslips by payrun.",
            ),
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "pay_run_id", "page"]
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
                    " to method get_pay_slips" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        if _params.get("pay_run_id") is not None:
            _query_params.append(("PayRunID", _params["pay_run_id"]))
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
            "200": "Payslips",
        }
        return await self.api_client.call_api(
            "/Payslips",
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

    async def get_reimbursement(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        reimbursement_id: Annotated[
            StrictStr, Field(..., description="Identifier for the reimbursement")
        ],
        **kwargs,
    ) -> ReimbursementObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_reimbursement_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_reimbursement_with_http_info(
            xero_tenant_id, reimbursement_id, **kwargs
        )

    async def get_reimbursement_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        reimbursement_id: Annotated[
            StrictStr, Field(..., description="Identifier for the reimbursement")
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "reimbursement_id"]
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
                    " to method get_reimbursement" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["reimbursement_id"] is not None:
            _path_params["ReimbursementID"] = _params["reimbursement_id"]
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
            "200": "ReimbursementObject",
        }
        return await self.api_client.call_api(
            "/Reimbursements/{ReimbursementID}",
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

    async def get_reimbursements(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> Reimbursements:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_reimbursements_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_reimbursements_with_http_info(
            xero_tenant_id, page, **kwargs
        )

    async def get_reimbursements_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "page"]
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
                    " to method get_reimbursements" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
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
            "200": "Reimbursements",
        }
        return await self.api_client.call_api(
            "/Reimbursements",
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
    ) -> Settings:
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
            "200": "Settings",
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

    async def get_statutory_leave_summary(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        active_only: Annotated[
            Optional[StrictBool],
            Field(
                description="Filter response with leaves that are currently active or yet to be taken. If not specified, all leaves (past, current, and future scheduled) are returned"
            ),
        ] = None,
        **kwargs,
    ) -> EmployeeStatutoryLeavesSummaries:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_statutory_leave_summary_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_statutory_leave_summary_with_http_info(
            xero_tenant_id, employee_id, active_only, **kwargs
        )

    async def get_statutory_leave_summary_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        active_only: Annotated[
            Optional[StrictBool],
            Field(
                description="Filter response with leaves that are currently active or yet to be taken. If not specified, all leaves (past, current, and future scheduled) are returned"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["xero_tenant_id", "employee_id", "active_only"]
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
                    " to method get_statutory_leave_summary" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        _query_params = []
        if _params.get("active_only") is not None:
            _query_params.append(("activeOnly", _params["active_only"]))
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
            "200": "EmployeeStatutoryLeavesSummaries",
        }
        return await self.api_client.call_api(
            "/StatutoryLeaves/Summary/{EmployeeID}",
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
            StrictStr, Field(..., description="Identifier for the timesheet")
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
            StrictStr, Field(..., description="Identifier for the timesheet")
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
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        filter: Annotated[
            Optional[StrictStr],
            Field(description="Filter by employeeId and/or payrollCalendarId"),
        ] = None,
        status: Annotated[
            Optional[StrictStr],
            Field(
                description="filter results by any timesheets with a matching timesheet status"
            ),
        ] = None,
        start_date: Annotated[
            Optional[StrictStr],
            Field(
                description="filter results by any timesheets with a startDate on or after the provided date"
            ),
        ] = None,
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="filter results by any timesheets with a endDate on or before the provided date"
            ),
        ] = None,
        sort: Annotated[
            Optional[StrictStr],
            Field(
                description="sort the order of timesheets returned. The default is based on the timesheets createdDate, sorted oldest to newest. Currently, the only other option is to reverse the order based on the timesheets startDate, sorted newest to oldest."
            ),
        ] = None,
        **kwargs,
    ) -> Timesheets:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_timesheets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_timesheets_with_http_info(
            xero_tenant_id, page, filter, status, start_date, end_date, sort, **kwargs
        )

    async def get_timesheets_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        page: Annotated[
            Optional[StrictInt],
            Field(
                description="Page number which specifies the set of records to retrieve. By default the number of the records per set is 100."
            ),
        ] = None,
        filter: Annotated[
            Optional[StrictStr],
            Field(description="Filter by employeeId and/or payrollCalendarId"),
        ] = None,
        status: Annotated[
            Optional[StrictStr],
            Field(
                description="filter results by any timesheets with a matching timesheet status"
            ),
        ] = None,
        start_date: Annotated[
            Optional[StrictStr],
            Field(
                description="filter results by any timesheets with a startDate on or after the provided date"
            ),
        ] = None,
        end_date: Annotated[
            Optional[StrictStr],
            Field(
                description="filter results by any timesheets with a endDate on or before the provided date"
            ),
        ] = None,
        sort: Annotated[
            Optional[StrictStr],
            Field(
                description="sort the order of timesheets returned. The default is based on the timesheets createdDate, sorted oldest to newest. Currently, the only other option is to reverse the order based on the timesheets startDate, sorted newest to oldest."
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "xero_tenant_id",
            "page",
            "filter",
            "status",
            "start_date",
            "end_date",
            "sort",
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
                    " to method get_timesheets" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        if _params.get("page") is not None:
            _query_params.append(("page", _params["page"]))
        if _params.get("filter") is not None:
            _query_params.append(("filter", _params["filter"]))
        if _params.get("status") is not None:
            _query_params.append(("status", _params["status"]))
        if _params.get("start_date") is not None:
            _query_params.append(("startDate", _params["start_date"]))
        if _params.get("end_date") is not None:
            _query_params.append(("endDate", _params["end_date"]))
        if _params.get("sort") is not None:
            _query_params.append(("sort", _params["sort"]))
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
            "200": "Timesheets",
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

    async def get_tracking_categories(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        **kwargs,
    ) -> TrackingCategories:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_tracking_categories_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.get_tracking_categories_with_http_info(
            xero_tenant_id, **kwargs
        )

    async def get_tracking_categories_with_http_info(
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
                    " to method get_tracking_categories" % _key
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
            "200": "TrackingCategories",
        }
        return await self.api_client.call_api(
            "/Settings/trackingCategories",
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

    async def revert_timesheet(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
        ],
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> TimesheetObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the revert_timesheet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.revert_timesheet_with_http_info(
            xero_tenant_id, timesheet_id, idempotency_key, **kwargs
        )

    async def revert_timesheet_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
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
        _all_params = ["xero_tenant_id", "timesheet_id", "idempotency_key"]
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
                    " to method revert_timesheet" % _key
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
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        _auth_settings = ["OAuth2"]
        _response_types_map = {
            "200": "TimesheetObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Timesheets/{TimesheetID}/RevertToDraft",
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
        employee: Employee,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EmployeeObject:
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
        employee: Employee,
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
            "200": "EmployeeObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}",
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

    async def update_employee_earnings_template(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        pay_template_earning_id: Annotated[
            StrictStr,
            Field(..., description="Id for single pay template earnings object"),
        ],
        earnings_template: EarningsTemplate,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EarningsTemplateObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_employee_earnings_template_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_employee_earnings_template_with_http_info(
            xero_tenant_id,
            employee_id,
            pay_template_earning_id,
            earnings_template,
            idempotency_key,
            **kwargs,
        )

    async def update_employee_earnings_template_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        pay_template_earning_id: Annotated[
            StrictStr,
            Field(..., description="Id for single pay template earnings object"),
        ],
        earnings_template: EarningsTemplate,
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
            "employee_id",
            "pay_template_earning_id",
            "earnings_template",
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
                    " to method update_employee_earnings_template" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        if _params["pay_template_earning_id"] is not None:
            _path_params["PayTemplateEarningID"] = _params["pay_template_earning_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["earnings_template"] is not None:
            _body_params = _params["earnings_template"]
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
            "200": "EarningsTemplateObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/PayTemplates/earnings/{PayTemplateEarningID}",
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

    async def update_employee_leave(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        leave_id: Annotated[
            StrictStr, Field(..., description="Leave id for single object")
        ],
        employee_leave: EmployeeLeave,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EmployeeLeaveObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_employee_leave_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_employee_leave_with_http_info(
            xero_tenant_id,
            employee_id,
            leave_id,
            employee_leave,
            idempotency_key,
            **kwargs,
        )

    async def update_employee_leave_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        leave_id: Annotated[
            StrictStr, Field(..., description="Leave id for single object")
        ],
        employee_leave: EmployeeLeave,
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
            "employee_id",
            "leave_id",
            "employee_leave",
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
                    " to method update_employee_leave" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        if _params["leave_id"] is not None:
            _path_params["LeaveID"] = _params["leave_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["employee_leave"] is not None:
            _body_params = _params["employee_leave"]
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
            "200": "EmployeeLeaveObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/Leave/{LeaveID}",
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

    async def update_employee_opening_balances(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employee_opening_balances: EmployeeOpeningBalances,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> EmployeeOpeningBalancesObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_employee_opening_balances_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_employee_opening_balances_with_http_info(
            xero_tenant_id,
            employee_id,
            employee_opening_balances,
            idempotency_key,
            **kwargs,
        )

    async def update_employee_opening_balances_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        employee_opening_balances: EmployeeOpeningBalances,
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
            "employee_id",
            "employee_opening_balances",
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
                    " to method update_employee_opening_balances" % _key
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
        if _params["employee_opening_balances"] is not None:
            _body_params = _params["employee_opening_balances"]
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
            "200": "EmployeeOpeningBalancesObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/ukopeningbalances",
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

    async def update_employee_salary_and_wage(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        salary_and_wages_id: Annotated[
            StrictStr,
            Field(..., description="Id for single pay template earnings object"),
        ],
        salary_and_wage: SalaryAndWage,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> SalaryAndWageObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_employee_salary_and_wage_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_employee_salary_and_wage_with_http_info(
            xero_tenant_id,
            employee_id,
            salary_and_wages_id,
            salary_and_wage,
            idempotency_key,
            **kwargs,
        )

    async def update_employee_salary_and_wage_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        employee_id: Annotated[
            StrictStr, Field(..., description="Employee id for single object")
        ],
        salary_and_wages_id: Annotated[
            StrictStr,
            Field(..., description="Id for single pay template earnings object"),
        ],
        salary_and_wage: SalaryAndWage,
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
            "employee_id",
            "salary_and_wages_id",
            "salary_and_wage",
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
                    " to method update_employee_salary_and_wage" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["employee_id"] is not None:
            _path_params["EmployeeID"] = _params["employee_id"]
        if _params["salary_and_wages_id"] is not None:
            _path_params["SalaryAndWagesID"] = _params["salary_and_wages_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["salary_and_wage"] is not None:
            _body_params = _params["salary_and_wage"]
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
            "200": "SalaryAndWageObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Employees/{EmployeeID}/SalaryAndWages/{SalaryAndWagesID}",
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

    async def update_pay_run(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        pay_run_id: Annotated[
            StrictStr, Field(..., description="Identifier for the pay run")
        ],
        pay_run: PayRun,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> PayRunObject:
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
            StrictStr, Field(..., description="Identifier for the pay run")
        ],
        pay_run: PayRun,
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
            "200": "PayRunObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/PayRuns/{PayRunID}",
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

    async def update_timesheet_line(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
        ],
        timesheet_line_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet line")
        ],
        timesheet_line: TimesheetLine,
        idempotency_key: Annotated[
            Optional[StrictStr],
            Field(
                description="This allows you to safely retry requests without the risk of duplicate processing. 128 character max."
            ),
        ] = None,
        **kwargs,
    ) -> TimesheetLineObject:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_timesheet_line_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return await self.update_timesheet_line_with_http_info(
            xero_tenant_id,
            timesheet_id,
            timesheet_line_id,
            timesheet_line,
            idempotency_key,
            **kwargs,
        )

    async def update_timesheet_line_with_http_info(
        self,
        xero_tenant_id: Annotated[
            StrictStr, Field(..., description="Xero identifier for Tenant")
        ],
        timesheet_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet")
        ],
        timesheet_line_id: Annotated[
            StrictStr, Field(..., description="Identifier for the timesheet line")
        ],
        timesheet_line: TimesheetLine,
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
            "timesheet_id",
            "timesheet_line_id",
            "timesheet_line",
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
                    " to method update_timesheet_line" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["timesheet_id"] is not None:
            _path_params["TimesheetID"] = _params["timesheet_id"]
        if _params["timesheet_line_id"] is not None:
            _path_params["TimesheetLineID"] = _params["timesheet_line_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["xero_tenant_id"] is not None:
            _header_params["Xero-Tenant-Id"] = _params["xero_tenant_id"]
        if _params["idempotency_key"] is not None:
            _header_params["Idempotency-Key"] = _params["idempotency_key"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["timesheet_line"] is not None:
            _body_params = _params["timesheet_line"]
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
            "200": "TimesheetLineObject",
            "400": "Problem",
        }
        return await self.api_client.call_api(
            "/Timesheets/{TimesheetID}/Lines/{TimesheetLineID}",
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
