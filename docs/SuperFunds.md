# SuperFunds


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**super_funds** | [**List[SuperFund]**](SuperFund.md) |  | [optional] 

## Example

```python
from xero_python.models.super_funds import SuperFunds

# TODO update the JSON string below
json = "{}"
# create an instance of SuperFunds from a JSON string
super_funds_instance = SuperFunds.from_json(json)
# print the JSON string representation of the object
print SuperFunds.to_json()

# convert the object into a dict
super_funds_dict = super_funds_instance.to_dict()
# create an instance of SuperFunds from a dict
super_funds_from_dict = SuperFunds.from_dict(super_funds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


