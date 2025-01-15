# EarningsOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Xero unique identifier for an earning rate | [optional] 
**name** | **str** | Name of the earning order | 
**statutory_deduction_category** | [**StatutoryDeductionCategory1**](StatutoryDeductionCategory1.md) |  | [optional] 
**liability_account_id** | **str** | Xero identifier for Liability Account | [optional] 
**current_record** | **bool** | Identifier of a record is active or not. | [optional] [default to True]

## Example

```python
from xero_python.models.earnings_order import EarningsOrder

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsOrder from a JSON string
earnings_order_instance = EarningsOrder.from_json(json)
# print the JSON string representation of the object
print EarningsOrder.to_json()

# convert the object into a dict
earnings_order_dict = earnings_order_instance.to_dict()
# create an instance of EarningsOrder from a dict
earnings_order_from_dict = EarningsOrder.from_dict(earnings_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


