# xero_python.AppStoreApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subscription**](AppStoreApi.md#get_subscription) | **GET** /subscriptions/{subscriptionId} | Retrieves a subscription for a given subscriptionId
[**get_usage_records**](AppStoreApi.md#get_usage_records) | **GET** /subscriptions/{subscriptionId}/usage-records | Gets all usage records related to the subscription
[**post_usage_records**](AppStoreApi.md#post_usage_records) | **POST** /subscriptions/{subscriptionId}/items/{subscriptionItemId}/usage-records | Send metered usage belonging to this subscription and subscription item
[**put_usage_records**](AppStoreApi.md#put_usage_records) | **PUT** /subscriptions/{subscriptionId}/items/{subscriptionItemId}/usage-records/{usageRecordId} | Update and existing metered usage belonging to this subscription and subscription item


# **get_subscription**
> Subscription get_subscription(subscription_id)

Retrieves a subscription for a given subscriptionId

### Example

```python
import time
import os
import xero_python
from xero_python.models.subscription import Subscription
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
    api_instance = xero_python.AppStoreApi(api_client)
    subscription_id = '00000000-0000-0000-0000-000000000000' # str | Unique identifier for Subscription object

    try:
        # Retrieves a subscription for a given subscriptionId
        api_response = await api_instance.get_subscription(subscription_id)
        print("The response of AppStoreApi->get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppStoreApi->get_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Unique identifier for Subscription object | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of unique Subscription object |  -  |
**404** | When a failure occurs in the endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_records**
> UsageRecordsList get_usage_records(subscription_id)

Gets all usage records related to the subscription

### Example

```python
import time
import os
import xero_python
from xero_python.models.usage_records_list import UsageRecordsList
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
    api_instance = xero_python.AppStoreApi(api_client)
    subscription_id = '00000000-0000-0000-0000-000000000000' # str | Unique identifier for Subscription object

    try:
        # Gets all usage records related to the subscription
        api_response = await api_instance.get_usage_records(subscription_id)
        print("The response of AppStoreApi->get_usage_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppStoreApi->get_usage_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Unique identifier for Subscription object | 

### Return type

[**UsageRecordsList**](UsageRecordsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return a list of all usage record submitted against this subscription for this subscription period |  -  |
**404** | When a failure occurs in the endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_usage_records**
> UsageRecord post_usage_records(subscription_id, subscription_item_id, create_usage_record, idempotency_key=idempotency_key)

Send metered usage belonging to this subscription and subscription item

### Example

```python
import time
import os
import xero_python
from xero_python.models.create_usage_record import CreateUsageRecord
from xero_python.models.usage_record import UsageRecord
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
    api_instance = xero_python.AppStoreApi(api_client)
    subscription_id = '00000000-0000-0000-0000-000000000000' # str | Unique identifier for Subscription object
    subscription_item_id = '00000000-0000-0000-0000-000000000000' # str | The unique identifier of the subscriptionItem
    create_usage_record = {timestamp=2022-01-21T13:01:00, quantity=10} # CreateUsageRecord | Contains the quantity for the usage record to create
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Send metered usage belonging to this subscription and subscription item
        api_response = await api_instance.post_usage_records(subscription_id, subscription_item_id, create_usage_record, idempotency_key=idempotency_key)
        print("The response of AppStoreApi->post_usage_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppStoreApi->post_usage_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Unique identifier for Subscription object | 
 **subscription_item_id** | **str**| The unique identifier of the subscriptionItem | 
 **create_usage_record** | [**CreateUsageRecord**](CreateUsageRecord.md)| Contains the quantity for the usage record to create | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**UsageRecord**](UsageRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of the record submitted |  -  |
**404** | When a failure occurs in the endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_usage_records**
> UsageRecord put_usage_records(subscription_id, subscription_item_id, usage_record_id, update_usage_record, idempotency_key=idempotency_key)

Update and existing metered usage belonging to this subscription and subscription item

### Example

```python
import time
import os
import xero_python
from xero_python.models.update_usage_record import UpdateUsageRecord
from xero_python.models.usage_record import UsageRecord
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
    api_instance = xero_python.AppStoreApi(api_client)
    subscription_id = '00000000-0000-0000-0000-000000000000' # str | Unique identifier for Subscription object
    subscription_item_id = '00000000-0000-0000-0000-000000000000' # str | The unique identifier of the subscriptionItem
    usage_record_id = '00000000-0000-0000-0000-000000000000' # str | The unique identifier of the usage record
    update_usage_record = {quantity=10} # UpdateUsageRecord | Contains the quantity for the usage record to update
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Update and existing metered usage belonging to this subscription and subscription item
        api_response = await api_instance.put_usage_records(subscription_id, subscription_item_id, usage_record_id, update_usage_record, idempotency_key=idempotency_key)
        print("The response of AppStoreApi->put_usage_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppStoreApi->put_usage_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Unique identifier for Subscription object | 
 **subscription_item_id** | **str**| The unique identifier of the subscriptionItem | 
 **usage_record_id** | **str**| The unique identifier of the usage record | 
 **update_usage_record** | [**UpdateUsageRecord**](UpdateUsageRecord.md)| Contains the quantity for the usage record to update | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**UsageRecord**](UsageRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of the modified record |  -  |
**404** | When a failure occurs in the endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

