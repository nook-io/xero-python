# Employee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | Xero unique identifier for the employee | [optional] 
**title** | **str** | Title of the employee | 
**first_name** | **str** | First name of employee | 
**last_name** | **str** | Last name of employee | 
**date_of_birth** | **date** | Date of birth of the employee (YYYY-MM-DD) | 
**address** | [**Address1**](Address1.md) |  | 
**email** | **str** | The email address for the employee | [optional] 
**gender** | **str** | The employee’s gender | 
**phone_number** | **str** | Employee phone number | [optional] 
**start_date** | **date** | Employment start date of the employee at the time it was requested | [optional] 
**end_date** | **date** | Employment end date of the employee at the time it was requested | [optional] 
**payroll_calendar_id** | **str** | Xero unique identifier for the payroll calendar of the employee | [optional] 
**updated_date_utc** | **datetime** | UTC timestamp of last update to the employee | [optional] 
**created_date_utc** | **datetime** | UTC timestamp when the employee was created in Xero | [optional] 
**national_insurance_number** | **str** | National insurance number of the employee | [optional] 
**is_off_payroll_worker** | **bool** | Whether the employee is an off payroll worker | [optional] 

## Example

```python
from xero_python.models.employee import Employee

# TODO update the JSON string below
json = "{}"
# create an instance of Employee from a JSON string
employee_instance = Employee.from_json(json)
# print the JSON string representation of the object
print Employee.to_json()

# convert the object into a dict
employee_dict = employee_instance.to_dict()
# create an instance of Employee from a dict
employee_from_dict = Employee.from_dict(employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


