# CashAccountResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unreconciled_amount_pos** | **float** | Total value of transactions in the journals which are not reconciled to bank statement lines, and have a positive (debit) value. | [optional] 
**unreconciled_amount_neg** | **float** | Total value of transactions in the journals which are not reconciled to bank statement lines, and have a negative (credit) value. | [optional] 
**starting_balance** | **float** | Starting (or historic) balance from the journals (manually keyed in by users on account creation - unverified). | [optional] 
**account_balance** | **float** | Current cash at bank accounting value from the journals. | [optional] 
**balance_currency** | **str** | Currency which the cashAccount transactions relate to. | [optional] 

## Example

```python
from xero_python.models.cash_account_response import CashAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashAccountResponse from a JSON string
cash_account_response_instance = CashAccountResponse.from_json(json)
# print the JSON string representation of the object
print CashAccountResponse.to_json()

# convert the object into a dict
cash_account_response_dict = cash_account_response_instance.to_dict()
# create an instance of CashAccountResponse from a dict
cash_account_response_from_dict = CashAccountResponse.from_dict(cash_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


