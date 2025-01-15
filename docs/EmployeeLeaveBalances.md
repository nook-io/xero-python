# EmployeeLeaveBalances


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**leave_balances** | [**List[EmployeeLeaveBalance]**](EmployeeLeaveBalance.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_leave_balances import EmployeeLeaveBalances

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeLeaveBalances from a JSON string
employee_leave_balances_instance = EmployeeLeaveBalances.from_json(json)
# print the JSON string representation of the object
print EmployeeLeaveBalances.to_json()

# convert the object into a dict
employee_leave_balances_dict = employee_leave_balances_instance.to_dict()
# create an instance of EmployeeLeaveBalances from a dict
employee_leave_balances_from_dict = EmployeeLeaveBalances.from_dict(employee_leave_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


