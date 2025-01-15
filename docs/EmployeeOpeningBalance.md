# EmployeeOpeningBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_end_date** | **date** | The opening balance period end date. | [optional] 
**days_paid** | **int** | The paid number of days. | [optional] 
**unpaid_weeks** | **int** | The number of unpaid weeks. | [optional] 
**gross_earnings** | **float** | The gross earnings during the period. | [optional] 

## Example

```python
from xero_python.models.employee_opening_balance import EmployeeOpeningBalance

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeOpeningBalance from a JSON string
employee_opening_balance_instance = EmployeeOpeningBalance.from_json(json)
# print the JSON string representation of the object
print EmployeeOpeningBalance.to_json()

# convert the object into a dict
employee_opening_balance_dict = employee_opening_balance_instance.to_dict()
# create an instance of EmployeeOpeningBalance from a dict
employee_opening_balance_from_dict = EmployeeOpeningBalance.from_dict(employee_opening_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


