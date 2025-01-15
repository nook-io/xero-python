# Balances

The raw AccountsReceivable(sales invoices) and AccountsPayable(bills) outstanding and overdue amounts, not converted to base currency (read only)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts_receivable** | [**AccountsReceivable**](AccountsReceivable.md) |  | [optional] 
**accounts_payable** | [**AccountsPayable**](AccountsPayable.md) |  | [optional] 

## Example

```python
from xero_python.models.balances import Balances

# TODO update the JSON string below
json = "{}"
# create an instance of Balances from a JSON string
balances_instance = Balances.from_json(json)
# print the JSON string representation of the object
print Balances.to_json()

# convert the object into a dict
balances_dict = balances_instance.to_dict()
# create an instance of Balances from a dict
balances_from_dict = Balances.from_dict(balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


