# LeaveEarningsLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earnings_rate_id** | **str** | Xero identifier for payroll leave earnings rate | [optional] 
**rate_per_unit** | **float** | Rate per unit for leave earnings line | [optional] 
**number_of_units** | **float** | Leave earnings number of units | [optional] 
**fixed_amount** | **float** | Leave earnings fixed amount. Only applicable if the EarningsRate RateType is Fixed | [optional] 
**amount** | **float** | The amount of the earnings line. | [optional] 
**is_linked_to_timesheet** | **bool** | Identifies if the leave earnings is taken from the timesheet. False for leave earnings line | [optional] 

## Example

```python
from xero_python.models.leave_earnings_line import LeaveEarningsLine

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveEarningsLine from a JSON string
leave_earnings_line_instance = LeaveEarningsLine.from_json(json)
# print the JSON string representation of the object
print LeaveEarningsLine.to_json()

# convert the object into a dict
leave_earnings_line_dict = leave_earnings_line_instance.to_dict()
# create an instance of LeaveEarningsLine from a dict
leave_earnings_line_from_dict = LeaveEarningsLine.from_dict(leave_earnings_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


