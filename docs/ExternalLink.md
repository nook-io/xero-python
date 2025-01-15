# ExternalLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_type** | **str** | See External link types | [optional] 
**url** | **str** | URL for service e.g. http://twitter.com/xeroapi | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from xero_python.models.external_link import ExternalLink

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalLink from a JSON string
external_link_instance = ExternalLink.from_json(json)
# print the JSON string representation of the object
print ExternalLink.to_json()

# convert the object into a dict
external_link_dict = external_link_instance.to_dict()
# create an instance of ExternalLink from a dict
external_link_from_dict = ExternalLink.from_dict(external_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


