# BenefitObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**benefit** | [**Benefit**](Benefit.md) |  | [optional] 

## Example

```python
from xero_python.models.benefit_object import BenefitObject

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitObject from a JSON string
benefit_object_instance = BenefitObject.from_json(json)
# print the JSON string representation of the object
print BenefitObject.to_json()

# convert the object into a dict
benefit_object_dict = benefit_object_instance.to_dict()
# create an instance of BenefitObject from a dict
benefit_object_from_dict = BenefitObject.from_dict(benefit_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


