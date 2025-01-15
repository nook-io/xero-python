# ProjectCreateOrUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | Identifier of the contact this project was created for. | [optional] 
**name** | **str** | Name of the project. | 
**estimate_amount** | **float** |  | [optional] 
**deadline_utc** | **datetime** | Deadline for the project. UTC Date Time in ISO-8601 format. | [optional] 

## Example

```python
from xero_python.models.project_create_or_update import ProjectCreateOrUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreateOrUpdate from a JSON string
project_create_or_update_instance = ProjectCreateOrUpdate.from_json(json)
# print the JSON string representation of the object
print ProjectCreateOrUpdate.to_json()

# convert the object into a dict
project_create_or_update_dict = project_create_or_update_instance.to_dict()
# create an instance of ProjectCreateOrUpdate from a dict
project_create_or_update_from_dict = ProjectCreateOrUpdate.from_dict(project_create_or_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


