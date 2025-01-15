# ContactPerson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of person | [optional] 
**last_name** | **str** | Last name of person | [optional] 
**email_address** | **str** | Email address of person | [optional] 
**include_in_emails** | **bool** | boolean to indicate whether contact should be included on emails with invoices etc. | [optional] 

## Example

```python
from xero_python.models.contact_person import ContactPerson

# TODO update the JSON string below
json = "{}"
# create an instance of ContactPerson from a JSON string
contact_person_instance = ContactPerson.from_json(json)
# print the JSON string representation of the object
print ContactPerson.to_json()

# convert the object into a dict
contact_person_dict = contact_person_instance.to_dict()
# create an instance of ContactPerson from a dict
contact_person_from_dict = ContactPerson.from_dict(contact_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


