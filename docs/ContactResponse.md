# ContactResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | Xero Identifier of contact | [optional] 
**contact_name** | **str** | Full name of contact/organisation | [optional] 

## Example

```python
from xero_python.models.contact_response import ContactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactResponse from a JSON string
contact_response_instance = ContactResponse.from_json(json)
# print the JSON string representation of the object
print ContactResponse.to_json()

# convert the object into a dict
contact_response_dict = contact_response_instance.to_dict()
# create an instance of ContactResponse from a dict
contact_response_from_dict = ContactResponse.from_dict(contact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


