# Actions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[Action]**](Action.md) |  | [optional] 

## Example

```python
from xero_python.models.actions import Actions

# TODO update the JSON string below
json = "{}"
# create an instance of Actions from a JSON string
actions_instance = Actions.from_json(json)
# print the JSON string representation of the object
print Actions.to_json()

# convert the object into a dict
actions_dict = actions_instance.to_dict()
# create an instance of Actions from a dict
actions_from_dict = Actions.from_dict(actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


