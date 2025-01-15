# UsageRecordsList

Response to get usage record

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_records** | [**List[UsageRecord]**](UsageRecord.md) | A collection of usage records | 

## Example

```python
from xero_python.models.usage_records_list import UsageRecordsList

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRecordsList from a JSON string
usage_records_list_instance = UsageRecordsList.from_json(json)
# print the JSON string representation of the object
print UsageRecordsList.to_json()

# convert the object into a dict
usage_records_list_dict = usage_records_list_instance.to_dict()
# create an instance of UsageRecordsList from a dict
usage_records_list_from_dict = UsageRecordsList.from_dict(usage_records_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


