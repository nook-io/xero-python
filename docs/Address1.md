# Address1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | Address line 1 for employee home address | 
**address_line2** | **str** | Address line 2 for employee home address | [optional] 
**city** | **str** | Suburb for employee home address | 
**post_code** | **str** | PostCode for employee home address | 
**country_name** | **str** | Country of HomeAddress | [optional] 

## Example

```python
from xero_python.models.address1 import Address1

# TODO update the JSON string below
json = "{}"
# create an instance of Address1 from a JSON string
address1_instance = Address1.from_json(json)
# print the JSON string representation of the object
print Address1.to_json()

# convert the object into a dict
address1_dict = address1_instance.to_dict()
# create an instance of Address1 from a dict
address1_from_dict = Address1.from_dict(address1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


