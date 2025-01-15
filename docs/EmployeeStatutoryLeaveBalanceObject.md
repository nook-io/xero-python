# EmployeeStatutoryLeaveBalanceObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**leave_balance** | [**EmployeeStatutoryLeaveBalance**](EmployeeStatutoryLeaveBalance.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_statutory_leave_balance_object import EmployeeStatutoryLeaveBalanceObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeStatutoryLeaveBalanceObject from a JSON string
employee_statutory_leave_balance_object_instance = EmployeeStatutoryLeaveBalanceObject.from_json(json)
# print the JSON string representation of the object
print EmployeeStatutoryLeaveBalanceObject.to_json()

# convert the object into a dict
employee_statutory_leave_balance_object_dict = employee_statutory_leave_balance_object_instance.to_dict()
# create an instance of EmployeeStatutoryLeaveBalanceObject from a dict
employee_statutory_leave_balance_object_from_dict = EmployeeStatutoryLeaveBalanceObject.from_dict(employee_statutory_leave_balance_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


