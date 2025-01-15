# Problem1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ProblemType**](ProblemType.md) |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from xero_python.models.problem1 import Problem1

# TODO update the JSON string below
json = "{}"
# create an instance of Problem1 from a JSON string
problem1_instance = Problem1.from_json(json)
# print the JSON string representation of the object
print Problem1.to_json()

# convert the object into a dict
problem1_dict = problem1_instance.to_dict()
# create an instance of Problem1 from a dict
problem1_from_dict = Problem1.from_dict(problem1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


