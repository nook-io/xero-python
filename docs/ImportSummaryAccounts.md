# ImportSummaryAccounts

A summary of the accounts changes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of accounts in the org | [optional] 
**new** | **int** | The number of new accounts created | [optional] 
**updated** | **int** | The number of accounts updated | [optional] 
**deleted** | **int** | The number of accounts deleted | [optional] 
**locked** | **int** | The number of locked accounts | [optional] 
**system** | **int** | The number of system accounts | [optional] 
**errored** | **int** | The number of accounts that had an error | [optional] 
**present** | **bool** |  | [optional] 
**new_or_updated** | **int** | The number of new or updated accounts | [optional] 

## Example

```python
from xero_python.models.import_summary_accounts import ImportSummaryAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of ImportSummaryAccounts from a JSON string
import_summary_accounts_instance = ImportSummaryAccounts.from_json(json)
# print the JSON string representation of the object
print ImportSummaryAccounts.to_json()

# convert the object into a dict
import_summary_accounts_dict = import_summary_accounts_instance.to_dict()
# create an instance of ImportSummaryAccounts from a dict
import_summary_accounts_from_dict = ImportSummaryAccounts.from_dict(import_summary_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


