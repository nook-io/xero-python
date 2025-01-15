# EarningsOrderObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**statutory_deduction** | [**EarningsOrder**](EarningsOrder.md) |  | [optional] 

## Example

```python
from xero_python.models.earnings_order_object import EarningsOrderObject

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsOrderObject from a JSON string
earnings_order_object_instance = EarningsOrderObject.from_json(json)
# print the JSON string representation of the object
print EarningsOrderObject.to_json()

# convert the object into a dict
earnings_order_object_dict = earnings_order_object_instance.to_dict()
# create an instance of EarningsOrderObject from a dict
earnings_order_object_from_dict = EarningsOrderObject.from_dict(earnings_order_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


