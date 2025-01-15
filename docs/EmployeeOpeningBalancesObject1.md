# EmployeeOpeningBalancesObject1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**opening_balances** | [**EmployeeOpeningBalances1**](EmployeeOpeningBalances1.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_opening_balances_object1 import EmployeeOpeningBalancesObject1

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeOpeningBalancesObject1 from a JSON string
employee_opening_balances_object1_instance = EmployeeOpeningBalancesObject1.from_json(json)
# print the JSON string representation of the object
print EmployeeOpeningBalancesObject1.to_json()

# convert the object into a dict
employee_opening_balances_object1_dict = employee_opening_balances_object1_instance.to_dict()
# create an instance of EmployeeOpeningBalancesObject1 from a dict
employee_opening_balances_object1_from_dict = EmployeeOpeningBalancesObject1.from_dict(employee_opening_balances_object1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


