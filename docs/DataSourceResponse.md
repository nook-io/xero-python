# DataSourceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct_bank_feed** | **float** | Sum of the amounts of all statement lines where the source of the data was a direct bank feed in to Xero via an API integration.   This could be from a bank or aggregator.   This gives an indication on the certainty of correctness of the data. | [optional] 
**indirect_bank_feed** | **float** | No longer in use. | [optional] 
**file_upload** | **float** | Sum of the amounts of all statement lines where the source of the data was a file manually uploaded in to Xero.   This gives an indication on the certainty of correctness of the data. | [optional] 
**manual** | **float** | Sum of the amounts of all statement lines where the source of the data was manually input in to Xero.   This gives an indication on the certainty of correctness of the data. | [optional] 
**direct_bank_feed_pos** | **float** | Sum of the amounts of all statement lines where the source of the data was a direct bank feed in to Xero via an API integration.   This could be from a bank or aggregator.  This gives an indication on the certainty of correctness of the data.  Only positive transactions are included. | [optional] 
**indirect_bank_feed_pos** | **float** | No longer in use. | [optional] 
**file_upload_pos** | **float** | Sum of the amounts of all statement lines where the source of the data was a file manually uploaded in to Xero.   This gives an indication on the certainty of correctness of the data. Only positive transactions are included. | [optional] 
**manual_pos** | **float** | Sum of the amounts of all statement lines where the source of the data was manually input in to Xero.   This gives an indication on the certainty of correctness of the data. Only positive transactions are included. | [optional] 
**direct_bank_feed_neg** | **float** | Sum of the amounts of all statement lines where the source of the data was a direct bank feed in to Xero via an API integration.   This could be from a bank or aggregator.   This gives an indication on the certainty of correctness of the data.  Only negative transactions are included. | [optional] 
**indirect_bank_feed_neg** | **float** | No longer in use. | [optional] 
**file_upload_neg** | **float** | Sum of the amounts of all statement lines where the source of the data was a file manually uploaded in to Xero.   This gives an indication on the certainty of correctness of the data.  Only negative transactions are included. | [optional] 
**manual_neg** | **float** | Sum of the amounts of all statement lines where the source of the data was manually input in to Xero.   This gives an indication on the certainty of correctness of the data.  Only negative transactions are included. | [optional] 
**other_pos** | **float** | Sum of the amounts of all statement lines where the source of the data was unknown.   This gives an indication on the certainty of correctness of the data.  Only positive transactions are included. | [optional] 
**other_neg** | **float** | Sum of the amounts of all statement lines where the source of the data was unknown.   This gives an indication on the certainty of correctness of the data.  Only negative transactions are included. | [optional] 
**other** | **float** | Sum of the amounts of all statement lines where the source of the data was unknown.   This gives an indication on the certainty of correctness of the data. | [optional] 

## Example

```python
from xero_python.models.data_source_response import DataSourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceResponse from a JSON string
data_source_response_instance = DataSourceResponse.from_json(json)
# print the JSON string representation of the object
print DataSourceResponse.to_json()

# convert the object into a dict
data_source_response_dict = data_source_response_instance.to_dict()
# create an instance of DataSourceResponse from a dict
data_source_response_from_dict = DataSourceResponse.from_dict(data_source_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


