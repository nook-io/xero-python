# SuperannuationObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**benefit** | [**Benefit1**](Benefit1.md) |  | [optional] 

## Example

```python
from xero_python.models.superannuation_object import SuperannuationObject

# TODO update the JSON string below
json = "{}"
# create an instance of SuperannuationObject from a JSON string
superannuation_object_instance = SuperannuationObject.from_json(json)
# print the JSON string representation of the object
print SuperannuationObject.to_json()

# convert the object into a dict
superannuation_object_dict = superannuation_object_instance.to_dict()
# create an instance of SuperannuationObject from a dict
superannuation_object_from_dict = SuperannuationObject.from_dict(superannuation_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


