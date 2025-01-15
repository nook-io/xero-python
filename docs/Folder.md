# Folder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the folder | [optional] 
**file_count** | **int** | The number of files in the folder | [optional] 
**email** | **str** | The email address used to email files to the inbox. Only the inbox will have this element. | [optional] 
**is_inbox** | **bool** | to indicate if the folder is the Inbox. The Inbox cannot be renamed or deleted. | [optional] 
**id** | **str** | Xero unique identifier for a folder  Files | [optional] 

## Example

```python
from xero_python.models.folder import Folder

# TODO update the JSON string below
json = "{}"
# create an instance of Folder from a JSON string
folder_instance = Folder.from_json(json)
# print the JSON string representation of the object
print Folder.to_json()

# convert the object into a dict
folder_dict = folder_instance.to_dict()
# create an instance of Folder from a dict
folder_from_dict = Folder.from_dict(folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


