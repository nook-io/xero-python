# EarningsLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earnings_line_id** | **str** | Xero identifier for payroll earnings line | [optional] 
**earnings_rate_id** | **str** | Xero identifier for payroll earnings rate | [optional] 
**display_name** | **str** | name of earnings rate for display in UI | [optional] 
**rate_per_unit** | **float** | Rate per unit for earnings line | [optional] 
**number_of_units** | **float** | Earnings number of units | [optional] 
**fixed_amount** | **float** | Earnings fixed amount. Only applicable if the EarningsRate RateType is Fixed | [optional] 
**amount** | **float** | The amount of the earnings line. | [optional] 
**is_linked_to_timesheet** | **bool** | Identifies if the earnings is taken from the timesheet. False for earnings line | [optional] 
**is_average_daily_pay_rate** | **bool** | Identifies if the earnings is using an average daily pay rate | [optional] 

## Example

```python
from xero_python.models.earnings_line import EarningsLine

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsLine from a JSON string
earnings_line_instance = EarningsLine.from_json(json)
# print the JSON string representation of the object
print EarningsLine.to_json()

# convert the object into a dict
earnings_line_dict = earnings_line_instance.to_dict()
# create an instance of EarningsLine from a dict
earnings_line_from_dict = EarningsLine.from_dict(earnings_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


