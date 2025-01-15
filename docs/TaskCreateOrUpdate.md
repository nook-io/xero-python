# TaskCreateOrUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the task. Max length 100 characters. | 
**rate** | [**Amount**](Amount.md) |  | 
**charge_type** | [**ChargeType**](ChargeType.md) |  | 
**estimate_minutes** | **int** | An estimated time to perform the task | [optional] 

## Example

```python
from xero_python.models.task_create_or_update import TaskCreateOrUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCreateOrUpdate from a JSON string
task_create_or_update_instance = TaskCreateOrUpdate.from_json(json)
# print the JSON string representation of the object
print TaskCreateOrUpdate.to_json()

# convert the object into a dict
task_create_or_update_dict = task_create_or_update_instance.to_dict()
# create an instance of TaskCreateOrUpdate from a dict
task_create_or_update_from_dict = TaskCreateOrUpdate.from_dict(task_create_or_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


