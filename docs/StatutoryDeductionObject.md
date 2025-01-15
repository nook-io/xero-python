# StatutoryDeductionObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**statutory_deduction** | [**StatutoryDeduction**](StatutoryDeduction.md) |  | [optional] 

## Example

```python
from xero_python.models.statutory_deduction_object import StatutoryDeductionObject

# TODO update the JSON string below
json = "{}"
# create an instance of StatutoryDeductionObject from a JSON string
statutory_deduction_object_instance = StatutoryDeductionObject.from_json(json)
# print the JSON string representation of the object
print StatutoryDeductionObject.to_json()

# convert the object into a dict
statutory_deduction_object_dict = statutory_deduction_object_instance.to_dict()
# create an instance of StatutoryDeductionObject from a dict
statutory_deduction_object_from_dict = StatutoryDeductionObject.from_dict(statutory_deduction_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


