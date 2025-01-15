# FileObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | File Name | [optional] 
**mime_type** | **str** | MimeType of the file (image/png, image/jpeg, application/pdf, etc..) | [optional] 
**size** | **int** | Numeric value in bytes | [optional] 
**created_date_utc** | **str** | Created date in UTC | [optional] 
**updated_date_utc** | **str** | Updated date in UTC | [optional] 
**user** | [**User1**](User1.md) |  | [optional] 
**id** | **str** | File object&#39;s UUID | [optional] 
**folder_id** | **str** | Folder relation object&#39;s UUID | [optional] 

## Example

```python
from xero_python.models.file_object import FileObject

# TODO update the JSON string below
json = "{}"
# create an instance of FileObject from a JSON string
file_object_instance = FileObject.from_json(json)
# print the JSON string representation of the object
print FileObject.to_json()

# convert the object into a dict
file_object_dict = file_object_instance.to_dict()
# create an instance of FileObject from a dict
file_object_from_dict = FileObject.from_dict(file_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


