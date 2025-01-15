# EmployeeOpeningBalances1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statutory_adoption_pay** | **float** | The total accumulated statutory adoption pay amount received by the employee for current fiscal year to date | [optional] 
**statutory_maternity_pay** | **float** | The total accumulated statutory maternity pay amount received by the employee for current fiscal year to date | [optional] 
**statutory_paternity_pay** | **float** | The total accumulated statutory paternity pay amount received by the employee for current fiscal year to date | [optional] 
**statutory_shared_parental_pay** | **float** | The total accumulated statutory shared parental pay amount received by the employee for current fiscal year to date | [optional] 
**statutory_sick_pay** | **float** | The total accumulated statutory sick pay amount received by the employee for current fiscal year to date | [optional] 
**prior_employee_number** | **float** | The unique employee number issued by the employee&#39;s former employer | [optional] 

## Example

```python
from xero_python.models.employee_opening_balances1 import EmployeeOpeningBalances1

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeOpeningBalances1 from a JSON string
employee_opening_balances1_instance = EmployeeOpeningBalances1.from_json(json)
# print the JSON string representation of the object
print EmployeeOpeningBalances1.to_json()

# convert the object into a dict
employee_opening_balances1_dict = employee_opening_balances1_instance.to_dict()
# create an instance of EmployeeOpeningBalances1 from a dict
employee_opening_balances1_from_dict = EmployeeOpeningBalances1.from_dict(employee_opening_balances1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


