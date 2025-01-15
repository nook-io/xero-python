# LeaveApplication


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leave_application_id** | **str** | The Xero identifier for Payroll Employee | [optional] 
**employee_id** | **str** | The Xero identifier for Payroll Employee | [optional] 
**leave_type_id** | **str** | The Xero identifier for Leave Type | [optional] 
**title** | **str** | The title of the leave | [optional] 
**start_date** | **str** | Start date of the leave (YYYY-MM-DD) | [optional] 
**end_date** | **str** | End date of the leave (YYYY-MM-DD) | [optional] 
**description** | **str** | The Description of the Leave | [optional] 
**pay_out_type** | [**PayOutType**](PayOutType.md) |  | [optional] 
**leave_periods** | [**List[LeavePeriod]**](LeavePeriod.md) |  | [optional] 
**updated_date_utc** | **str** | Last modified timestamp | [optional] [readonly] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

## Example

```python
from xero_python.models.leave_application import LeaveApplication

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveApplication from a JSON string
leave_application_instance = LeaveApplication.from_json(json)
# print the JSON string representation of the object
print LeaveApplication.to_json()

# convert the object into a dict
leave_application_dict = leave_application_instance.to_dict()
# create an instance of LeaveApplication from a dict
leave_application_from_dict = LeaveApplication.from_dict(leave_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


