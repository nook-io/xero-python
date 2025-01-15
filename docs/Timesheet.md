# Timesheet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timesheet_id** | **str** | The Xero identifier for a Timesheet | [optional] 
**payroll_calendar_id** | **str** | The Xero identifier for the Payroll Calendar that the Timesheet applies to | 
**employee_id** | **str** | The Xero identifier for the Employee that the Timesheet is for | 
**start_date** | **date** | The Start Date of the Timesheet period (YYYY-MM-DD) | 
**end_date** | **date** | The End Date of the Timesheet period (YYYY-MM-DD) | 
**status** | **str** | Status of the timesheet | [optional] 
**total_hours** | **float** | The Total Hours of the Timesheet | [optional] 
**updated_date_utc** | **datetime** | The UTC date time that the Timesheet was last updated | [optional] 
**timesheet_lines** | [**List[TimesheetLine]**](TimesheetLine.md) |  | [optional] 

## Example

```python
from xero_python.models.timesheet import Timesheet

# TODO update the JSON string below
json = "{}"
# create an instance of Timesheet from a JSON string
timesheet_instance = Timesheet.from_json(json)
# print the JSON string representation of the object
print Timesheet.to_json()

# convert the object into a dict
timesheet_dict = timesheet_instance.to_dict()
# create an instance of Timesheet from a dict
timesheet_from_dict = Timesheet.from_dict(timesheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


