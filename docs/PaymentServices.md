# PaymentServices


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_services** | [**List[PaymentService]**](PaymentService.md) |  | [optional] 

## Example

```python
from xero_python.models.payment_services import PaymentServices

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentServices from a JSON string
payment_services_instance = PaymentServices.from_json(json)
# print the JSON string representation of the object
print PaymentServices.to_json()

# convert the object into a dict
payment_services_dict = payment_services_instance.to_dict()
# create an instance of PaymentServices from a dict
payment_services_from_dict = PaymentServices.from_dict(payment_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


