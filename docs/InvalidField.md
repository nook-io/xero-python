# InvalidField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field that caused the error | [optional] 
**reason** | **str** | The reason the error occurred | [optional] 

## Example

```python
from xero_python.models.invalid_field import InvalidField

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidField from a JSON string
invalid_field_instance = InvalidField.from_json(json)
# print the JSON string representation of the object
print InvalidField.to_json()

# convert the object into a dict
invalid_field_dict = invalid_field_instance.to_dict()
# create an instance of InvalidField from a dict
invalid_field_from_dict = InvalidField.from_dict(invalid_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


