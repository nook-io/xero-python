# EmployeeLeaveSetupObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**leave_setup** | [**EmployeeLeaveSetup**](EmployeeLeaveSetup.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_leave_setup_object import EmployeeLeaveSetupObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeLeaveSetupObject from a JSON string
employee_leave_setup_object_instance = EmployeeLeaveSetupObject.from_json(json)
# print the JSON string representation of the object
print EmployeeLeaveSetupObject.to_json()

# convert the object into a dict
employee_leave_setup_object_dict = employee_leave_setup_object_instance.to_dict()
# create an instance of EmployeeLeaveSetupObject from a dict
employee_leave_setup_object_from_dict = EmployeeLeaveSetupObject.from_dict(employee_leave_setup_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


