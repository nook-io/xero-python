# InvoiceReminders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_reminders** | [**List[InvoiceReminder]**](InvoiceReminder.md) |  | [optional] 

## Example

```python
from xero_python.models.invoice_reminders import InvoiceReminders

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReminders from a JSON string
invoice_reminders_instance = InvoiceReminders.from_json(json)
# print the JSON string representation of the object
print InvoiceReminders.to_json()

# convert the object into a dict
invoice_reminders_dict = invoice_reminders_instance.to_dict()
# create an instance of InvoiceReminders from a dict
invoice_reminders_from_dict = InvoiceReminders.from_dict(invoice_reminders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


