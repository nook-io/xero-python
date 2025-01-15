# EmployeeStatutoryLeaveBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leave_type** | **str** | The type of statutory leave | [optional] 
**balance_remaining** | **float** | The balance remaining for the corresponding leave type as of specified date. | [optional] 
**units** | **str** | The units will be \&quot;Hours\&quot; | [optional] 

## Example

```python
from xero_python.models.employee_statutory_leave_balance import EmployeeStatutoryLeaveBalance

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeStatutoryLeaveBalance from a JSON string
employee_statutory_leave_balance_instance = EmployeeStatutoryLeaveBalance.from_json(json)
# print the JSON string representation of the object
print EmployeeStatutoryLeaveBalance.to_json()

# convert the object into a dict
employee_statutory_leave_balance_dict = employee_statutory_leave_balance_instance.to_dict()
# create an instance of EmployeeStatutoryLeaveBalance from a dict
employee_statutory_leave_balance_from_dict = EmployeeStatutoryLeaveBalance.from_dict(employee_statutory_leave_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


