# BalanceSheetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_date** | **date** | Balance date of the report | [optional] 
**asset** | [**BalanceSheetAccountGroup**](BalanceSheetAccountGroup.md) |  | [optional] 
**liability** | [**BalanceSheetAccountGroup**](BalanceSheetAccountGroup.md) |  | [optional] 
**equity** | [**BalanceSheetAccountGroup**](BalanceSheetAccountGroup.md) |  | [optional] 

## Example

```python
from xero_python.models.balance_sheet_response import BalanceSheetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSheetResponse from a JSON string
balance_sheet_response_instance = BalanceSheetResponse.from_json(json)
# print the JSON string representation of the object
print BalanceSheetResponse.to_json()

# convert the object into a dict
balance_sheet_response_dict = balance_sheet_response_instance.to_dict()
# create an instance of BalanceSheetResponse from a dict
balance_sheet_response_from_dict = BalanceSheetResponse.from_dict(balance_sheet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


