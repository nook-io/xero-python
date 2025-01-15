# Statement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | GUID used to identify the Statement. | [optional] 
**feed_connection_id** | **str** | The Xero generated feed connection Id that identifies the Xero Bank Account Container into which the statement should be delivered. This is obtained by calling GET FeedConnections. | [optional] 
**status** | **str** | Current status of statements | [optional] 
**start_date** | **date** | Opening balance date (can be no older than one year from the current date) ISO-8601 YYYY-MM-DD | [optional] 
**end_date** | **date** | Closing balance date ISO-8601 YYYY-MM-DD | [optional] 
**start_balance** | [**StartBalance**](StartBalance.md) |  | [optional] 
**end_balance** | [**EndBalance**](EndBalance.md) |  | [optional] 
**statement_lines** | [**List[StatementLine]**](StatementLine.md) |  | [optional] 
**errors** | [**List[Error2]**](Error2.md) |  | [optional] 
**statement_line_count** | **int** |  | [optional] 

## Example

```python
from xero_python.models.statement import Statement

# TODO update the JSON string below
json = "{}"
# create an instance of Statement from a JSON string
statement_instance = Statement.from_json(json)
# print the JSON string representation of the object
print Statement.to_json()

# convert the object into a dict
statement_dict = statement_instance.to_dict()
# create an instance of Statement from a dict
statement_from_dict = Statement.from_dict(statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


