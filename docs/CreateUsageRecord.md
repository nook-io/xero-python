# CreateUsageRecord

Data transfer object for public create usage end point

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The initial quantity for the usage record. Must be a whole number that is greater than or equal to 0 | 
**timestamp** | **datetime** | DateTime in UTC of when the the product was consumed/used | 

## Example

```python
from xero_python.models.create_usage_record import CreateUsageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUsageRecord from a JSON string
create_usage_record_instance = CreateUsageRecord.from_json(json)
# print the JSON string representation of the object
print CreateUsageRecord.to_json()

# convert the object into a dict
create_usage_record_dict = create_usage_record_instance.to_dict()
# create an instance of CreateUsageRecord from a dict
create_usage_record_from_dict = CreateUsageRecord.from_dict(create_usage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


