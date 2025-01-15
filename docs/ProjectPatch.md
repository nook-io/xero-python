# ProjectPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ProjectStatus**](ProjectStatus.md) |  | 

## Example

```python
from xero_python.models.project_patch import ProjectPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPatch from a JSON string
project_patch_instance = ProjectPatch.from_json(json)
# print the JSON string representation of the object
print ProjectPatch.to_json()

# convert the object into a dict
project_patch_dict = project_patch_instance.to_dict()
# create an instance of ProjectPatch from a dict
project_patch_from_dict = ProjectPatch.from_dict(project_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


