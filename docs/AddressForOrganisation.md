# AddressForOrganisation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_type** | **str** | define the type of address | [optional] 
**address_line1** | **str** | max length &#x3D; 500 | [optional] 
**address_line2** | **str** | max length &#x3D; 500 | [optional] 
**address_line3** | **str** | max length &#x3D; 500 | [optional] 
**address_line4** | **str** | max length &#x3D; 500 | [optional] 
**city** | **str** | max length &#x3D; 255 | [optional] 
**region** | **str** | max length &#x3D; 255 | [optional] 
**postal_code** | **str** | max length &#x3D; 50 | [optional] 
**country** | **str** | max length &#x3D; 50, [A-Z], [a-z] only | [optional] 
**attention_to** | **str** | max length &#x3D; 255 | [optional] 

## Example

```python
from xero_python.models.address_for_organisation import AddressForOrganisation

# TODO update the JSON string below
json = "{}"
# create an instance of AddressForOrganisation from a JSON string
address_for_organisation_instance = AddressForOrganisation.from_json(json)
# print the JSON string representation of the object
print AddressForOrganisation.to_json()

# convert the object into a dict
address_for_organisation_dict = address_for_organisation_instance.to_dict()
# create an instance of AddressForOrganisation from a dict
address_for_organisation_from_dict = AddressForOrganisation.from_dict(address_for_organisation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


