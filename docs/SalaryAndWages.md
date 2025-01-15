# SalaryAndWages


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**salary_and_wages** | [**List[SalaryAndWage]**](SalaryAndWage.md) |  | [optional] 

## Example

```python
from xero_python.models.salary_and_wages import SalaryAndWages

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryAndWages from a JSON string
salary_and_wages_instance = SalaryAndWages.from_json(json)
# print the JSON string representation of the object
print SalaryAndWages.to_json()

# convert the object into a dict
salary_and_wages_dict = salary_and_wages_instance.to_dict()
# create an instance of SalaryAndWages from a dict
salary_and_wages_from_dict = SalaryAndWages.from_dict(salary_and_wages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


