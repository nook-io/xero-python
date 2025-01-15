# LockHistoryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organisation_id** | **str** | The requested Organisation to which the data pertains | [optional] 
**end_date** | **date** | The end date of the report | [optional] 
**lock_dates** | [**List[LockHistoryModel]**](LockHistoryModel.md) |  | [optional] 

## Example

```python
from xero_python.models.lock_history_response import LockHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LockHistoryResponse from a JSON string
lock_history_response_instance = LockHistoryResponse.from_json(json)
# print the JSON string representation of the object
print LockHistoryResponse.to_json()

# convert the object into a dict
lock_history_response_dict = lock_history_response_instance.to_dict()
# create an instance of LockHistoryResponse from a dict
lock_history_response_from_dict = LockHistoryResponse.from_dict(lock_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


