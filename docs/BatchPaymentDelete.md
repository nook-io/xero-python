# BatchPaymentDelete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_payment_id** | **str** | The Xero generated unique identifier for the bank transaction (read-only) | 
**status** | **str** | The status of the batch payment. | [default to 'DELETED']

## Example

```python
from xero_python.models.batch_payment_delete import BatchPaymentDelete

# TODO update the JSON string below
json = "{}"
# create an instance of BatchPaymentDelete from a JSON string
batch_payment_delete_instance = BatchPaymentDelete.from_json(json)
# print the JSON string representation of the object
print BatchPaymentDelete.to_json()

# convert the object into a dict
batch_payment_delete_dict = batch_payment_delete_instance.to_dict()
# create an instance of BatchPaymentDelete from a dict
batch_payment_delete_from_dict = BatchPaymentDelete.from_dict(batch_payment_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


