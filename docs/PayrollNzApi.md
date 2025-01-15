# xero_python.PayrollNzApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee_earnings_template**](PayrollNzApi.md#create_employee_earnings_template) | **POST** /Employees/{EmployeeID}/PayTemplates/Earnings | Creates earnings template records for an employee
[**create_employee_leave_setup**](PayrollNzApi.md#create_employee_leave_setup) | **POST** /Employees/{EmployeeID}/LeaveSetup | Creates a leave set-up for a specific employee. This is required before viewing, configuring and requesting leave for an employee
[**create_employee_opening_balances**](PayrollNzApi.md#create_employee_opening_balances) | **POST** /Employees/{EmployeeID}/OpeningBalances | Creates opening balances for a specific employee
[**create_employee_working_pattern**](PayrollNzApi.md#create_employee_working_pattern) | **POST** /Employees/{EmployeeID}/Working-Patterns | Creates an employee working pattern
[**create_multiple_employee_earnings_template**](PayrollNzApi.md#create_multiple_employee_earnings_template) | **POST** /Employees/{EmployeeID}/PayTemplateEarnings | Creates multiple employee earnings template records for a specific employee
[**create_superannuation**](PayrollNzApi.md#create_superannuation) | **POST** /Superannuations | Creates a new superannuation
[**delete_employee_earnings_template**](PayrollNzApi.md#delete_employee_earnings_template) | **DELETE** /Employees/{EmployeeID}/PayTemplates/Earnings/{PayTemplateEarningID} | Deletes an employee&#39;s earnings template record
[**delete_employee_working_pattern**](PayrollNzApi.md#delete_employee_working_pattern) | **DELETE** /Employees/{EmployeeID}/Working-Patterns/{EmployeeWorkingPatternID} | deletes employee&#39;s working patterns
[**get_employee_opening_balances**](PayrollNzApi.md#get_employee_opening_balances) | **GET** /Employees/{EmployeeID}/OpeningBalances | Retrieves the opening balance for a specific employee
[**get_employee_working_pattern**](PayrollNzApi.md#get_employee_working_pattern) | **GET** /Employees/{EmployeeID}/Working-Patterns/{EmployeeWorkingPatternID} | Retrieves employee&#39;s working patterns
[**get_employee_working_patterns**](PayrollNzApi.md#get_employee_working_patterns) | **GET** /Employees/{EmployeeID}/Working-Patterns | Retrieves employee&#39;s working patterns
[**get_pay_run_calendar**](PayrollNzApi.md#get_pay_run_calendar) | **GET** /PayRunCalendars/{PayrollCalendarID} | Retrieves a specific payrun calendar by using a unique payroll calendar ID
[**get_pay_slip**](PayrollNzApi.md#get_pay_slip) | **GET** /PaySlips/{PaySlipID} | Retrieves a specific payslip by a unique pay slip ID
[**get_pay_slips**](PayrollNzApi.md#get_pay_slips) | **GET** /PaySlips | Retrieves payslips
[**get_statutory_deduction**](PayrollNzApi.md#get_statutory_deduction) | **GET** /StatutoryDeductions/{id} | Retrieves a specific statutory deduction by using a unique statutory deductions id
[**get_statutory_deductions**](PayrollNzApi.md#get_statutory_deductions) | **GET** /StatutoryDeductions | Retrieves statutory deductions
[**get_superannuation**](PayrollNzApi.md#get_superannuation) | **GET** /Superannuations/{SuperannuationID} | Retrieves a specific superannuation using a unique superannuation ID
[**get_superannuations**](PayrollNzApi.md#get_superannuations) | **GET** /Superannuations | Retrieves superannuations
[**get_tracking_categories**](PayrollNzApi.md#get_tracking_categories) | **GET** /Settings/TrackingCategories | Retrieves tracking categories
[**update_employee_earnings_template**](PayrollNzApi.md#update_employee_earnings_template) | **PUT** /Employees/{EmployeeID}/PayTemplates/Earnings/{PayTemplateEarningID} | Updates an earnings template records for an employee
[**update_pay_slip_line_items**](PayrollNzApi.md#update_pay_slip_line_items) | **PUT** /PaySlips/{PaySlipID} | Creates an employee pay slip


# **create_employee_earnings_template**
> EarningsTemplateObject create_employee_earnings_template(xero_tenant_id, employee_id, earnings_template, idempotency_key=idempotency_key)

Creates earnings template records for an employee

### Example

```python
import time
import os
import xero_python
from xero_python.models.earnings_template import EarningsTemplate
from xero_python.models.earnings_template_object import EarningsTemplateObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
    earnings_template = {ratePerUnit=20, numberOfUnits=8, earningsRateID=f9d8f5b5-9049-47f4-8541-35e200f750a5, name=My New One} # EarningsTemplate | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates earnings template records for an employee
        api_response = await api_instance.create_employee_earnings_template(xero_tenant_id, employee_id, earnings_template, idempotency_key=idempotency_key)
        print("The response of PayrollNzApi->create_employee_earnings_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->create_employee_earnings_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | **str**| Employee id for single object | 
 **earnings_template** | [**EarningsTemplate**](EarningsTemplate.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**EarningsTemplateObject**](EarningsTemplateObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_leave_setup**
> EmployeeLeaveSetupObject create_employee_leave_setup(xero_tenant_id, employee_id, employee_leave_setup, idempotency_key=idempotency_key)

Creates a leave set-up for a specific employee. This is required before viewing, configuring and requesting leave for an employee

### Example

```python
import time
import os
import xero_python
from xero_python.models.employee_leave_setup import EmployeeLeaveSetup
from xero_python.models.employee_leave_setup_object import EmployeeLeaveSetupObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
    employee_leave_setup = {holidayPayOpeningBalance=10, annualLeaveOpeningBalance=100, sickLeaveHoursToAccrueAnnually=20, sickLeaveToAccrueAnnually=20, sickLeaveOpeningBalance=10, sickLeaveScheduleOfAccrual=OnAnniversaryDate, sickLeaveAnniversaryDate=2023-12-31, annualLeaveAnniversaryDate=2023-12-31} # EmployeeLeaveSetup | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates a leave set-up for a specific employee. This is required before viewing, configuring and requesting leave for an employee
        api_response = await api_instance.create_employee_leave_setup(xero_tenant_id, employee_id, employee_leave_setup, idempotency_key=idempotency_key)
        print("The response of PayrollNzApi->create_employee_leave_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->create_employee_leave_setup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | **str**| Employee id for single object | 
 **employee_leave_setup** | [**EmployeeLeaveSetup**](EmployeeLeaveSetup.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**EmployeeLeaveSetupObject**](EmployeeLeaveSetupObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_opening_balances**
> EmployeeOpeningBalancesObject create_employee_opening_balances(xero_tenant_id, employee_id, employee_opening_balance, idempotency_key=idempotency_key)

Creates opening balances for a specific employee

### Example

```python
import time
import os
import xero_python
from xero_python.models.employee_opening_balance import EmployeeOpeningBalance
from xero_python.models.employee_opening_balances_object import EmployeeOpeningBalancesObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
    employee_opening_balance = [{"periodEndDate":"2020-10-01","daysPaid":3,"unpaidWeeks":2,"grossEarnings":40.0}] # List[EmployeeOpeningBalance] | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates opening balances for a specific employee
        api_response = await api_instance.create_employee_opening_balances(xero_tenant_id, employee_id, employee_opening_balance, idempotency_key=idempotency_key)
        print("The response of PayrollNzApi->create_employee_opening_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->create_employee_opening_balances: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | **str**| Employee id for single object | 
 **employee_opening_balance** | [**List[EmployeeOpeningBalance]**](EmployeeOpeningBalance.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**EmployeeOpeningBalancesObject**](EmployeeOpeningBalancesObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_working_pattern**
> EmployeeWorkingPatternWithWorkingWeeksObject create_employee_working_pattern(xero_tenant_id, employee_id, employee_working_pattern_with_working_weeks_request, idempotency_key=idempotency_key)

Creates an employee working pattern

### Example

```python
import time
import os
import xero_python
from xero_python.models.employee_working_pattern_with_working_weeks_object import EmployeeWorkingPatternWithWorkingWeeksObject
from xero_python.models.employee_working_pattern_with_working_weeks_request import EmployeeWorkingPatternWithWorkingWeeksRequest
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
    employee_working_pattern_with_working_weeks_request = {effectiveFrom=2020-01-01T00:00:00, workingWeeks=[{monday=0.0, tuesday=3.0, wednesday=0.0, thursday=0.0, friday=0.0, saturday=0.0, sunday=0.0}]} # EmployeeWorkingPatternWithWorkingWeeksRequest | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates an employee working pattern
        api_response = await api_instance.create_employee_working_pattern(xero_tenant_id, employee_id, employee_working_pattern_with_working_weeks_request, idempotency_key=idempotency_key)
        print("The response of PayrollNzApi->create_employee_working_pattern:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->create_employee_working_pattern: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | **str**| Employee id for single object | 
 **employee_working_pattern_with_working_weeks_request** | [**EmployeeWorkingPatternWithWorkingWeeksRequest**](EmployeeWorkingPatternWithWorkingWeeksRequest.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**EmployeeWorkingPatternWithWorkingWeeksObject**](EmployeeWorkingPatternWithWorkingWeeksObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | employee working pattern correctly added |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_employee_earnings_template**
> EmployeeEarningsTemplates create_multiple_employee_earnings_template(xero_tenant_id, employee_id, earnings_template, idempotency_key=idempotency_key)

Creates multiple employee earnings template records for a specific employee

### Example

```python
import time
import os
import xero_python
from xero_python.models.earnings_template import EarningsTemplate
from xero_python.models.employee_earnings_templates import EmployeeEarningsTemplates
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
    earnings_template = [{"ratePerUnit":20.0,"numberOfUnits":8.0,"earningsRateID":"f9d8f5b5-9049-47f4-8541-35e200f750a5"},{"ratePerUnit":0.0,"numberOfUnits":8.0,"earningsRateID":"65b83d94-f20f-45e1-85ae-387fcf460c26"}] # List[EarningsTemplate] | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates multiple employee earnings template records for a specific employee
        api_response = await api_instance.create_multiple_employee_earnings_template(xero_tenant_id, employee_id, earnings_template, idempotency_key=idempotency_key)
        print("The response of PayrollNzApi->create_multiple_employee_earnings_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->create_multiple_employee_earnings_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | **str**| Employee id for single object | 
 **earnings_template** | [**List[EarningsTemplate]**](EarningsTemplate.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**EmployeeEarningsTemplates**](EmployeeEarningsTemplates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_superannuation**
> SuperannuationObject create_superannuation(xero_tenant_id, benefit, idempotency_key=idempotency_key)

Creates a new superannuation

### Example

```python
import time
import os
import xero_python
from xero_python.models.benefit import Benefit
from xero_python.models.superannuation_object import SuperannuationObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    benefit = {name=SidSaver, category=Other, liabilityAccountId=568f2e9a-0870-46cc-8678-f83f132ed4e3, expenseAccountId=e4eb36f6-97e3-4427-a394-dd4e1b355c2e, CalculationTypeNZ=FixedAmount, standardAmount=10} # Benefit | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates a new superannuation
        api_response = await api_instance.create_superannuation(xero_tenant_id, benefit, idempotency_key=idempotency_key)
        print("The response of PayrollNzApi->create_superannuation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->create_superannuation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **benefit** | [**Benefit**](Benefit.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**SuperannuationObject**](SuperannuationObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_earnings_template**
> EarningsTemplateObject delete_employee_earnings_template(xero_tenant_id, employee_id, pay_template_earning_id)

Deletes an employee's earnings template record

### Example

```python
import time
import os
import xero_python
from xero_python.models.earnings_template_object import EarningsTemplateObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
    pay_template_earning_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Id for single pay template earnings object

    try:
        # Deletes an employee's earnings template record
        api_response = await api_instance.delete_employee_earnings_template(xero_tenant_id, employee_id, pay_template_earning_id)
        print("The response of PayrollNzApi->delete_employee_earnings_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->delete_employee_earnings_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | **str**| Employee id for single object | 
 **pay_template_earning_id** | **str**| Id for single pay template earnings object | 

### Return type

[**EarningsTemplateObject**](EarningsTemplateObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deletion successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_working_pattern**
> EmployeeLeaveObject delete_employee_working_pattern(xero_tenant_id, employee_id, employee_working_pattern_id)

deletes employee's working patterns

### Example

```python
import time
import os
import xero_python
from xero_python.models.employee_leave_object import EmployeeLeaveObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
    employee_working_pattern_id = '4ff1e5cc-9835-40d5-bb18-09f3b118db9c' # str | Employee working pattern id for single object

    try:
        # deletes employee's working patterns
        api_response = await api_instance.delete_employee_working_pattern(xero_tenant_id, employee_id, employee_working_pattern_id)
        print("The response of PayrollNzApi->delete_employee_working_pattern:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->delete_employee_working_pattern: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | **str**| Employee id for single object | 
 **employee_working_pattern_id** | **str**| Employee working pattern id for single object | 

### Return type

[**EmployeeLeaveObject**](EmployeeLeaveObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful response |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_opening_balances**
> EmployeeOpeningBalancesObject get_employee_opening_balances(xero_tenant_id, employee_id)

Retrieves the opening balance for a specific employee

### Example

```python
import time
import os
import xero_python
from xero_python.models.employee_opening_balances_object import EmployeeOpeningBalancesObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object

    try:
        # Retrieves the opening balance for a specific employee
        api_response = await api_instance.get_employee_opening_balances(xero_tenant_id, employee_id)
        print("The response of PayrollNzApi->get_employee_opening_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->get_employee_opening_balances: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | **str**| Employee id for single object | 

### Return type

[**EmployeeOpeningBalancesObject**](EmployeeOpeningBalancesObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_working_pattern**
> EmployeeWorkingPatternWithWorkingWeeksObject get_employee_working_pattern(xero_tenant_id, employee_id, employee_working_pattern_id)

Retrieves employee's working patterns

### Example

```python
import time
import os
import xero_python
from xero_python.models.employee_working_pattern_with_working_weeks_object import EmployeeWorkingPatternWithWorkingWeeksObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
    employee_working_pattern_id = '4ff1e5cc-9835-40d5-bb18-09f3b118db9c' # str | Employee working pattern id for single object

    try:
        # Retrieves employee's working patterns
        api_response = await api_instance.get_employee_working_pattern(xero_tenant_id, employee_id, employee_working_pattern_id)
        print("The response of PayrollNzApi->get_employee_working_pattern:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->get_employee_working_pattern: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | **str**| Employee id for single object | 
 **employee_working_pattern_id** | **str**| Employee working pattern id for single object | 

### Return type

[**EmployeeWorkingPatternWithWorkingWeeksObject**](EmployeeWorkingPatternWithWorkingWeeksObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_working_patterns**
> EmployeeWorkingPatternsObject get_employee_working_patterns(xero_tenant_id, employee_id)

Retrieves employee's working patterns

### Example

```python
import time
import os
import xero_python
from xero_python.models.employee_working_patterns_object import EmployeeWorkingPatternsObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object

    try:
        # Retrieves employee's working patterns
        api_response = await api_instance.get_employee_working_patterns(xero_tenant_id, employee_id)
        print("The response of PayrollNzApi->get_employee_working_patterns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->get_employee_working_patterns: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | **str**| Employee id for single object | 

### Return type

[**EmployeeWorkingPatternsObject**](EmployeeWorkingPatternsObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_run_calendar**
> PayRunCalendarObject get_pay_run_calendar(xero_tenant_id, payroll_calendar_id)

Retrieves a specific payrun calendar by using a unique payroll calendar ID

### Example

```python
import time
import os
import xero_python
from xero_python.models.pay_run_calendar_object import PayRunCalendarObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    payroll_calendar_id = 'payroll_calendar_id_example' # str | Identifier for the payrun calendars

    try:
        # Retrieves a specific payrun calendar by using a unique payroll calendar ID
        api_response = await api_instance.get_pay_run_calendar(xero_tenant_id, payroll_calendar_id)
        print("The response of PayrollNzApi->get_pay_run_calendar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->get_pay_run_calendar: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payroll_calendar_id** | **str**| Identifier for the payrun calendars | 

### Return type

[**PayRunCalendarObject**](PayRunCalendarObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_slip**
> PaySlipObject get_pay_slip(xero_tenant_id, pay_slip_id)

Retrieves a specific payslip by a unique pay slip ID

### Example

```python
import time
import os
import xero_python
from xero_python.models.pay_slip_object import PaySlipObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    pay_slip_id = 'pay_slip_id_example' # str | Identifier for the payslip

    try:
        # Retrieves a specific payslip by a unique pay slip ID
        api_response = await api_instance.get_pay_slip(xero_tenant_id, pay_slip_id)
        print("The response of PayrollNzApi->get_pay_slip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->get_pay_slip: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_slip_id** | **str**| Identifier for the payslip | 

### Return type

[**PaySlipObject**](PaySlipObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_slips**
> PaySlips get_pay_slips(xero_tenant_id, pay_run_id, page=page)

Retrieves payslips

### Example

```python
import time
import os
import xero_python
from xero_python.models.pay_slips import PaySlips
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    pay_run_id = 'pay_run_id_example' # str | PayrunID which specifies the containing payrun of payslips to retrieve. By default, the API does not group payslips by payrun.
    page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)

    try:
        # Retrieves payslips
        api_response = await api_instance.get_pay_slips(xero_tenant_id, pay_run_id, page=page)
        print("The response of PayrollNzApi->get_pay_slips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->get_pay_slips: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_run_id** | **str**| PayrunID which specifies the containing payrun of payslips to retrieve. By default, the API does not group payslips by payrun. | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**PaySlips**](PaySlips.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statutory_deduction**
> StatutoryDeductionObject get_statutory_deduction(xero_tenant_id, id)

Retrieves a specific statutory deduction by using a unique statutory deductions id

### Example

```python
import time
import os
import xero_python
from xero_python.models.statutory_deduction_object import StatutoryDeductionObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    id = 'id_example' # str | Identifier for the statutory deduction

    try:
        # Retrieves a specific statutory deduction by using a unique statutory deductions id
        api_response = await api_instance.get_statutory_deduction(xero_tenant_id, id)
        print("The response of PayrollNzApi->get_statutory_deduction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->get_statutory_deduction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **id** | **str**| Identifier for the statutory deduction | 

### Return type

[**StatutoryDeductionObject**](StatutoryDeductionObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statutory_deductions**
> StatutoryDeductions get_statutory_deductions(xero_tenant_id, page=page)

Retrieves statutory deductions

### Example

```python
import time
import os
import xero_python
from xero_python.models.statutory_deductions import StatutoryDeductions
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)

    try:
        # Retrieves statutory deductions
        api_response = await api_instance.get_statutory_deductions(xero_tenant_id, page=page)
        print("The response of PayrollNzApi->get_statutory_deductions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->get_statutory_deductions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**StatutoryDeductions**](StatutoryDeductions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_superannuation**
> SuperannuationObject get_superannuation(xero_tenant_id, superannuation_id)

Retrieves a specific superannuation using a unique superannuation ID

### Example

```python
import time
import os
import xero_python
from xero_python.models.superannuation_object import SuperannuationObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    superannuation_id = 'superannuation_id_example' # str | Identifier for the superannuation

    try:
        # Retrieves a specific superannuation using a unique superannuation ID
        api_response = await api_instance.get_superannuation(xero_tenant_id, superannuation_id)
        print("The response of PayrollNzApi->get_superannuation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->get_superannuation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **superannuation_id** | **str**| Identifier for the superannuation | 

### Return type

[**SuperannuationObject**](SuperannuationObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_superannuations**
> Superannuations get_superannuations(xero_tenant_id, page=page)

Retrieves superannuations

### Example

```python
import time
import os
import xero_python
from xero_python.models.superannuations import Superannuations
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)

    try:
        # Retrieves superannuations
        api_response = await api_instance.get_superannuations(xero_tenant_id, page=page)
        print("The response of PayrollNzApi->get_superannuations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->get_superannuations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**Superannuations**](Superannuations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracking_categories**
> TrackingCategories get_tracking_categories(xero_tenant_id)

Retrieves tracking categories

### Example

```python
import time
import os
import xero_python
from xero_python.models.tracking_categories import TrackingCategories
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant

    try:
        # Retrieves tracking categories
        api_response = await api_instance.get_tracking_categories(xero_tenant_id)
        print("The response of PayrollNzApi->get_tracking_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->get_tracking_categories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_earnings_template**
> EarningsTemplateObject update_employee_earnings_template(xero_tenant_id, employee_id, pay_template_earning_id, earnings_template, idempotency_key=idempotency_key)

Updates an earnings template records for an employee

### Example

```python
import time
import os
import xero_python
from xero_python.models.earnings_template import EarningsTemplate
from xero_python.models.earnings_template_object import EarningsTemplateObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
    pay_template_earning_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Id for single pay template earnings object
    earnings_template = {ratePerUnit=25, numberOfUnits=4, earningsRateID=f9d8f5b5-9049-47f4-8541-35e200f750a5} # EarningsTemplate | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Updates an earnings template records for an employee
        api_response = await api_instance.update_employee_earnings_template(xero_tenant_id, employee_id, pay_template_earning_id, earnings_template, idempotency_key=idempotency_key)
        print("The response of PayrollNzApi->update_employee_earnings_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->update_employee_earnings_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | **str**| Employee id for single object | 
 **pay_template_earning_id** | **str**| Id for single pay template earnings object | 
 **earnings_template** | [**EarningsTemplate**](EarningsTemplate.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**EarningsTemplateObject**](EarningsTemplateObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pay_slip_line_items**
> PaySlipObject update_pay_slip_line_items(xero_tenant_id, pay_slip_id, body, idempotency_key=idempotency_key)

Creates an employee pay slip

### Example

```python
import time
import os
import xero_python
from xero_python.models.pay_slip import PaySlip
from xero_python.models.pay_slip_object import PaySlipObject
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.PayrollNzApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    pay_slip_id = 'pay_slip_id_example' # str | Identifier for the payslip
    body = {earningsLines=[{earningsLineID=f9d8f5b5-9049-47f4-8541-35e200f750a5, earningsRateID=f9d8f5b5-9049-47f4-8541-35e200f750a5, displayName=Ordinary Time, ratePerUnit=25, numberOfUnits=0, amount=0, isLinkedToTimesheet=false, isSystemGenerated=true}, {earningsLineID=65b83d94-f20f-45e1-85ae-387fcf460c26, earningsRateID=65b83d94-f20f-45e1-85ae-387fcf460c26, displayName=Salary, ratePerUnit=0, numberOfUnits=8, amount=0, isLinkedToTimesheet=false, isSystemGenerated=false}], leaveEarningsLines=[{earningsLineID=0441497f-5dc7-4cd3-a90d-f2e07e21b2a6, earningsRateID=39b3560a-5d2f-4538-924a-4349dc86396e, displayName=Holiday Pay, fixedAmount=268.8, amount=268.8, isLinkedToTimesheet=false, isSystemGenerated=true}], deductionLines=[{deductionTypeID=a3760fe4-68a4-4e38-8326-fe616af7dc74, amount=100}], leaveAccrualLines=[{leaveTypeID=0441497f-5dc7-4cd3-a90d-f2e07e21b2a6, numberOfUnits=268.8}, {leaveTypeID=b0b1b79e-2a25-46c2-ad08-ca25ef48d7e4, numberOfUnits=0}, {leaveTypeID=f2f994cf-1899-46f3-ad4f-5d92d78c3719, numberOfUnits=0}, {leaveTypeID=34129765-11cb-4d8c-b568-84a2219beda3, numberOfUnits=0}], superannuationLines=[{superannuationTypeID=563273ea-0dae-4f82-86a4-e0db77c008ea, displayName=KiwiSaver, amount=108.86, fixedAmount=3, percentage=3, manualAdjustment=false}], employeeTaxLines=[{taxLineID=1084146b-e890-489c-aed3-06de80f63d84, amount=1057.22, globalTaxTypeID=11, manualAdjustment=false}], employerTaxLines=[{taxLineID=6f9eb8cd-0f4a-440b-939c-bdb0f6ad694c, amount=18.9, globalTaxTypeID=10, manualAdjustment=false}], statutoryDeductionLines=[{statutoryDeductionTypeID=b5efd8d1-0c93-4a14-a314-b5cba4a4e6b3, amount=108.86}], grossEarningsHistory={daysPaid=3, unpaidWeeks=0}} # PaySlip | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates an employee pay slip
        api_response = await api_instance.update_pay_slip_line_items(xero_tenant_id, pay_slip_id, body, idempotency_key=idempotency_key)
        print("The response of PayrollNzApi->update_pay_slip_line_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollNzApi->update_pay_slip_line_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_slip_id** | **str**| Identifier for the payslip | 
 **body** | **PaySlip**|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**PaySlipObject**](PaySlipObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

