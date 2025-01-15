# TrackingCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_category_id** | **str** | The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9 | [optional] 
**tracking_option_id** | **str** | The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f | [optional] 
**name** | **str** | The name of the tracking category e.g. Department, Region (max length &#x3D; 100) | [optional] 
**option** | **str** | The option name of the tracking option e.g. East, West (max length &#x3D; 100) | [optional] 
**status** | **str** | The status of a tracking category | [optional] 
**options** | [**List[TrackingOption]**](TrackingOption.md) | See Tracking Options | [optional] 

## Example

```python
from xero_python.models.tracking_category import TrackingCategory

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingCategory from a JSON string
tracking_category_instance = TrackingCategory.from_json(json)
# print the JSON string representation of the object
print TrackingCategory.to_json()

# convert the object into a dict
tracking_category_dict = tracking_category_instance.to_dict()
# create an instance of TrackingCategory from a dict
tracking_category_from_dict = TrackingCategory.from_dict(tracking_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


