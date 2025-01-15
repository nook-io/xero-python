# LinkedTransactions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked_transactions** | [**List[LinkedTransaction]**](LinkedTransaction.md) |  | [optional] 

## Example

```python
from xero_python.models.linked_transactions import LinkedTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedTransactions from a JSON string
linked_transactions_instance = LinkedTransactions.from_json(json)
# print the JSON string representation of the object
print LinkedTransactions.to_json()

# convert the object into a dict
linked_transactions_dict = linked_transactions_instance.to_dict()
# create an instance of LinkedTransactions from a dict
linked_transactions_from_dict = LinkedTransactions.from_dict(linked_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


