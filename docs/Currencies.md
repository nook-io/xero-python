# Currencies


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencies** | [**List[Currency]**](Currency.md) |  | [optional] 

## Example

```python
from xero_python.models.currencies import Currencies

# TODO update the JSON string below
json = "{}"
# create an instance of Currencies from a JSON string
currencies_instance = Currencies.from_json(json)
# print the JSON string representation of the object
print Currencies.to_json()

# convert the object into a dict
currencies_dict = currencies_instance.to_dict()
# create an instance of Currencies from a dict
currencies_from_dict = Currencies.from_dict(currencies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


