# Files


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**items** | [**List[FileObject]**](FileObject.md) |  | [optional] 

## Example

```python
from xero_python.models.files import Files

# TODO update the JSON string below
json = "{}"
# create an instance of Files from a JSON string
files_instance = Files.from_json(json)
# print the JSON string representation of the object
print Files.to_json()

# convert the object into a dict
files_dict = files_instance.to_dict()
# create an instance of Files from a dict
files_from_dict = Files.from_dict(files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


