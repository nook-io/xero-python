# UpdateUsageRecord

Data transfer object for public update usage end point

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The new quantity for the usage record. Must be a whole number that is greater than or equal to 0 | 

## Example

```python
from xero_python.models.update_usage_record import UpdateUsageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUsageRecord from a JSON string
update_usage_record_instance = UpdateUsageRecord.from_json(json)
# print the JSON string representation of the object
print UpdateUsageRecord.to_json()

# convert the object into a dict
update_usage_record_dict = update_usage_record_instance.to_dict()
# create an instance of UpdateUsageRecord from a dict
update_usage_record_from_dict = UpdateUsageRecord.from_dict(update_usage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


