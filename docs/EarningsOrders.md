# EarningsOrders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**statutory_deductions** | [**List[EarningsOrder]**](EarningsOrder.md) |  | [optional] 

## Example

```python
from xero_python.models.earnings_orders import EarningsOrders

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsOrders from a JSON string
earnings_orders_instance = EarningsOrders.from_json(json)
# print the JSON string representation of the object
print EarningsOrders.to_json()

# convert the object into a dict
earnings_orders_dict = earnings_orders_instance.to_dict()
# create an instance of EarningsOrders from a dict
earnings_orders_from_dict = EarningsOrders.from_dict(earnings_orders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


