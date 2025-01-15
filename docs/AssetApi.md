# xero_python.AssetApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset**](AssetApi.md#create_asset) | **POST** /Assets | adds a fixed asset
[**create_asset_type**](AssetApi.md#create_asset_type) | **POST** /AssetTypes | adds a fixed asset type
[**get_asset_by_id**](AssetApi.md#get_asset_by_id) | **GET** /Assets/{id} | Retrieves fixed asset by id
[**get_asset_types**](AssetApi.md#get_asset_types) | **GET** /AssetTypes | searches fixed asset types
[**get_assets**](AssetApi.md#get_assets) | **GET** /Assets | searches fixed asset


# **create_asset**
> Asset create_asset(xero_tenant_id, asset, idempotency_key=idempotency_key)

adds a fixed asset

Adds an asset to the system

### Example

```python
import time
import os
import xero_python
from xero_python.models.asset import Asset
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
    api_instance = xero_python.AssetApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    asset = {assetName=Computer74863, assetNumber=123477544, purchaseDate=2020-01-01, purchasePrice=100.0, disposalPrice=23.23, assetStatus=Draft, bookDepreciationSetting={depreciationMethod=StraightLine, averagingMethod=ActualDays, depreciationRate=0.5, depreciationCalculationMethod=None}, bookDepreciationDetail={currentCapitalGain=5.32, currentGainLoss=3.88, depreciationStartDate=2020-01-02, costLimit=100.0, currentAccumDepreciationAmount=2.25}, AccountingBookValue=99.5} # Asset | Fixed asset you are creating
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # adds a fixed asset
        api_response = await api_instance.create_asset(xero_tenant_id, asset, idempotency_key=idempotency_key)
        print("The response of AssetApi->create_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->create_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **asset** | [**Asset**](Asset.md)| Fixed asset you are creating | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | return single object - create new asset |  -  |
**400** | invalid input, object invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_type**
> AssetType create_asset_type(xero_tenant_id, asset_type, idempotency_key=idempotency_key)

adds a fixed asset type

Adds an fixed asset type to the system

### Example

```python
import time
import os
import xero_python
from xero_python.models.asset_type import AssetType
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
    api_instance = xero_python.AssetApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    asset_type = {assetTypeName=Machinery11004, fixedAssetAccountId=3d8d063a-c148-4bb8-8b3c-a5e2ad3b1e82, depreciationExpenseAccountId=d1602f69-f900-4616-8d34-90af393fa368, accumulatedDepreciationAccountId=9195cadd-8645-41e6-9f67-7bcd421defe8, bookDepreciationSetting={depreciationMethod=DiminishingValue100, averagingMethod=ActualDays, depreciationRate=0.05, depreciationCalculationMethod=None}} # AssetType | Asset type to add
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # adds a fixed asset type
        api_response = await api_instance.create_asset_type(xero_tenant_id, asset_type, idempotency_key=idempotency_key)
        print("The response of AssetApi->create_asset_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->create_asset_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **asset_type** | [**AssetType**](AssetType.md)| Asset type to add | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**AssetType**](AssetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results single object -  created fixed type |  -  |
**400** | invalid input, object invalid |  -  |
**409** | a type already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_id**
> Asset get_asset_by_id(xero_tenant_id, id)

Retrieves fixed asset by id

By passing in the appropriate asset id, you can search for a specific fixed asset in the system 

### Example

```python
import time
import os
import xero_python
from xero_python.models.asset import Asset
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
    api_instance = xero_python.AssetApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    id = '00000000-0000-0000-0000-000000000000' # str | fixed asset id for single object

    try:
        # Retrieves fixed asset by id
        api_response = await api_instance.get_asset_by_id(xero_tenant_id, id)
        print("The response of AssetApi->get_asset_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **id** | **str**| fixed asset id for single object | 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_types**
> List[AssetType] get_asset_types(xero_tenant_id)

searches fixed asset types

By passing in the appropriate options, you can search for available fixed asset types in the system

### Example

```python
import time
import os
import xero_python
from xero_python.models.asset_type import AssetType
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
    api_instance = xero_python.AssetApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant

    try:
        # searches fixed asset types
        api_response = await api_instance.get_asset_types(xero_tenant_id)
        print("The response of AssetApi->get_asset_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**List[AssetType]**](AssetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets**
> Assets get_assets(xero_tenant_id, status, page=page, page_size=page_size, order_by=order_by, sort_direction=sort_direction, filter_by=filter_by)

searches fixed asset

By passing in the appropriate options, you can search for available fixed asset in the system

### Example

```python
import time
import os
import xero_python
from xero_python.models.asset_status_query_param import AssetStatusQueryParam
from xero_python.models.assets import Assets
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
    api_instance = xero_python.AssetApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    status = xero_python.AssetStatusQueryParam() # AssetStatusQueryParam | Required when retrieving a collection of assets. See Asset Status Codes
    page = 1 # int | Results are paged. This specifies which page of the results to return. The default page is 1. (optional)
    page_size = 5 # int | The number of records returned per page. By default the number of records returned is 10. (optional)
    order_by = 'AssetName' # str | Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice. (optional)
    sort_direction = 'ASC' # str | ASC or DESC (optional)
    filter_by = 'Company Car' # str | A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields. (optional)

    try:
        # searches fixed asset
        api_response = await api_instance.get_assets(xero_tenant_id, status, page=page, page_size=page_size, order_by=order_by, sort_direction=sort_direction, filter_by=filter_by)
        print("The response of AssetApi->get_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_assets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **status** | [**AssetStatusQueryParam**](.md)| Required when retrieving a collection of assets. See Asset Status Codes | 
 **page** | **int**| Results are paged. This specifies which page of the results to return. The default page is 1. | [optional] 
 **page_size** | **int**| The number of records returned per page. By default the number of records returned is 10. | [optional] 
 **order_by** | **str**| Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice. | [optional] 
 **sort_direction** | **str**| ASC or DESC | [optional] 
 **filter_by** | **str**| A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields. | [optional] 

### Return type

[**Assets**](Assets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results matching criteria |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

