# ConversionBalances

Balance supplied for each account that has a value as at the conversion date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_code** | **str** | The account code for a account | [optional] 
**balance** | **float** | The opening balances of the account. Debits are positive, credits are negative values | [optional] 
**balance_details** | [**List[BalanceDetails]**](BalanceDetails.md) |  | [optional] 

## Example

```python
from xero_python.models.conversion_balances import ConversionBalances

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionBalances from a JSON string
conversion_balances_instance = ConversionBalances.from_json(json)
# print the JSON string representation of the object
print ConversionBalances.to_json()

# convert the object into a dict
conversion_balances_dict = conversion_balances_instance.to_dict()
# create an instance of ConversionBalances from a dict
conversion_balances_from_dict = ConversionBalances.from_dict(conversion_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


