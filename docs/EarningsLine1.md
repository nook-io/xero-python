# EarningsLine1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earnings_rate_id** | **str** | Xero unique id for earnings rate | 
**calculation_type** | [**EarningsRateCalculationType**](EarningsRateCalculationType.md) |  | [optional] 
**annual_salary** | **float** | Annual salary for earnings line | [optional] 
**number_of_units_per_week** | **float** | number of units for earning line | [optional] 
**rate_per_unit** | **float** | Rate per unit of the EarningsLine. | [optional] 
**normal_number_of_units** | **float** | Normal number of units for EarningsLine. Applicable when RateType is \&quot;MULTIPLE\&quot; | [optional] 
**amount** | **float** | Earnings rate amount | [optional] 
**number_of_units** | **float** | Earnings rate number of units. | [optional] 
**fixed_amount** | **float** | Earnings rate amount. Only applicable if the EarningsRate RateType is Fixed | [optional] 

## Example

```python
from xero_python.models.earnings_line1 import EarningsLine1

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsLine1 from a JSON string
earnings_line1_instance = EarningsLine1.from_json(json)
# print the JSON string representation of the object
print EarningsLine1.to_json()

# convert the object into a dict
earnings_line1_dict = earnings_line1_instance.to_dict()
# create an instance of EarningsLine1 from a dict
earnings_line1_from_dict = EarningsLine1.from_dict(earnings_line1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


