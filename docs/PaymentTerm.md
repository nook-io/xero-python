# PaymentTerm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bills** | [**Bill**](Bill.md) |  | [optional] 
**sales** | [**Bill**](Bill.md) |  | [optional] 

## Example

```python
from xero_python.models.payment_term import PaymentTerm

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTerm from a JSON string
payment_term_instance = PaymentTerm.from_json(json)
# print the JSON string representation of the object
print PaymentTerm.to_json()

# convert the object into a dict
payment_term_dict = payment_term_instance.to_dict()
# create an instance of PaymentTerm from a dict
payment_term_from_dict = PaymentTerm.from_dict(payment_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


