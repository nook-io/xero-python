# LeaveEarningsLine1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earnings_rate_id** | **str** | Xero identifier | [optional] 
**rate_per_unit** | **float** | Rate per unit of the EarningsLine. | [optional] 
**number_of_units** | **float** | Earnings rate number of units. | [optional] 
**pay_out_type** | [**PayOutType**](PayOutType.md) |  | [optional] 

## Example

```python
from xero_python.models.leave_earnings_line1 import LeaveEarningsLine1

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveEarningsLine1 from a JSON string
leave_earnings_line1_instance = LeaveEarningsLine1.from_json(json)
# print the JSON string representation of the object
print LeaveEarningsLine1.to_json()

# convert the object into a dict
leave_earnings_line1_dict = leave_earnings_line1_instance.to_dict()
# create an instance of LeaveEarningsLine1 from a dict
leave_earnings_line1_from_dict = LeaveEarningsLine1.from_dict(leave_earnings_line1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


