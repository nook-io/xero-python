# EarningsRates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**earnings_rates** | [**List[EarningsRate]**](EarningsRate.md) |  | [optional] 

## Example

```python
from xero_python.models.earnings_rates import EarningsRates

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsRates from a JSON string
earnings_rates_instance = EarningsRates.from_json(json)
# print the JSON string representation of the object
print EarningsRates.to_json()

# convert the object into a dict
earnings_rates_dict = earnings_rates_instance.to_dict()
# create an instance of EarningsRates from a dict
earnings_rates_from_dict = EarningsRates.from_dict(earnings_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


