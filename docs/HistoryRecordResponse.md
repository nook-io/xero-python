# HistoryRecordResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **str** | The type of change recorded against the document | [optional] 
**date_utc_string** | **str** | UTC date that the history record was created | [optional] 
**date_utc** | **datetime** | UTC date that the history record was created | [optional] 
**user** | **str** | The users first and last name | [optional] 
**details** | **str** | Description of the change event or transaction | [optional] 

## Example

```python
from xero_python.models.history_record_response import HistoryRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryRecordResponse from a JSON string
history_record_response_instance = HistoryRecordResponse.from_json(json)
# print the JSON string representation of the object
print HistoryRecordResponse.to_json()

# convert the object into a dict
history_record_response_dict = history_record_response_instance.to_dict()
# create an instance of HistoryRecordResponse from a dict
history_record_response_from_dict = HistoryRecordResponse.from_dict(history_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


