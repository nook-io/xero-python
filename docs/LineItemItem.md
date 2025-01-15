# LineItemItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | User defined item code (max length &#x3D; 30) | [optional] 
**name** | **str** | The name of the item (max length &#x3D; 50) | [optional] 
**item_id** | **str** | The Xero identifier for an Item | [optional] 

## Example

```python
from xero_python.models.line_item_item import LineItemItem

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemItem from a JSON string
line_item_item_instance = LineItemItem.from_json(json)
# print the JSON string representation of the object
print LineItemItem.to_json()

# convert the object into a dict
line_item_item_dict = line_item_item_instance.to_dict()
# create an instance of LineItemItem from a dict
line_item_item_from_dict = LineItemItem.from_dict(line_item_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


