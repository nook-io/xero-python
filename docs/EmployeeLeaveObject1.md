# EmployeeLeaveObject1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**leave** | [**EmployeeLeave1**](EmployeeLeave1.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_leave_object1 import EmployeeLeaveObject1

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeLeaveObject1 from a JSON string
employee_leave_object1_instance = EmployeeLeaveObject1.from_json(json)
# print the JSON string representation of the object
print EmployeeLeaveObject1.to_json()

# convert the object into a dict
employee_leave_object1_dict = employee_leave_object1_instance.to_dict()
# create an instance of EmployeeLeaveObject1 from a dict
employee_leave_object1_from_dict = EmployeeLeaveObject1.from_dict(employee_leave_object1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


