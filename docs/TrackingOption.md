# TrackingOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_option_id** | **str** | The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a | [optional] 
**name** | **str** | The name of the tracking option e.g. Marketing, East (max length &#x3D; 100) | [optional] 
**status** | **str** | The status of a tracking option | [optional] 
**tracking_category_id** | **str** | Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9 | [optional] 

## Example

```python
from xero_python.models.tracking_option import TrackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingOption from a JSON string
tracking_option_instance = TrackingOption.from_json(json)
# print the JSON string representation of the object
print TrackingOption.to_json()

# convert the object into a dict
tracking_option_dict = tracking_option_instance.to_dict()
# create an instance of TrackingOption from a dict
tracking_option_from_dict = TrackingOption.from_dict(tracking_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


