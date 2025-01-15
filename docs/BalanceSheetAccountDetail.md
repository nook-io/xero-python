# BalanceSheetAccountDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Accounting code | [optional] 
**account_id** | **str** | ID of the account | [optional] 
**name** | **str** | Account name | [optional] 
**reporting_code** | **str** | Reporting code | [optional] 
**total** | **float** | Total movement on this account | [optional] 

## Example

```python
from xero_python.models.balance_sheet_account_detail import BalanceSheetAccountDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSheetAccountDetail from a JSON string
balance_sheet_account_detail_instance = BalanceSheetAccountDetail.from_json(json)
# print the JSON string representation of the object
print BalanceSheetAccountDetail.to_json()

# convert the object into a dict
balance_sheet_account_detail_dict = balance_sheet_account_detail_instance.to_dict()
# create an instance of BalanceSheetAccountDetail from a dict
balance_sheet_account_detail_from_dict = BalanceSheetAccountDetail.from_dict(balance_sheet_account_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


