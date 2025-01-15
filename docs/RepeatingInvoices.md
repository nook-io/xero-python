# RepeatingInvoices


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repeating_invoices** | [**List[RepeatingInvoice]**](RepeatingInvoice.md) |  | [optional] 

## Example

```python
from xero_python.models.repeating_invoices import RepeatingInvoices

# TODO update the JSON string below
json = "{}"
# create an instance of RepeatingInvoices from a JSON string
repeating_invoices_instance = RepeatingInvoices.from_json(json)
# print the JSON string representation of the object
print RepeatingInvoices.to_json()

# convert the object into a dict
repeating_invoices_dict = repeating_invoices_instance.to_dict()
# create an instance of RepeatingInvoices from a dict
repeating_invoices_from_dict = RepeatingInvoices.from_dict(repeating_invoices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


