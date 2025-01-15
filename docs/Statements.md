# Statements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination3**](Pagination3.md) |  | [optional] 
**items** | [**List[Statement]**](Statement.md) |  | [optional] 

## Example

```python
from xero_python.models.statements import Statements

# TODO update the JSON string below
json = "{}"
# create an instance of Statements from a JSON string
statements_instance = Statements.from_json(json)
# print the JSON string representation of the object
print Statements.to_json()

# convert the object into a dict
statements_dict = statements_instance.to_dict()
# create an instance of Statements from a dict
statements_from_dict = Statements.from_dict(statements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


