# EmployeeLeaveBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the leave type. | [optional] 
**leave_type_id** | **str** | The Xero identifier for leave type | [optional] 
**balance** | **float** | The employees current balance for the corresponding leave type. | [optional] 
**type_of_units** | **str** | The type of the units of the leave. | [optional] 

## Example

```python
from xero_python.models.employee_leave_balance import EmployeeLeaveBalance

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeLeaveBalance from a JSON string
employee_leave_balance_instance = EmployeeLeaveBalance.from_json(json)
# print the JSON string representation of the object
print EmployeeLeaveBalance.to_json()

# convert the object into a dict
employee_leave_balance_dict = employee_leave_balance_instance.to_dict()
# create an instance of EmployeeLeaveBalance from a dict
employee_leave_balance_from_dict = EmployeeLeaveBalance.from_dict(employee_leave_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


