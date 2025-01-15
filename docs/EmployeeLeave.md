# EmployeeLeave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leave_id** | **str** | The Xero identifier for LeaveType | [optional] 
**leave_type_id** | **str** | The Xero identifier for LeaveType | 
**description** | **str** | The description of the leave  (max length &#x3D; 50) | 
**start_date** | **date** | Start date of the leave (YYYY-MM-DD) | 
**end_date** | **date** | End date of the leave (YYYY-MM-DD) | 
**periods** | [**List[LeavePeriod1]**](LeavePeriod1.md) | The leave period information. The StartDate, EndDate and NumberOfUnits needs to be specified when you do not want to calculate NumberOfUnits automatically. Using incorrect period StartDate and EndDate will result in automatic computation of the NumberOfUnits. | [optional] 
**updated_date_utc** | **datetime** | UTC timestamp of last update to the leave type note | [optional] 

## Example

```python
from xero_python.models.employee_leave import EmployeeLeave

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeLeave from a JSON string
employee_leave_instance = EmployeeLeave.from_json(json)
# print the JSON string representation of the object
print EmployeeLeave.to_json()

# convert the object into a dict
employee_leave_dict = employee_leave_instance.to_dict()
# create an instance of EmployeeLeave from a dict
employee_leave_from_dict = EmployeeLeave.from_dict(employee_leave_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


