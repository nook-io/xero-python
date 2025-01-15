# InvoiceReminder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | setting for on or off | [optional] 

## Example

```python
from xero_python.models.invoice_reminder import InvoiceReminder

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReminder from a JSON string
invoice_reminder_instance = InvoiceReminder.from_json(json)
# print the JSON string representation of the object
print InvoiceReminder.to_json()

# convert the object into a dict
invoice_reminder_dict = invoice_reminder_instance.to_dict()
# create an instance of InvoiceReminder from a dict
invoice_reminder_from_dict = InvoiceReminder.from_dict(invoice_reminder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


