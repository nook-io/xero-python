# SalaryAndWageObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**salary_and_wages** | [**SalaryAndWage**](SalaryAndWage.md) |  | [optional] 

## Example

```python
from xero_python.models.salary_and_wage_object import SalaryAndWageObject

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryAndWageObject from a JSON string
salary_and_wage_object_instance = SalaryAndWageObject.from_json(json)
# print the JSON string representation of the object
print SalaryAndWageObject.to_json()

# convert the object into a dict
salary_and_wage_object_dict = salary_and_wage_object_instance.to_dict()
# create an instance of SalaryAndWageObject from a dict
salary_and_wage_object_from_dict = SalaryAndWageObject.from_dict(salary_and_wage_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


