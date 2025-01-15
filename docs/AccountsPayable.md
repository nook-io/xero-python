# AccountsPayable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outstanding** | **float** |  | [optional] 
**overdue** | **float** |  | [optional] 

## Example

```python
from xero_python.models.accounts_payable import AccountsPayable

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsPayable from a JSON string
accounts_payable_instance = AccountsPayable.from_json(json)
# print the JSON string representation of the object
print AccountsPayable.to_json()

# convert the object into a dict
accounts_payable_dict = accounts_payable_instance.to_dict()
# create an instance of AccountsPayable from a dict
accounts_payable_from_dict = AccountsPayable.from_dict(accounts_payable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


