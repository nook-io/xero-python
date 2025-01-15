# OnlineInvoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**online_invoice_url** | **str** | the URL to an online invoice | [optional] 

## Example

```python
from xero_python.models.online_invoice import OnlineInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of OnlineInvoice from a JSON string
online_invoice_instance = OnlineInvoice.from_json(json)
# print the JSON string representation of the object
print OnlineInvoice.to_json()

# convert the object into a dict
online_invoice_dict = online_invoice_instance.to_dict()
# create an instance of OnlineInvoice from a dict
online_invoice_from_dict = OnlineInvoice.from_dict(online_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


