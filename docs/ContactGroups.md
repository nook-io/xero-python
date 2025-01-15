# ContactGroups


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_groups** | [**List[ContactGroup]**](ContactGroup.md) |  | [optional] 

## Example

```python
from xero_python.models.contact_groups import ContactGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ContactGroups from a JSON string
contact_groups_instance = ContactGroups.from_json(json)
# print the JSON string representation of the object
print ContactGroups.to_json()

# convert the object into a dict
contact_groups_dict = contact_groups_instance.to_dict()
# create an instance of ContactGroups from a dict
contact_groups_from_dict = ContactGroups.from_dict(contact_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


