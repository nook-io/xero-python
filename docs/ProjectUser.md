# ProjectUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Identifier of the user of the project. | [optional] 
**name** | **str** | Full name of the user. | [optional] 
**email** | **str** | Email address of the user. | [optional] 

## Example

```python
from xero_python.models.project_user import ProjectUser

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUser from a JSON string
project_user_instance = ProjectUser.from_json(json)
# print the JSON string representation of the object
print ProjectUser.to_json()

# convert the object into a dict
project_user_dict = project_user_instance.to_dict()
# create an instance of ProjectUser from a dict
project_user_from_dict = ProjectUser.from_dict(project_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


