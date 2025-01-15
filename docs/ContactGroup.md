# ContactGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the contact group. Required when creating a new contact  group | [optional] 
**status** | **str** | The Status of a contact group. To delete a contact group update the status to DELETED. Only contact groups with a status of ACTIVE are returned on GETs. | [optional] 
**contact_group_id** | **str** | The Xero identifier for an contact group – specified as a string following the endpoint name. e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9 | [optional] 
**contacts** | [**List[Contact]**](Contact.md) | The ContactID and Name of Contacts in a contact group. Returned on GETs when the ContactGroupID is supplied in the URL. | [optional] 

## Example

```python
from xero_python.models.contact_group import ContactGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ContactGroup from a JSON string
contact_group_instance = ContactGroup.from_json(json)
# print the JSON string representation of the object
print ContactGroup.to_json()

# convert the object into a dict
contact_group_dict = contact_group_instance.to_dict()
# create an instance of ContactGroup from a dict
contact_group_from_dict = ContactGroup.from_dict(contact_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


