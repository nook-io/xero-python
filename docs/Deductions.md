# Deductions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**deductions** | [**List[Deduction]**](Deduction.md) |  | [optional] 

## Example

```python
from xero_python.models.deductions import Deductions

# TODO update the JSON string below
json = "{}"
# create an instance of Deductions from a JSON string
deductions_instance = Deductions.from_json(json)
# print the JSON string representation of the object
print Deductions.to_json()

# convert the object into a dict
deductions_dict = deductions_instance.to_dict()
# create an instance of Deductions from a dict
deductions_from_dict = Deductions.from_dict(deductions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


