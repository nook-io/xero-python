# Assets


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**items** | [**List[Asset]**](Asset.md) |  | [optional] 

## Example

```python
from xero_python.models.assets import Assets

# TODO update the JSON string below
json = "{}"
# create an instance of Assets from a JSON string
assets_instance = Assets.from_json(json)
# print the JSON string representation of the object
print Assets.to_json()

# convert the object into a dict
assets_dict = assets_instance.to_dict()
# create an instance of Assets from a dict
assets_from_dict = Assets.from_dict(assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


