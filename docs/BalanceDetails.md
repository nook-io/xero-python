# BalanceDetails

An array to specify multiple currency balances of an account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | The opening balances of the account. Debits are positive, credits are negative values | [optional] 
**currency_code** | **str** | The currency of the balance (Not required for base currency) | [optional] 
**currency_rate** | **float** | (Optional) Exchange rate to base currency when money is spent or received. If not specified, XE rate for the day is applied | [optional] 

## Example

```python
from xero_python.models.balance_details import BalanceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceDetails from a JSON string
balance_details_instance = BalanceDetails.from_json(json)
# print the JSON string representation of the object
print BalanceDetails.to_json()

# convert the object into a dict
balance_details_dict = balance_details_instance.to_dict()
# create an instance of BalanceDetails from a dict
balance_details_from_dict = BalanceDetails.from_dict(balance_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


