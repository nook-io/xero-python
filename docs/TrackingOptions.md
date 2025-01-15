# TrackingOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**List[TrackingOption]**](TrackingOption.md) |  | [optional] 

## Example

```python
from xero_python.models.tracking_options import TrackingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingOptions from a JSON string
tracking_options_instance = TrackingOptions.from_json(json)
# print the JSON string representation of the object
print TrackingOptions.to_json()

# convert the object into a dict
tracking_options_dict = tracking_options_instance.to_dict()
# create an instance of TrackingOptions from a dict
tracking_options_from_dict = TrackingOptions.from_dict(tracking_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


