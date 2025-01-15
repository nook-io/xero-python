# xero_python.BankFeedsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_feed_connections**](BankFeedsApi.md#create_feed_connections) | **POST** /FeedConnections | Create one or more new feed connection
[**create_statements**](BankFeedsApi.md#create_statements) | **POST** /Statements | Creates one or more new statements
[**delete_feed_connections**](BankFeedsApi.md#delete_feed_connections) | **POST** /FeedConnections/DeleteRequests | Delete an existing feed connection
[**get_feed_connection**](BankFeedsApi.md#get_feed_connection) | **GET** /FeedConnections/{id} | Retrieve single feed connection based on a unique id provided
[**get_feed_connections**](BankFeedsApi.md#get_feed_connections) | **GET** /FeedConnections | Searches for feed connections
[**get_statement**](BankFeedsApi.md#get_statement) | **GET** /Statements/{statementId} | Retrieve single statement based on unique id provided
[**get_statements**](BankFeedsApi.md#get_statements) | **GET** /Statements | Retrieve all statements


# **create_feed_connections**
> FeedConnections create_feed_connections(xero_tenant_id, feed_connections, idempotency_key=idempotency_key)

Create one or more new feed connection

By passing in the FeedConnections array object in the body, you can create one or more new feed connections

### Example

```python
import time
import os
import xero_python
from xero_python.models.feed_connections import FeedConnections
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
    api_instance = xero_python.BankFeedsApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    feed_connections = {items=[{accountToken=foobar71760, accountNumber=123458637, accountName=SDK Bank 90861, accountType=BANK, currency=GBP}]} # FeedConnections | Feed Connection(s) array object in the body
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Create one or more new feed connection
        api_response = await api_instance.create_feed_connections(xero_tenant_id, feed_connections, idempotency_key=idempotency_key)
        print("The response of BankFeedsApi->create_feed_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankFeedsApi->create_feed_connections: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **feed_connections** | [**FeedConnections**](FeedConnections.md)| Feed Connection(s) array object in the body | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**FeedConnections**](FeedConnections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | success new feed connection(s)response |  -  |
**400** | failed to create new feed connection(s)response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_statements**
> Statements create_statements(xero_tenant_id, statements, idempotency_key=idempotency_key)

Creates one or more new statements

### Example

```python
import time
import os
import xero_python
from xero_python.models.statements import Statements
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
    api_instance = xero_python.BankFeedsApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    statements = {items=[{feedConnectionId=6a4b9ff5-3a5f-4321-936b-4796163550f6, startDate=2019-08-11, endDate=2019-08-11, startBalance={amount=100, creditDebitIndicator=CREDIT}, endBalance={amount=150, creditDebitIndicator=CREDIT}, statementLines=[{postedDate=2019-08-11, description=My new line, amount=50, creditDebitIndicator=CREDIT, transactionId=123446422, payeeName=StarLord90315, reference=Foobar95578, chequeNumber=12379009, transactionType=Refund}]}, {feedConnectionId=2ebe6393-f3bb-48ab-9a0e-b04fa8585a70, startDate=2019-08-11, endDate=2019-08-11, startBalance={amount=100, creditDebitIndicator=CREDIT}, endBalance={amount=150, creditDebitIndicator=CREDIT}, statementLines=[{postedDate=2019-08-11, description=My new line, amount=50, creditDebitIndicator=CREDIT, transactionId=123449402, payeeName=StarLord56705, reference=Foobar67355, chequeNumber=12379350, transactionType=Currency Conversion Fee}]}]} # Statements | Statements array of objects in the body
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates one or more new statements
        api_response = await api_instance.create_statements(xero_tenant_id, statements, idempotency_key=idempotency_key)
        print("The response of BankFeedsApi->create_statements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankFeedsApi->create_statements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **statements** | [**Statements**](Statements.md)| Statements array of objects in the body | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**Statements**](Statements.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success returns Statements array of objects in response |  -  |
**400** | Statement failed validation |  -  |
**403** | Invalid application or feed connection |  -  |
**409** | Duplicate statement received |  -  |
**413** | Statement exceeds size limit |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Intermittent Xero Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feed_connections**
> FeedConnections delete_feed_connections(xero_tenant_id, feed_connections, idempotency_key=idempotency_key)

Delete an existing feed connection

By passing in FeedConnections array object in the body, you can delete a feed connection.

### Example

```python
import time
import os
import xero_python
from xero_python.models.feed_connections import FeedConnections
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
    api_instance = xero_python.BankFeedsApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    feed_connections = {items=[{id=b4cc693b-24d9-42ec-a6d4-2943d253ff63}]} # FeedConnections | Feed Connections array object in the body
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Delete an existing feed connection
        api_response = await api_instance.delete_feed_connections(xero_tenant_id, feed_connections, idempotency_key=idempotency_key)
        print("The response of BankFeedsApi->delete_feed_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankFeedsApi->delete_feed_connections: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **feed_connections** | [**FeedConnections**](FeedConnections.md)| Feed Connections array object in the body | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**FeedConnections**](FeedConnections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success response for deleted feed connection |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feed_connection**
> FeedConnection get_feed_connection(xero_tenant_id, id)

Retrieve single feed connection based on a unique id provided

By passing in a FeedConnection Id options, you can search for matching feed connections

### Example

```python
import time
import os
import xero_python
from xero_python.models.feed_connection import FeedConnection
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
    api_instance = xero_python.BankFeedsApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    id = 'id_example' # str | Unique identifier for retrieving single object

    try:
        # Retrieve single feed connection based on a unique id provided
        api_response = await api_instance.get_feed_connection(xero_tenant_id, id)
        print("The response of BankFeedsApi->get_feed_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankFeedsApi->get_feed_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **id** | **str**| Unique identifier for retrieving single object | 

### Return type

[**FeedConnection**](FeedConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success returns a FeedConnection object matching the id in response |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feed_connections**
> FeedConnections get_feed_connections(xero_tenant_id, page=page, page_size=page_size)

Searches for feed connections

By passing in the appropriate options, you can search for available feed connections in the system.

### Example

```python
import time
import os
import xero_python
from xero_python.models.feed_connections import FeedConnections
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
    api_instance = xero_python.BankFeedsApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    page = 1 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 10. Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?page=1 to get the second set of the records. When page value is not a number or a negative number, by default, the first set of records is returned. (optional)
    page_size = 100 # int | Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?pageSize=100 to specify page size of 100. (optional)

    try:
        # Searches for feed connections
        api_response = await api_instance.get_feed_connections(xero_tenant_id, page=page, page_size=page_size)
        print("The response of BankFeedsApi->get_feed_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankFeedsApi->get_feed_connections: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 10. Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?page&#x3D;1 to get the second set of the records. When page value is not a number or a negative number, by default, the first set of records is returned. | [optional] 
 **page_size** | **int**| Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?pageSize&#x3D;100 to specify page size of 100. | [optional] 

### Return type

[**FeedConnections**](FeedConnections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | search results matching criteria returned with pagination and items array |  -  |
**400** | validation error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement**
> Statement get_statement(xero_tenant_id, statement_id)

Retrieve single statement based on unique id provided

By passing in a statement id, you can search for matching statements

### Example

```python
import time
import os
import xero_python
from xero_python.models.statement import Statement
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
    api_instance = xero_python.BankFeedsApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    statement_id = 'statement_id_example' # str | statement id for single object

    try:
        # Retrieve single statement based on unique id provided
        api_response = await api_instance.get_statement(xero_tenant_id, statement_id)
        print("The response of BankFeedsApi->get_statement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankFeedsApi->get_statement: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **statement_id** | **str**| statement id for single object | 

### Return type

[**Statement**](Statement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching id for single statement |  -  |
**404** | Statement not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statements**
> Statements get_statements(xero_tenant_id, page=page, page_size=page_size, xero_application_id=xero_application_id, xero_user_id=xero_user_id)

Retrieve all statements

By passing in parameters, you can search for matching statements

### Example

```python
import time
import os
import xero_python
from xero_python.models.statements import Statements
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
    api_instance = xero_python.BankFeedsApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    page = 56 # int | unique id for single object (optional)
    page_size = 56 # int | Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/Statements?pageSize=100 to specify page size of 100. (optional)
    xero_application_id = '00000000-0000-0000-0000-0000000010000' # str |  (optional) (default to '00000000-0000-0000-0000-0000000010000')
    xero_user_id = '00000000-0000-0000-0000-0000030000000' # str |  (optional) (default to '00000000-0000-0000-0000-0000030000000')

    try:
        # Retrieve all statements
        api_response = await api_instance.get_statements(xero_tenant_id, page=page, page_size=page_size, xero_application_id=xero_application_id, xero_user_id=xero_user_id)
        print("The response of BankFeedsApi->get_statements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankFeedsApi->get_statements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| unique id for single object | [optional] 
 **page_size** | **int**| Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/Statements?pageSize&#x3D;100 to specify page size of 100. | [optional] 
 **xero_application_id** | **str**|  | [optional] [default to &#39;00000000-0000-0000-0000-0000000010000&#39;]
 **xero_user_id** | **str**|  | [optional] [default to &#39;00000000-0000-0000-0000-0000030000000&#39;]

### Return type

[**Statements**](Statements.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success returns Statements array of objects response |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

