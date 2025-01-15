# EmployeeStatutoryLeavesSummaries


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**statutory_leaves** | [**List[EmployeeStatutoryLeaveSummary]**](EmployeeStatutoryLeaveSummary.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_statutory_leaves_summaries import EmployeeStatutoryLeavesSummaries

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeStatutoryLeavesSummaries from a JSON string
employee_statutory_leaves_summaries_instance = EmployeeStatutoryLeavesSummaries.from_json(json)
# print the JSON string representation of the object
print EmployeeStatutoryLeavesSummaries.to_json()

# convert the object into a dict
employee_statutory_leaves_summaries_dict = employee_statutory_leaves_summaries_instance.to_dict()
# create an instance of EmployeeStatutoryLeavesSummaries from a dict
employee_statutory_leaves_summaries_from_dict = EmployeeStatutoryLeavesSummaries.from_dict(employee_statutory_leaves_summaries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


