# Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Identifier of the project. | [optional] 
**contact_id** | **str** | Identifier of the contact this project was created for. | [optional] 
**name** | **str** | Name of the project. | 
**currency_code** | [**CurrencyCode1**](CurrencyCode1.md) |  | [optional] 
**minutes_logged** | **int** | A total of minutes logged against all tasks on the Project. | [optional] 
**total_task_amount** | [**Amount**](Amount.md) |  | [optional] 
**total_expense_amount** | [**Amount**](Amount.md) |  | [optional] 
**estimate_amount** | [**Amount**](Amount.md) |  | [optional] 
**minutes_to_be_invoiced** | **int** | Minutes which have not been invoiced across all chargeable tasks in the project. | [optional] 
**task_amount_to_be_invoiced** | [**Amount**](Amount.md) |  | [optional] 
**task_amount_invoiced** | [**Amount**](Amount.md) |  | [optional] 
**expense_amount_to_be_invoiced** | [**Amount**](Amount.md) |  | [optional] 
**expense_amount_invoiced** | [**Amount**](Amount.md) |  | [optional] 
**project_amount_invoiced** | [**Amount**](Amount.md) |  | [optional] 
**deposit** | [**Amount**](Amount.md) |  | [optional] 
**deposit_applied** | [**Amount**](Amount.md) |  | [optional] 
**credit_note_amount** | [**Amount**](Amount.md) |  | [optional] 
**deadline_utc** | **datetime** | Deadline for the project. UTC Date Time in ISO-8601 format. | [optional] 
**total_invoiced** | [**Amount**](Amount.md) |  | [optional] 
**total_to_be_invoiced** | [**Amount**](Amount.md) |  | [optional] 
**estimate** | [**Amount**](Amount.md) |  | [optional] 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | [optional] 

## Example

```python
from xero_python.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print Project.to_json()

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


