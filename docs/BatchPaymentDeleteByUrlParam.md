# BatchPaymentDeleteByUrlParam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the batch payment. | [default to 'DELETED']

## Example

```python
from xero_python.models.batch_payment_delete_by_url_param import BatchPaymentDeleteByUrlParam

# TODO update the JSON string below
json = "{}"
# create an instance of BatchPaymentDeleteByUrlParam from a JSON string
batch_payment_delete_by_url_param_instance = BatchPaymentDeleteByUrlParam.from_json(json)
# print the JSON string representation of the object
print BatchPaymentDeleteByUrlParam.to_json()

# convert the object into a dict
batch_payment_delete_by_url_param_dict = batch_payment_delete_by_url_param_instance.to_dict()
# create an instance of BatchPaymentDeleteByUrlParam from a dict
batch_payment_delete_by_url_param_from_dict = BatchPaymentDeleteByUrlParam.from_dict(batch_payment_delete_by_url_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


