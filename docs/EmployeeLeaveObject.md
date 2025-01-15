# EmployeeLeaveObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**leave** | [**EmployeeLeave**](EmployeeLeave.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_leave_object import EmployeeLeaveObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeLeaveObject from a JSON string
employee_leave_object_instance = EmployeeLeaveObject.from_json(json)
# print the JSON string representation of the object
print EmployeeLeaveObject.to_json()

# convert the object into a dict
employee_leave_object_dict = employee_leave_object_instance.to_dict()
# create an instance of EmployeeLeaveObject from a dict
employee_leave_object_from_dict = EmployeeLeaveObject.from_dict(employee_leave_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


