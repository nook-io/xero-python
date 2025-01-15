# PayRuns


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**pay_runs** | [**List[PayRun]**](PayRun.md) |  | [optional] 

## Example

```python
from xero_python.models.pay_runs import PayRuns

# TODO update the JSON string below
json = "{}"
# create an instance of PayRuns from a JSON string
pay_runs_instance = PayRuns.from_json(json)
# print the JSON string representation of the object
print PayRuns.to_json()

# convert the object into a dict
pay_runs_dict = pay_runs_instance.to_dict()
# create an instance of PayRuns from a dict
pay_runs_from_dict = PayRuns.from_dict(pay_runs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


