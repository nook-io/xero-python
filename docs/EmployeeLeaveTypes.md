# EmployeeLeaveTypes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**leave_types** | [**List[EmployeeLeaveType]**](EmployeeLeaveType.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_leave_types import EmployeeLeaveTypes

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeLeaveTypes from a JSON string
employee_leave_types_instance = EmployeeLeaveTypes.from_json(json)
# print the JSON string representation of the object
print EmployeeLeaveTypes.to_json()

# convert the object into a dict
employee_leave_types_dict = employee_leave_types_instance.to_dict()
# create an instance of EmployeeLeaveTypes from a dict
employee_leave_types_from_dict = EmployeeLeaveTypes.from_dict(employee_leave_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


