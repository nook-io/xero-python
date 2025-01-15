# PaymentMethodObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from xero_python.models.payment_method_object import PaymentMethodObject

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodObject from a JSON string
payment_method_object_instance = PaymentMethodObject.from_json(json)
# print the JSON string representation of the object
print PaymentMethodObject.to_json()

# convert the object into a dict
payment_method_object_dict = payment_method_object_instance.to_dict()
# create an instance of PaymentMethodObject from a dict
payment_method_object_from_dict = PaymentMethodObject.from_dict(payment_method_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


