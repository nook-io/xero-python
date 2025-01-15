# xero_python.IdentityApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_connection**](IdentityApi.md#delete_connection) | **DELETE** /Connections/{id} | Deletes a connection for this user (i.e. disconnect a tenant)
[**get_connections**](IdentityApi.md#get_connections) | **GET** /Connections | Retrieves the connections for this user


# **delete_connection**
> delete_connection(id)

Deletes a connection for this user (i.e. disconnect a tenant)

Override the base server url that include version

### Example

```python
import time
import os
import xero_python
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
    api_instance = xero_python.IdentityApi(api_client)
    id = 'id_example' # str | Unique identifier for retrieving single object

    try:
        # Deletes a connection for this user (i.e. disconnect a tenant)
        await api_instance.delete_connection(id)
    except Exception as e:
        print("Exception when calling IdentityApi->delete_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for retrieving single object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success - connection has been deleted no content returned |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections**
> List[Connection] get_connections(auth_event_id=auth_event_id)

Retrieves the connections for this user

Override the base server url that include version

### Example

```python
import time
import os
import xero_python
from xero_python.models.connection import Connection
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
    api_instance = xero_python.IdentityApi(api_client)
    auth_event_id = '00000000-0000-0000-0000-000000000000' # str | Filter by authEventId (optional)

    try:
        # Retrieves the connections for this user
        api_response = await api_instance.get_connections(auth_event_id=auth_event_id)
        print("The response of IdentityApi->get_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->get_connections: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_event_id** | **str**| Filter by authEventId | [optional] 

### Return type

[**List[Connection]**](Connection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Connections array with 0 to n Connection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

