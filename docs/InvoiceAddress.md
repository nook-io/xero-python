# InvoiceAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_address_type** | **str** | Indicates whether the address is defined as origin (FROM) or destination (TO) | [optional] 
**address_line1** | **str** | First line of a physical address | [optional] 
**address_line2** | **str** | Second line of a physical address | [optional] 
**address_line3** | **str** | Third line of a physical address | [optional] 
**address_line4** | **str** | Fourth line of a physical address | [optional] 
**city** | **str** | City of a physical address | [optional] 
**region** | **str** | Region or state of a physical address | [optional] 
**postal_code** | **str** | Postal code of a physical address | [optional] 
**country** | **str** | Country of a physical address | [optional] 

## Example

```python
from xero_python.models.invoice_address import InvoiceAddress

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAddress from a JSON string
invoice_address_instance = InvoiceAddress.from_json(json)
# print the JSON string representation of the object
print InvoiceAddress.to_json()

# convert the object into a dict
invoice_address_dict = invoice_address_instance.to_dict()
# create an instance of InvoiceAddress from a dict
invoice_address_from_dict = InvoiceAddress.from_dict(invoice_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


