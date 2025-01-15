# TimesheetEarningsLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earnings_rate_id** | **str** | Xero identifier for payroll timesheet earnings rate | [optional] 
**rate_per_unit** | **float** | Rate per unit for timesheet earnings line | [optional] 
**number_of_units** | **float** | Timesheet earnings number of units | [optional] 
**fixed_amount** | **float** | Timesheet earnings fixed amount. Only applicable if the EarningsRate RateType is Fixed | [optional] 
**amount** | **float** | The amount of the timesheet earnings line. | [optional] 
**is_linked_to_timesheet** | **bool** | Identifies if the timesheet earnings is taken from the timesheet. False for leave earnings line | [optional] 

## Example

```python
from xero_python.models.timesheet_earnings_line import TimesheetEarningsLine

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetEarningsLine from a JSON string
timesheet_earnings_line_instance = TimesheetEarningsLine.from_json(json)
# print the JSON string representation of the object
print TimesheetEarningsLine.to_json()

# convert the object into a dict
timesheet_earnings_line_dict = timesheet_earnings_line_instance.to_dict()
# create an instance of TimesheetEarningsLine from a dict
timesheet_earnings_line_from_dict = TimesheetEarningsLine.from_dict(timesheet_earnings_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


