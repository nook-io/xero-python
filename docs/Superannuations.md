# Superannuations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**benefits** | [**List[Benefit1]**](Benefit1.md) |  | [optional] 

## Example

```python
from xero_python.models.superannuations import Superannuations

# TODO update the JSON string below
json = "{}"
# create an instance of Superannuations from a JSON string
superannuations_instance = Superannuations.from_json(json)
# print the JSON string representation of the object
print Superannuations.to_json()

# convert the object into a dict
superannuations_dict = superannuations_instance.to_dict()
# create an instance of Superannuations from a dict
superannuations_from_dict = Superannuations.from_dict(superannuations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


