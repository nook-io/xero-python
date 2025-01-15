# EndBalance

The StartBalance plus all the Statement Line Amounts should be equal to the EndBalance Amount.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**credit_debit_indicator** | [**CreditDebitIndicator**](CreditDebitIndicator.md) |  | [optional] 

## Example

```python
from xero_python.models.end_balance import EndBalance

# TODO update the JSON string below
json = "{}"
# create an instance of EndBalance from a JSON string
end_balance_instance = EndBalance.from_json(json)
# print the JSON string representation of the object
print EndBalance.to_json()

# convert the object into a dict
end_balance_dict = end_balance_instance.to_dict()
# create an instance of EndBalance from a dict
end_balance_from_dict = EndBalance.from_dict(end_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


