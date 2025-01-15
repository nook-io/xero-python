# StatementLine

the lines details for a statement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posted_date** | **date** | The date that the transaction was processed or cleared as seen in internet banking ISO-8601 YYYY-MM-DD | [optional] 
**description** | **str** | Transaction description | [optional] 
**amount** | **float** | Transaction amount | [optional] 
**credit_debit_indicator** | [**CreditDebitIndicator**](CreditDebitIndicator.md) |  | [optional] 
**transaction_id** | **str** | Financial institute&#39;s internal transaction identifier. If provided this field is factored into duplicate detection. | [optional] 
**payee_name** | **str** | Typically the merchant or payee name | [optional] 
**reference** | **str** | Optional field to enhance the Description | [optional] 
**cheque_number** | **str** | The cheque/check number | [optional] 
**transaction_type** | **str** | Descriptive transaction type | [optional] 

## Example

```python
from xero_python.models.statement_line import StatementLine

# TODO update the JSON string below
json = "{}"
# create an instance of StatementLine from a JSON string
statement_line_instance = StatementLine.from_json(json)
# print the JSON string representation of the object
print StatementLine.to_json()

# convert the object into a dict
statement_line_dict = statement_line_instance.to_dict()
# create an instance of StatementLine from a dict
statement_line_from_dict = StatementLine.from_dict(statement_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


