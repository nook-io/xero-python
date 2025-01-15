# TrackingCategories


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_categories** | [**List[TrackingCategory]**](TrackingCategory.md) |  | [optional] 

## Example

```python
from xero_python.models.tracking_categories import TrackingCategories

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingCategories from a JSON string
tracking_categories_instance = TrackingCategories.from_json(json)
# print the JSON string representation of the object
print TrackingCategories.to_json()

# convert the object into a dict
tracking_categories_dict = tracking_categories_instance.to_dict()
# create an instance of TrackingCategories from a dict
tracking_categories_from_dict = TrackingCategories.from_dict(tracking_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


