# PaymentDelete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the payment. | [default to 'DELETED']

## Example

```python
from xero_python.models.payment_delete import PaymentDelete

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDelete from a JSON string
payment_delete_instance = PaymentDelete.from_json(json)
# print the JSON string representation of the object
print PaymentDelete.to_json()

# convert the object into a dict
payment_delete_dict = payment_delete_instance.to_dict()
# create an instance of PaymentDelete from a dict
payment_delete_from_dict = PaymentDelete.from_dict(payment_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


