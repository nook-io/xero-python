# LeaveTypeObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**leave_type** | [**LeaveType1**](LeaveType1.md) |  | [optional] 

## Example

```python
from xero_python.models.leave_type_object import LeaveTypeObject

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveTypeObject from a JSON string
leave_type_object_instance = LeaveTypeObject.from_json(json)
# print the JSON string representation of the object
print LeaveTypeObject.to_json()

# convert the object into a dict
leave_type_object_dict = leave_type_object_instance.to_dict()
# create an instance of LeaveTypeObject from a dict
leave_type_object_from_dict = LeaveTypeObject.from_dict(leave_type_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


