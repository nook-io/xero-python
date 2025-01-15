# BalanceSheetAccountGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_types** | [**List[BalanceSheetAccountType]**](BalanceSheetAccountType.md) |  | [optional] 
**total** | **float** | Total value of all the accounts in this type | [optional] 

## Example

```python
from xero_python.models.balance_sheet_account_group import BalanceSheetAccountGroup

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSheetAccountGroup from a JSON string
balance_sheet_account_group_instance = BalanceSheetAccountGroup.from_json(json)
# print the JSON string representation of the object
print BalanceSheetAccountGroup.to_json()

# convert the object into a dict
balance_sheet_account_group_dict = balance_sheet_account_group_instance.to_dict()
# create an instance of BalanceSheetAccountGroup from a dict
balance_sheet_account_group_from_dict = BalanceSheetAccountGroup.from_dict(balance_sheet_account_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


