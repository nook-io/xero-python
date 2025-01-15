# BatchPayments


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_payments** | [**List[BatchPayment]**](BatchPayment.md) |  | [optional] 

## Example

```python
from xero_python.models.batch_payments import BatchPayments

# TODO update the JSON string below
json = "{}"
# create an instance of BatchPayments from a JSON string
batch_payments_instance = BatchPayments.from_json(json)
# print the JSON string representation of the object
print BatchPayments.to_json()

# convert the object into a dict
batch_payments_dict = batch_payments_instance.to_dict()
# create an instance of BatchPayments from a dict
batch_payments_from_dict = BatchPayments.from_dict(batch_payments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


