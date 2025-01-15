# LockHistoryModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard_lock_date** | **date** | Date the account hard lock was set | [optional] 
**soft_lock_date** | **date** | Date the account soft lock was set | [optional] 
**updated_date_utc** | **datetime** | The system date time that the lock was updated | [optional] 

## Example

```python
from xero_python.models.lock_history_model import LockHistoryModel

# TODO update the JSON string below
json = "{}"
# create an instance of LockHistoryModel from a JSON string
lock_history_model_instance = LockHistoryModel.from_json(json)
# print the JSON string representation of the object
print LockHistoryModel.to_json()

# convert the object into a dict
lock_history_model_dict = lock_history_model_instance.to_dict()
# create an instance of LockHistoryModel from a dict
lock_history_model_from_dict = LockHistoryModel.from_dict(lock_history_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


