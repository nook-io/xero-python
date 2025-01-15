# HistoryRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str** | details | [optional] 
**changes** | **str** | Name of branding theme | [optional] 
**user** | **str** | has a value of 0 | [optional] 
**date_utc** | **str** | UTC timestamp of creation date of branding theme | [optional] [readonly] 

## Example

```python
from xero_python.models.history_record import HistoryRecord

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryRecord from a JSON string
history_record_instance = HistoryRecord.from_json(json)
# print the JSON string representation of the object
print HistoryRecord.to_json()

# convert the object into a dict
history_record_dict = history_record_instance.to_dict()
# create an instance of HistoryRecord from a dict
history_record_from_dict = HistoryRecord.from_dict(history_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


