# EmployeeStatutoryLeaveSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statutory_leave_id** | **str** | The unique identifier (guid) of a statutory leave. | [optional] 
**employee_id** | **str** | The unique identifier (guid) of the employee | [optional] 
**type** | **str** | The category of statutory leave | [optional] 
**start_date** | **date** | The date when the leave starts | [optional] 
**end_date** | **date** | The date when the leave ends | [optional] 
**is_entitled** | **bool** | Whether the leave was entitled to receive payment | [optional] 
**status** | **str** | The status of the leave | [optional] 

## Example

```python
from xero_python.models.employee_statutory_leave_summary import EmployeeStatutoryLeaveSummary

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeStatutoryLeaveSummary from a JSON string
employee_statutory_leave_summary_instance = EmployeeStatutoryLeaveSummary.from_json(json)
# print the JSON string representation of the object
print EmployeeStatutoryLeaveSummary.to_json()

# convert the object into a dict
employee_statutory_leave_summary_dict = employee_statutory_leave_summary_instance.to_dict()
# create an instance of EmployeeStatutoryLeaveSummary from a dict
employee_statutory_leave_summary_from_dict = EmployeeStatutoryLeaveSummary.from_dict(employee_statutory_leave_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


