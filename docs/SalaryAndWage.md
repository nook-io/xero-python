# SalaryAndWage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**salary_and_wages_id** | **str** | Xero unique identifier for a salary and wages record | [optional] 
**earnings_rate_id** | **str** | Xero unique identifier for an earnings rate | 
**number_of_units_per_week** | **float** | The Number of Units per week for the corresponding salary and wages | 
**rate_per_unit** | **float** | The rate of each unit for the corresponding salary and wages | [optional] 
**number_of_units_per_day** | **float** | The Number of Units per day for the corresponding salary and wages | [optional] 
**effective_from** | **date** | The effective date of the corresponding salary and wages | 
**annual_salary** | **float** | The annual salary | 
**status** | **str** | The current status of the corresponding salary and wages | 
**payment_type** | **str** | The type of the payment of the corresponding salary and wages | 

## Example

```python
from xero_python.models.salary_and_wage import SalaryAndWage

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryAndWage from a JSON string
salary_and_wage_instance = SalaryAndWage.from_json(json)
# print the JSON string representation of the object
print SalaryAndWage.to_json()

# convert the object into a dict
salary_and_wage_dict = salary_and_wage_instance.to_dict()
# create an instance of SalaryAndWage from a dict
salary_and_wage_from_dict = SalaryAndWage.from_dict(salary_and_wage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


