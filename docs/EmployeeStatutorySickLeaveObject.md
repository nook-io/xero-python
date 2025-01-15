# EmployeeStatutorySickLeaveObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**statutory_sick_leave** | [**EmployeeStatutorySickLeave**](EmployeeStatutorySickLeave.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_statutory_sick_leave_object import EmployeeStatutorySickLeaveObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeStatutorySickLeaveObject from a JSON string
employee_statutory_sick_leave_object_instance = EmployeeStatutorySickLeaveObject.from_json(json)
# print the JSON string representation of the object
print EmployeeStatutorySickLeaveObject.to_json()

# convert the object into a dict
employee_statutory_sick_leave_object_dict = employee_statutory_sick_leave_object_instance.to_dict()
# create an instance of EmployeeStatutorySickLeaveObject from a dict
employee_statutory_sick_leave_object_from_dict = EmployeeStatutorySickLeaveObject.from_dict(employee_statutory_sick_leave_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


