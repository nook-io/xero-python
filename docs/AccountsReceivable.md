# AccountsReceivable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outstanding** | **float** |  | [optional] 
**overdue** | **float** |  | [optional] 

## Example

```python
from xero_python.models.accounts_receivable import AccountsReceivable

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsReceivable from a JSON string
accounts_receivable_instance = AccountsReceivable.from_json(json)
# print the JSON string representation of the object
print AccountsReceivable.to_json()

# convert the object into a dict
accounts_receivable_dict = accounts_receivable_instance.to_dict()
# create an instance of AccountsReceivable from a dict
accounts_receivable_from_dict = AccountsReceivable.from_dict(accounts_receivable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


