# EarningsRate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earnings_rate_id** | **str** | Xero unique identifier for an earning rate | [optional] 
**name** | **str** | Name of the earning rate | 
**earnings_type** | **str** | Indicates how an employee will be paid when taking this type of earning | 
**rate_type** | **str** | Indicates the type of the earning rate | 
**type_of_units** | **str** | The type of units used to record earnings | 
**current_record** | **bool** | Indicates whether an earning type is active | [optional] 
**expense_account_id** | **str** | The account that will be used for the earnings rate | 
**rate_per_unit** | **float** | Default rate per unit (optional). Only applicable if RateType is RatePerUnit | [optional] 
**multiple_of_ordinary_earnings_rate** | **float** | This is the multiplier used to calculate the rate per unit, based on the employee’s ordinary earnings rate. For example, for time and a half enter 1.5. Only applicable if RateType is MultipleOfOrdinaryEarningsRate | [optional] 
**fixed_amount** | **float** | Optional Fixed Rate Amount. Applicable for FixedAmount Rate | [optional] 

## Example

```python
from xero_python.models.earnings_rate import EarningsRate

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsRate from a JSON string
earnings_rate_instance = EarningsRate.from_json(json)
# print the JSON string representation of the object
print EarningsRate.to_json()

# convert the object into a dict
earnings_rate_dict = earnings_rate_instance.to_dict()
# create an instance of EarningsRate from a dict
earnings_rate_from_dict = EarningsRate.from_dict(earnings_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


