# EarningsRateObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**earnings_rate** | [**EarningsRate**](EarningsRate.md) |  | [optional] 

## Example

```python
from xero_python.models.earnings_rate_object import EarningsRateObject

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsRateObject from a JSON string
earnings_rate_object_instance = EarningsRateObject.from_json(json)
# print the JSON string representation of the object
print EarningsRateObject.to_json()

# convert the object into a dict
earnings_rate_object_dict = earnings_rate_object_instance.to_dict()
# create an instance of EarningsRateObject from a dict
earnings_rate_object_from_dict = EarningsRateObject.from_dict(earnings_rate_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


