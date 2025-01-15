# EmployeeOpeningBalancesObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**opening_balances** | [**List[EmployeeOpeningBalance]**](EmployeeOpeningBalance.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_opening_balances_object import EmployeeOpeningBalancesObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeOpeningBalancesObject from a JSON string
employee_opening_balances_object_instance = EmployeeOpeningBalancesObject.from_json(json)
# print the JSON string representation of the object
print EmployeeOpeningBalancesObject.to_json()

# convert the object into a dict
employee_opening_balances_object_dict = employee_opening_balances_object_instance.to_dict()
# create an instance of EmployeeOpeningBalancesObject from a dict
employee_opening_balances_object_from_dict = EmployeeOpeningBalancesObject.from_dict(employee_opening_balances_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


