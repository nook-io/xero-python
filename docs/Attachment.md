# Attachment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_id** | **str** | Unique ID for the file | [optional] 
**file_name** | **str** | Name of the file | [optional] 
**url** | **str** | URL to the file on xero.com | [optional] 
**mime_type** | **str** | Type of file | [optional] 
**content_length** | **int** | Length of the file content | [optional] 
**include_online** | **bool** | Include the file with the online invoice | [optional] 

## Example

```python
from xero_python.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print Attachment.to_json()

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_from_dict = Attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


