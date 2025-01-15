# Phone


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_type** | **str** |  | [optional] 
**phone_number** | **str** | max length &#x3D; 50 | [optional] 
**phone_area_code** | **str** | max length &#x3D; 10 | [optional] 
**phone_country_code** | **str** | max length &#x3D; 20 | [optional] 

## Example

```python
from xero_python.models.phone import Phone

# TODO update the JSON string below
json = "{}"
# create an instance of Phone from a JSON string
phone_instance = Phone.from_json(json)
# print the JSON string representation of the object
print Phone.to_json()

# convert the object into a dict
phone_dict = phone_instance.to_dict()
# create an instance of Phone from a dict
phone_from_dict = Phone.from_dict(phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


