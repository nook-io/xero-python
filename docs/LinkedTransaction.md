# LinkedTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_transaction_id** | **str** | Filter by the SourceTransactionID. Get all the linked transactions created from a particular ACCPAY invoice | [optional] 
**source_line_item_id** | **str** | The line item identifier from the source transaction. | [optional] 
**contact_id** | **str** | Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID&#x3D;4bb34b03-3378-4bb2-a0ed-6345abf3224e&amp;Status&#x3D;APPROVED. | [optional] 
**target_transaction_id** | **str** | Filter by the TargetTransactionID. Get all the linked transactions  allocated to a particular ACCREC invoice | [optional] 
**target_line_item_id** | **str** | The line item identifier from the target transaction. It is possible  to link multiple billable expenses to the same TargetLineItemID. | [optional] 
**linked_transaction_id** | **str** | The Xero identifier for an Linked Transaction e.g./LinkedTransactions/297c2dc5-cc47-4afd-8ec8-74990b8761e9 | [optional] 
**status** | **str** | Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID&#x3D;4bb34b03-3378-4bb2-a0ed-6345abf3224e&amp;Status&#x3D;APPROVED. | [optional] 
**type** | **str** | This will always be BILLABLEEXPENSE. More types may be added in future. | [optional] 
**updated_date_utc** | **str** | The last modified date in UTC format | [optional] [readonly] 
**source_transaction_type_code** | **str** | The Type of the source tranasction. This will be ACCPAY if the linked transaction was created from an invoice and SPEND if it was created from a bank transaction. | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

## Example

```python
from xero_python.models.linked_transaction import LinkedTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedTransaction from a JSON string
linked_transaction_instance = LinkedTransaction.from_json(json)
# print the JSON string representation of the object
print LinkedTransaction.to_json()

# convert the object into a dict
linked_transaction_dict = linked_transaction_instance.to_dict()
# create an instance of LinkedTransaction from a dict
linked_transaction_from_dict = LinkedTransaction.from_dict(linked_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


