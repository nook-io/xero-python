# PnlAccountType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | Total movement on this account type | [optional] 
**title** | **str** | Name of this account type, it will be either Trading Income or Other Income for Revenue section / Direct Cost or Operating Expenses for Expense section | [optional] 
**accounts** | [**List[PnlAccount]**](PnlAccount.md) | A list of the movement on each account detail during the query period. Refer to the account detail element below | [optional] 

## Example

```python
from xero_python.models.pnl_account_type import PnlAccountType

# TODO update the JSON string below
json = "{}"
# create an instance of PnlAccountType from a JSON string
pnl_account_type_instance = PnlAccountType.from_json(json)
# print the JSON string representation of the object
print PnlAccountType.to_json()

# convert the object into a dict
pnl_account_type_dict = pnl_account_type_instance.to_dict()
# create an instance of PnlAccountType from a dict
pnl_account_type_from_dict = PnlAccountType.from_dict(pnl_account_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


