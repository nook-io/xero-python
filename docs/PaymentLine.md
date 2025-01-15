# PaymentLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_line_id** | **str** | Xero identifier for payroll payment line | [optional] 
**amount** | **float** | The amount of the payment line | [optional] 
**account_number** | **str** | The account number | [optional] 
**sort_code** | **str** | The account sort code | [optional] 
**account_name** | **str** | The account name | [optional] 

## Example

```python
from xero_python.models.payment_line import PaymentLine

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLine from a JSON string
payment_line_instance = PaymentLine.from_json(json)
# print the JSON string representation of the object
print PaymentLine.to_json()

# convert the object into a dict
payment_line_dict = payment_line_instance.to_dict()
# create an instance of PaymentLine from a dict
payment_line_from_dict = PaymentLine.from_dict(payment_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


