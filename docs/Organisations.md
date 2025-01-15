# Organisations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organisations** | [**List[Organisation]**](Organisation.md) |  | [optional] 

## Example

```python
from xero_python.models.organisations import Organisations

# TODO update the JSON string below
json = "{}"
# create an instance of Organisations from a JSON string
organisations_instance = Organisations.from_json(json)
# print the JSON string representation of the object
print Organisations.to_json()

# convert the object into a dict
organisations_dict = organisations_instance.to_dict()
# create an instance of Organisations from a dict
organisations_from_dict = Organisations.from_dict(organisations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


