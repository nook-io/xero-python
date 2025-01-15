# LineItemTracking


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_category_id** | **str** | The Xero identifier for a tracking category | [optional] 
**tracking_option_id** | **str** | The Xero identifier for a tracking category option | [optional] 
**name** | **str** | The name of the tracking category | [optional] 
**option** | **str** | See Tracking Options | [optional] 

## Example

```python
from xero_python.models.line_item_tracking import LineItemTracking

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemTracking from a JSON string
line_item_tracking_instance = LineItemTracking.from_json(json)
# print the JSON string representation of the object
print LineItemTracking.to_json()

# convert the object into a dict
line_item_tracking_dict = line_item_tracking_instance.to_dict()
# create an instance of LineItemTracking from a dict
line_item_tracking_from_dict = LineItemTracking.from_dict(line_item_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


