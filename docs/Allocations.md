# Allocations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocations** | [**List[Allocation]**](Allocation.md) |  | [optional] 

## Example

```python
from xero_python.models.allocations import Allocations

# TODO update the JSON string below
json = "{}"
# create an instance of Allocations from a JSON string
allocations_instance = Allocations.from_json(json)
# print the JSON string representation of the object
print Allocations.to_json()

# convert the object into a dict
allocations_dict = allocations_instance.to_dict()
# create an instance of Allocations from a dict
allocations_from_dict = Allocations.from_dict(allocations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


