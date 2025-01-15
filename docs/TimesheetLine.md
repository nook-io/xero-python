# TimesheetLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timesheet_line_id** | **str** | The Xero identifier for a Timesheet Line | [optional] 
**var_date** | **date** | The Date that this Timesheet Line is for (YYYY-MM-DD) | 
**earnings_rate_id** | **str** | The Xero identifier for the Earnings Rate that the Timesheet is for | 
**tracking_item_id** | **str** | The Xero identifier for the Tracking Item that the Timesheet is for | [optional] 
**number_of_units** | **float** | The Number of Units of the Timesheet Line | 

## Example

```python
from xero_python.models.timesheet_line import TimesheetLine

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetLine from a JSON string
timesheet_line_instance = TimesheetLine.from_json(json)
# print the JSON string representation of the object
print TimesheetLine.to_json()

# convert the object into a dict
timesheet_line_dict = timesheet_line_instance.to_dict()
# create an instance of TimesheetLine from a dict
timesheet_line_from_dict = TimesheetLine.from_dict(timesheet_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


