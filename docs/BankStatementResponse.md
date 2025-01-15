# BankStatementResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_lines** | [**StatementLinesResponse**](StatementLinesResponse.md) |  | [optional] 
**current_statement** | [**CurrentStatementResponse**](CurrentStatementResponse.md) |  | [optional] 

## Example

```python
from xero_python.models.bank_statement_response import BankStatementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BankStatementResponse from a JSON string
bank_statement_response_instance = BankStatementResponse.from_json(json)
# print the JSON string representation of the object
print BankStatementResponse.to_json()

# convert the object into a dict
bank_statement_response_dict = bank_statement_response_instance.to_dict()
# create an instance of BankStatementResponse from a dict
bank_statement_response_from_dict = BankStatementResponse.from_dict(bank_statement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


