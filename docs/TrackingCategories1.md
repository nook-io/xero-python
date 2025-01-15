# TrackingCategories1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**tracking_categories** | [**TrackingCategory1**](TrackingCategory1.md) |  | [optional] 

## Example

```python
from xero_python.models.tracking_categories1 import TrackingCategories1

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingCategories1 from a JSON string
tracking_categories1_instance = TrackingCategories1.from_json(json)
# print the JSON string representation of the object
print TrackingCategories1.to_json()

# convert the object into a dict
tracking_categories1_dict = tracking_categories1_instance.to_dict()
# create an instance of TrackingCategories1 from a dict
tracking_categories1_from_dict = TrackingCategories1.from_dict(tracking_categories1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


