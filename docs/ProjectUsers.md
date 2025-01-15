# ProjectUsers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination2**](Pagination2.md) |  | [optional] 
**items** | [**List[ProjectUser]**](ProjectUser.md) |  | [optional] 

## Example

```python
from xero_python.models.project_users import ProjectUsers

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUsers from a JSON string
project_users_instance = ProjectUsers.from_json(json)
# print the JSON string representation of the object
print ProjectUsers.to_json()

# convert the object into a dict
project_users_dict = project_users_instance.to_dict()
# create an instance of ProjectUsers from a dict
project_users_from_dict = ProjectUsers.from_dict(project_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


