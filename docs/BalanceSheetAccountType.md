# BalanceSheetAccountType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** | The type of the account. See &lt;a href&#x3D;&#39;https://developer.xero.com/documentation/api/types#AccountTypes&#39;&gt;Account Types&lt;/a&gt; | [optional] 
**accounts** | [**List[BalanceSheetAccountDetail]**](BalanceSheetAccountDetail.md) | A list of all accounts of this type. Refer to the Account section below for each account element detail. | [optional] 
**total** | **float** | Total value of all the accounts in this type | [optional] 

## Example

```python
from xero_python.models.balance_sheet_account_type import BalanceSheetAccountType

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSheetAccountType from a JSON string
balance_sheet_account_type_instance = BalanceSheetAccountType.from_json(json)
# print the JSON string representation of the object
print BalanceSheetAccountType.to_json()

# convert the object into a dict
balance_sheet_account_type_dict = balance_sheet_account_type_instance.to_dict()
# create an instance of BalanceSheetAccountType from a dict
balance_sheet_account_type_from_dict = BalanceSheetAccountType.from_dict(balance_sheet_account_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


