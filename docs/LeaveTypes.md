# LeaveTypes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**leave_types** | [**List[LeaveType1]**](LeaveType1.md) |  | [optional] 

## Example

```python
from xero_python.models.leave_types import LeaveTypes

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveTypes from a JSON string
leave_types_instance = LeaveTypes.from_json(json)
# print the JSON string representation of the object
print LeaveTypes.to_json()

# convert the object into a dict
leave_types_dict = leave_types_instance.to_dict()
# create an instance of LeaveTypes from a dict
leave_types_from_dict = LeaveTypes.from_dict(leave_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


