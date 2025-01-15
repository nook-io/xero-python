# DeductionObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**deduction** | [**Deduction**](Deduction.md) |  | [optional] 

## Example

```python
from xero_python.models.deduction_object import DeductionObject

# TODO update the JSON string below
json = "{}"
# create an instance of DeductionObject from a JSON string
deduction_object_instance = DeductionObject.from_json(json)
# print the JSON string representation of the object
print DeductionObject.to_json()

# convert the object into a dict
deduction_object_dict = deduction_object_instance.to_dict()
# create an instance of DeductionObject from a dict
deduction_object_from_dict = DeductionObject.from_dict(deduction_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


