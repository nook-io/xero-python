# Benefits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**benefits** | [**List[Benefit]**](Benefit.md) |  | [optional] 

## Example

```python
from xero_python.models.benefits import Benefits

# TODO update the JSON string below
json = "{}"
# create an instance of Benefits from a JSON string
benefits_instance = Benefits.from_json(json)
# print the JSON string representation of the object
print Benefits.to_json()

# convert the object into a dict
benefits_dict = benefits_instance.to_dict()
# create an instance of Benefits from a dict
benefits_from_dict = Benefits.from_dict(benefits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


