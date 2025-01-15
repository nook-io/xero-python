# LeavePeriods


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**periods** | [**List[LeavePeriod2]**](LeavePeriod2.md) |  | [optional] 

## Example

```python
from xero_python.models.leave_periods import LeavePeriods

# TODO update the JSON string below
json = "{}"
# create an instance of LeavePeriods from a JSON string
leave_periods_instance = LeavePeriods.from_json(json)
# print the JSON string representation of the object
print LeavePeriods.to_json()

# convert the object into a dict
leave_periods_dict = leave_periods_instance.to_dict()
# create an instance of LeavePeriods from a dict
leave_periods_from_dict = LeavePeriods.from_dict(leave_periods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


