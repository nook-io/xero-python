# EmployeeLeaveType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leave_type_id** | **str** | The Xero identifier for leave type | 
**schedule_of_accrual** | **str** | The schedule of accrual | 
**hours_accrued_annually** | **float** | The number of hours accrued for the leave annually. This is 0 when the scheduleOfAccrual chosen is \&quot;OnHourWorked\&quot; | [optional] 
**maximum_to_accrue** | **float** | The maximum number of hours that can be accrued for the leave | [optional] 
**opening_balance** | **float** | The initial number of hours assigned when the leave was added to the employee | [optional] 
**rate_accrued_hourly** | **float** | The number of hours added to the leave balance for every hour worked by the employee. This is normally 0, unless the scheduleOfAccrual chosen is \&quot;OnHourWorked\&quot; | [optional] 
**schedule_of_accrual_date** | **date** | The date when an employee becomes entitled to their accrual. Only applicable when scheduleOfAccrual is \&quot;OnAnniversaryDate\&quot; | [optional] 

## Example

```python
from xero_python.models.employee_leave_type import EmployeeLeaveType

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeLeaveType from a JSON string
employee_leave_type_instance = EmployeeLeaveType.from_json(json)
# print the JSON string representation of the object
print EmployeeLeaveType.to_json()

# convert the object into a dict
employee_leave_type_dict = employee_leave_type_instance.to_dict()
# create an instance of EmployeeLeaveType from a dict
employee_leave_type_from_dict = EmployeeLeaveType.from_dict(employee_leave_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


