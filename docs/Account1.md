# Account1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The Xero identifier for Settings. | [optional] 
**type** | **str** | The assigned AccountType | [optional] 
**code** | **str** | A unique 3 digit number for each Account | [optional] 
**name** | **str** | Name of the Account. | [optional] 

## Example

```python
from xero_python.models.account1 import Account1

# TODO update the JSON string below
json = "{}"
# create an instance of Account1 from a JSON string
account1_instance = Account1.from_json(json)
# print the JSON string representation of the object
print Account1.to_json()

# convert the object into a dict
account1_dict = account1_instance.to_dict()
# create an instance of Account1 from a dict
account1_from_dict = Account1.from_dict(account1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


