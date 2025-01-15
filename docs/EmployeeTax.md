# EmployeeTax


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starter_type** | **str** | The Starter type. | [optional] 
**starter_declaration** | **str** | Starter declaration. | [optional] 
**tax_code** | **str** | The Tax code. | [optional] 
**w1_m1** | **bool** | Describes whether the tax settings is W1M1 | [optional] 
**previous_taxable_pay** | **float** | The previous taxable pay | [optional] 
**previous_tax_paid** | **float** | The tax amount previously paid | [optional] 
**student_loan_deduction** | **str** | The employee&#39;s student loan deduction type | [optional] 
**has_post_graduate_loans** | **bool** | Describes whether the employee has post graduate loans | [optional] 
**is_director** | **bool** | Describes whether the employee is director | [optional] 
**directorship_start_date** | **date** | The directorship start date | [optional] 
**nic_calculation_method** | **str** | NICs calculation method | [optional] 

## Example

```python
from xero_python.models.employee_tax import EmployeeTax

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeTax from a JSON string
employee_tax_instance = EmployeeTax.from_json(json)
# print the JSON string representation of the object
print EmployeeTax.to_json()

# convert the object into a dict
employee_tax_dict = employee_tax_instance.to_dict()
# create an instance of EmployeeTax from a dict
employee_tax_from_dict = EmployeeTax.from_dict(employee_tax_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


