# HistoryRecords


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**history_records** | [**List[HistoryRecord]**](HistoryRecord.md) |  | [optional] 

## Example

```python
from xero_python.models.history_records import HistoryRecords

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryRecords from a JSON string
history_records_instance = HistoryRecords.from_json(json)
# print the JSON string representation of the object
print HistoryRecords.to_json()

# convert the object into a dict
history_records_dict = history_records_instance.to_dict()
# create an instance of HistoryRecords from a dict
history_records_from_dict = HistoryRecords.from_dict(history_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


