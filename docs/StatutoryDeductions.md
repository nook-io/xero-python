# StatutoryDeductions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**statutory_deductions** | [**List[StatutoryDeduction]**](StatutoryDeduction.md) |  | [optional] 

## Example

```python
from xero_python.models.statutory_deductions import StatutoryDeductions

# TODO update the JSON string below
json = "{}"
# create an instance of StatutoryDeductions from a JSON string
statutory_deductions_instance = StatutoryDeductions.from_json(json)
# print the JSON string representation of the object
print StatutoryDeductions.to_json()

# convert the object into a dict
statutory_deductions_dict = statutory_deductions_instance.to_dict()
# create an instance of StatutoryDeductions from a dict
statutory_deductions_from_dict = StatutoryDeductions.from_dict(statutory_deductions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


