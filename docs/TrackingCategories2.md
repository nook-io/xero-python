# TrackingCategories2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**tracking_categories** | [**TrackingCategory1**](TrackingCategory1.md) |  | [optional] 

## Example

```python
from xero_python.models.tracking_categories2 import TrackingCategories2

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingCategories2 from a JSON string
tracking_categories2_instance = TrackingCategories2.from_json(json)
# print the JSON string representation of the object
print TrackingCategories2.to_json()

# convert the object into a dict
tracking_categories2_dict = tracking_categories2_instance.to_dict()
# create an instance of TrackingCategories2 from a dict
tracking_categories2_from_dict = TrackingCategories2.from_dict(tracking_categories2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


