# xero_python.PayrollAuApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_leave_application**](PayrollAuApi.md#approve_leave_application) | **POST** /LeaveApplications/{LeaveApplicationID}/approve | Approve a requested leave application by a unique leave application id
[**create_leave_application**](PayrollAuApi.md#create_leave_application) | **POST** /LeaveApplications | Creates a leave application
[**create_pay_item**](PayrollAuApi.md#create_pay_item) | **POST** /PayItems | Creates a pay item
[**create_payroll_calendar**](PayrollAuApi.md#create_payroll_calendar) | **POST** /PayrollCalendars | Creates a Payroll Calendar
[**create_superfund**](PayrollAuApi.md#create_superfund) | **POST** /Superfunds | Creates a superfund
[**get_leave_application**](PayrollAuApi.md#get_leave_application) | **GET** /LeaveApplications/{LeaveApplicationID} | Retrieves a leave application by a unique leave application id
[**get_leave_applications**](PayrollAuApi.md#get_leave_applications) | **GET** /LeaveApplications | Retrieves leave applications
[**get_leave_applications_v2**](PayrollAuApi.md#get_leave_applications_v2) | **GET** /LeaveApplications/v2 | Retrieves leave applications including leave requests
[**get_pay_items**](PayrollAuApi.md#get_pay_items) | **GET** /PayItems | Retrieves pay items
[**get_payroll_calendar**](PayrollAuApi.md#get_payroll_calendar) | **GET** /PayrollCalendars/{PayrollCalendarID} | Retrieves payroll calendar by using a unique payroll calendar ID
[**get_payroll_calendars**](PayrollAuApi.md#get_payroll_calendars) | **GET** /PayrollCalendars | Retrieves payroll calendars
[**get_payslip**](PayrollAuApi.md#get_payslip) | **GET** /Payslip/{PayslipID} | Retrieves for a payslip by a unique payslip id
[**get_superfund**](PayrollAuApi.md#get_superfund) | **GET** /Superfunds/{SuperFundID} | Retrieves a superfund by using a unique superfund ID
[**get_superfund_products**](PayrollAuApi.md#get_superfund_products) | **GET** /SuperfundProducts | Retrieves superfund products
[**get_superfunds**](PayrollAuApi.md#get_superfunds) | **GET** /Superfunds | Retrieves superfunds
[**reject_leave_application**](PayrollAuApi.md#reject_leave_application) | **POST** /LeaveApplications/{LeaveApplicationID}/reject | Reject a leave application by a unique leave application id
[**update_leave_application**](PayrollAuApi.md#update_leave_application) | **POST** /LeaveApplications/{LeaveApplicationID} | Updates a specific leave application
[**update_payslip**](PayrollAuApi.md#update_payslip) | **POST** /Payslip/{PayslipID} | Updates a payslip
[**update_superfund**](PayrollAuApi.md#update_superfund) | **POST** /Superfunds/{SuperFundID} | Updates a superfund


# **approve_leave_application**
> LeaveApplications approve_leave_application(xero_tenant_id, leave_application_id, idempotency_key=idempotency_key)

Approve a requested leave application by a unique leave application id

### Example

```python
import time
import os
import xero_python
from xero_python.models.leave_applications import LeaveApplications
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    leave_application_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Leave Application id for single object
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Approve a requested leave application by a unique leave application id
        api_response = await api_instance.approve_leave_application(xero_tenant_id, leave_application_id, idempotency_key=idempotency_key)
        print("The response of PayrollAuApi->approve_leave_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->approve_leave_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_application_id** | **str**| Leave Application id for single object | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application successfully approved |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_leave_application**
> LeaveApplications create_leave_application(xero_tenant_id, leave_application, idempotency_key=idempotency_key)

Creates a leave application

### Example

```python
import time
import os
import xero_python
from xero_python.models.leave_application import LeaveApplication
from xero_python.models.leave_applications import LeaveApplications
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    leave_application = [ { "EmployeeID": "cdfb8371-0b21-4b8a-8903-1024df6c391e", "LeaveTypeID": "184ea8f7-d143-46dd-bef3-0c60e1aa6fca", "Title": "Hello World", "StartDate": "/Date(1572559200000+0000)/", "EndDate": "/Date(1572645600000+0000)/" } ] # List[LeaveApplication] | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates a leave application
        api_response = await api_instance.create_leave_application(xero_tenant_id, leave_application, idempotency_key=idempotency_key)
        print("The response of PayrollAuApi->create_leave_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->create_leave_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_application** | [**List[LeaveApplication]**](LeaveApplication.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful request |  -  |
**400** | invalid input, object invalid - TODO |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pay_item**
> PayItems create_pay_item(xero_tenant_id, pay_item, idempotency_key=idempotency_key)

Creates a pay item

### Example

```python
import time
import os
import xero_python
from xero_python.models.pay_item import PayItem
from xero_python.models.pay_items import PayItems
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    pay_item = {EarningsRates=[{Name=MyRate, AccountCode=400, TypeOfUnits=4.00, IsExemptFromTax=true, IsExemptFromSuper=true, IsReportableAsW1=false, AllowanceContributesToAnnualLeaveRate=false, AllowanceContributesToOvertimeRate=false, EarningsType=ORDINARYTIMEEARNINGS, EarningsRateID=1fa4e226-b711-46ba-a8a7-4344c9c5fb87, RateType=MULTIPLE, RatePerUnit=10.0, Multiplier=1.5, Amount=5, EmploymentTerminationPaymentType=O}]} # PayItem | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates a pay item
        api_response = await api_instance.create_pay_item(xero_tenant_id, pay_item, idempotency_key=idempotency_key)
        print("The response of PayrollAuApi->create_pay_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->create_pay_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_item** | [**PayItem**](PayItem.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**PayItems**](PayItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful request - currently returns empty array for JSON |  -  |
**400** | invalid input, object invalid - TODO |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payroll_calendar**
> PayrollCalendars create_payroll_calendar(xero_tenant_id, payroll_calendar, idempotency_key=idempotency_key)

Creates a Payroll Calendar

### Example

```python
import time
import os
import xero_python
from xero_python.models.payroll_calendar import PayrollCalendar
from xero_python.models.payroll_calendars import PayrollCalendars
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    payroll_calendar = [ { "PayrollCalendarID":"78bb86b9-e1ea-47ac-b75d-f087a81931de", "PayRunPeriodStartDate":"/Date(1572566400000+0000)/", "PayRunPeriodEndDate":"/Date(1573084800000+0000)/", "PayRunStatus":"DRAFT", "PaymentDate":"/Date(1573171200000+0000)/" } ] # List[PayrollCalendar] | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates a Payroll Calendar
        api_response = await api_instance.create_payroll_calendar(xero_tenant_id, payroll_calendar, idempotency_key=idempotency_key)
        print("The response of PayrollAuApi->create_payroll_calendar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->create_payroll_calendar: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payroll_calendar** | [**List[PayrollCalendar]**](PayrollCalendar.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful request |  -  |
**400** | invalid input, object invalid - TODO |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_superfund**
> SuperFunds create_superfund(xero_tenant_id, super_fund, idempotency_key=idempotency_key)

Creates a superfund

### Example

```python
import time
import os
import xero_python
from xero_python.models.super_fund import SuperFund
from xero_python.models.super_funds import SuperFunds
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    super_fund = [ { "usi":"PTC0133AU", "Type":"REGULATED", "Name":"Bar99359", "AccountNumber":"FB36350", "AccountName":"Foo38428", "USI":"PTC0133AU" } ] # List[SuperFund] | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates a superfund
        api_response = await api_instance.create_superfund(xero_tenant_id, super_fund, idempotency_key=idempotency_key)
        print("The response of PayrollAuApi->create_superfund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->create_superfund: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **super_fund** | [**List[SuperFund]**](SuperFund.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful request |  -  |
**400** | invalid input, object invalid - TODO |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leave_application**
> LeaveApplications get_leave_application(xero_tenant_id, leave_application_id)

Retrieves a leave application by a unique leave application id

### Example

```python
import time
import os
import xero_python
from xero_python.models.leave_applications import LeaveApplications
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    leave_application_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Leave Application id for single object

    try:
        # Retrieves a leave application by a unique leave application id
        api_response = await api_instance.get_leave_application(xero_tenant_id, leave_application_id)
        print("The response of PayrollAuApi->get_leave_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->get_leave_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_application_id** | **str**| Leave Application id for single object | 

### Return type

[**LeaveApplications**](LeaveApplications.md)

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

# **get_leave_applications**
> LeaveApplications get_leave_applications(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves leave applications

### Example

```python
import time
import os
import xero_python
from xero_python.models.leave_applications import LeaveApplications
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
    where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
    order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
    page = 56 # int | e.g. page=1 – Up to 100 objects will be returned in a single API call (optional)

    try:
        # Retrieves leave applications
        api_response = await api_instance.get_leave_applications(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
        print("The response of PayrollAuApi->get_leave_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->get_leave_applications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leave_applications_v2**
> LeaveApplications get_leave_applications_v2(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves leave applications including leave requests

### Example

```python
import time
import os
import xero_python
from xero_python.models.leave_applications import LeaveApplications
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
    where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
    order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
    page = 56 # int | e.g. page=1 – Up to 100 objects will be returned in a single API call (optional)

    try:
        # Retrieves leave applications including leave requests
        api_response = await api_instance.get_leave_applications_v2(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
        print("The response of PayrollAuApi->get_leave_applications_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->get_leave_applications_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_items**
> PayItems get_pay_items(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves pay items

### Example

```python
import time
import os
import xero_python
from xero_python.models.pay_items import PayItems
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
    where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
    order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
    page = 56 # int | e.g. page=1 – Up to 100 objects will be returned in a single API call (optional)

    try:
        # Retrieves pay items
        api_response = await api_instance.get_pay_items(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
        print("The response of PayrollAuApi->get_pay_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->get_pay_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] 

### Return type

[**PayItems**](PayItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payroll_calendar**
> PayrollCalendars get_payroll_calendar(xero_tenant_id, payroll_calendar_id)

Retrieves payroll calendar by using a unique payroll calendar ID

### Example

```python
import time
import os
import xero_python
from xero_python.models.payroll_calendars import PayrollCalendars
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    payroll_calendar_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Payroll Calendar id for single object

    try:
        # Retrieves payroll calendar by using a unique payroll calendar ID
        api_response = await api_instance.get_payroll_calendar(xero_tenant_id, payroll_calendar_id)
        print("The response of PayrollAuApi->get_payroll_calendar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->get_payroll_calendar: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payroll_calendar_id** | **str**| Payroll Calendar id for single object | 

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payroll_calendars**
> PayrollCalendars get_payroll_calendars(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves payroll calendars

### Example

```python
import time
import os
import xero_python
from xero_python.models.payroll_calendars import PayrollCalendars
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
    where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
    order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
    page = 56 # int | e.g. page=1 – Up to 100 objects will be returned in a single API call (optional)

    try:
        # Retrieves payroll calendars
        api_response = await api_instance.get_payroll_calendars(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
        print("The response of PayrollAuApi->get_payroll_calendars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->get_payroll_calendars: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] 

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payslip**
> PayslipObject get_payslip(xero_tenant_id, payslip_id)

Retrieves for a payslip by a unique payslip id

### Example

```python
import time
import os
import xero_python
from xero_python.models.payslip_object import PayslipObject
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    payslip_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Payslip id for single object

    try:
        # Retrieves for a payslip by a unique payslip id
        api_response = await api_instance.get_payslip(xero_tenant_id, payslip_id)
        print("The response of PayrollAuApi->get_payslip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->get_payslip: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payslip_id** | **str**| Payslip id for single object | 

### Return type

[**PayslipObject**](PayslipObject.md)

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

# **get_superfund**
> SuperFunds get_superfund(xero_tenant_id, super_fund_id)

Retrieves a superfund by using a unique superfund ID

### Example

```python
import time
import os
import xero_python
from xero_python.models.super_funds import SuperFunds
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    super_fund_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Superfund id for single object

    try:
        # Retrieves a superfund by using a unique superfund ID
        api_response = await api_instance.get_superfund(xero_tenant_id, super_fund_id)
        print("The response of PayrollAuApi->get_superfund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->get_superfund: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **super_fund_id** | **str**| Superfund id for single object | 

### Return type

[**SuperFunds**](SuperFunds.md)

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

# **get_superfund_products**
> SuperFundProducts get_superfund_products(xero_tenant_id, abn=abn, usi=usi)

Retrieves superfund products

### Example

```python
import time
import os
import xero_python
from xero_python.models.super_fund_products import SuperFundProducts
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    abn = '40022701955' # str | The ABN of the Regulated SuperFund (optional)
    usi = 'OSF0001AU' # str | The USI of the Regulated SuperFund (optional)

    try:
        # Retrieves superfund products
        api_response = await api_instance.get_superfund_products(xero_tenant_id, abn=abn, usi=usi)
        print("The response of PayrollAuApi->get_superfund_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->get_superfund_products: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **abn** | **str**| The ABN of the Regulated SuperFund | [optional] 
 **usi** | **str**| The USI of the Regulated SuperFund | [optional] 

### Return type

[**SuperFundProducts**](SuperFundProducts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_superfunds**
> SuperFunds get_superfunds(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves superfunds

### Example

```python
import time
import os
import xero_python
from xero_python.models.super_funds import SuperFunds
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
    where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
    order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
    page = 56 # int | e.g. page=1 – Up to 100 SuperFunds will be returned in a single API call (optional)

    try:
        # Retrieves superfunds
        api_response = await api_instance.get_superfunds(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
        print("The response of PayrollAuApi->get_superfunds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->get_superfunds: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 SuperFunds will be returned in a single API call | [optional] 

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_leave_application**
> LeaveApplications reject_leave_application(xero_tenant_id, leave_application_id, idempotency_key=idempotency_key)

Reject a leave application by a unique leave application id

### Example

```python
import time
import os
import xero_python
from xero_python.models.leave_applications import LeaveApplications
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    leave_application_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Leave Application id for single object
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Reject a leave application by a unique leave application id
        api_response = await api_instance.reject_leave_application(xero_tenant_id, leave_application_id, idempotency_key=idempotency_key)
        print("The response of PayrollAuApi->reject_leave_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->reject_leave_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_application_id** | **str**| Leave Application id for single object | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application successfully rejected |  -  |
**400** | validation error for a bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_leave_application**
> LeaveApplications update_leave_application(xero_tenant_id, leave_application_id, leave_application, idempotency_key=idempotency_key)

Updates a specific leave application

### Example

```python
import time
import os
import xero_python
from xero_python.models.leave_application import LeaveApplication
from xero_python.models.leave_applications import LeaveApplications
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    leave_application_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Leave Application id for single object
    leave_application = [ { "EmployeeID": "cdfb8371-0b21-4b8a-8903-1024df6c391e", "LeaveApplicationID": "1d4cd583-0107-4386-936b-672eb3d1f624", "LeaveTypeID": "184ea8f7-d143-46dd-bef3-0c60e1aa6fca", "LeavePeriods": [ { "PayPeriodStartDate": "/Date(1572566400000+0000)/", "PayPeriodEndDate": "/Date(1573084800000+0000)/", "LeavePeriodStatus": "SCHEDULED", "NumberOfUnits": 7.6 } ], "Title": "vacation", "Description": "My updated Description", "StartDate": "/Date(1572559200000+0000)/", "EndDate": "/Date(1572645600000+0000)/", "PayOutType": "DEFAULT" } ] # List[LeaveApplication] | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Updates a specific leave application
        api_response = await api_instance.update_leave_application(xero_tenant_id, leave_application_id, leave_application, idempotency_key=idempotency_key)
        print("The response of PayrollAuApi->update_leave_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->update_leave_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_application_id** | **str**| Leave Application id for single object | 
 **leave_application** | [**List[LeaveApplication]**](LeaveApplication.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful request |  -  |
**400** | invalid input, object invalid - TODO |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payslip**
> Payslips update_payslip(xero_tenant_id, payslip_id, payslip_lines, idempotency_key=idempotency_key)

Updates a payslip

Update lines on a single payslips

### Example

```python
import time
import os
import xero_python
from xero_python.models.payslip_lines import PayslipLines
from xero_python.models.payslips import Payslips
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    payslip_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Payslip id for single object
    payslip_lines = {Payslip={EmployeeID=cdfb8371-0b21-4b8a-8903-1024df6c391e, DeductionLines=[{DeductionTypeID=727af5e8-b347-4ae7-85fc-9b82266d0aec, CalculationType=FIXEDAMOUNT, NumberOfUnits=10}]}} # List[PayslipLines] | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Updates a payslip
        api_response = await api_instance.update_payslip(xero_tenant_id, payslip_id, payslip_lines, idempotency_key=idempotency_key)
        print("The response of PayrollAuApi->update_payslip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->update_payslip: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payslip_id** | **str**| Payslip id for single object | 
 **payslip_lines** | [**List[PayslipLines]**](PayslipLines.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**Payslips**](Payslips.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful request - currently returns empty array for JSON |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_superfund**
> SuperFunds update_superfund(xero_tenant_id, super_fund_id, super_fund, idempotency_key=idempotency_key)

Updates a superfund

Update properties on a single Superfund

### Example

```python
import time
import os
import xero_python
from xero_python.models.super_fund import SuperFund
from xero_python.models.super_funds import SuperFunds
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
    api_instance = xero_python.PayrollAuApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    super_fund_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Superfund id for single object
    super_fund =  [ { "Type":"REGULATED", "Name":"Nice23534" } ] # List[SuperFund] | 
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Updates a superfund
        api_response = await api_instance.update_superfund(xero_tenant_id, super_fund_id, super_fund, idempotency_key=idempotency_key)
        print("The response of PayrollAuApi->update_superfund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollAuApi->update_superfund: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **super_fund_id** | **str**| Superfund id for single object | 
 **super_fund** | [**List[SuperFund]**](SuperFund.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

