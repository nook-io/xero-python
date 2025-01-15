# OnlineInvoices


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**online_invoices** | [**List[OnlineInvoice]**](OnlineInvoice.md) |  | [optional] 

## Example

```python
from xero_python.models.online_invoices import OnlineInvoices

# TODO update the JSON string below
json = "{}"
# create an instance of OnlineInvoices from a JSON string
online_invoices_instance = OnlineInvoices.from_json(json)
# print the JSON string representation of the object
print OnlineInvoices.to_json()

# convert the object into a dict
online_invoices_dict = online_invoices_instance.to_dict()
# create an instance of OnlineInvoices from a dict
online_invoices_from_dict = OnlineInvoices.from_dict(online_invoices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


