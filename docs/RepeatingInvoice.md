# RepeatingInvoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | See Invoice Types | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**line_items** | [**List[LineItem]**](LineItem.md) | See LineItems | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**reference** | **str** | ACCREC only – additional reference number | [optional] 
**branding_theme_id** | **str** | See BrandingThemes | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**status** | **str** | One of the following - DRAFT or AUTHORISED – See Invoice Status Codes | [optional] 
**sub_total** | **float** | Total of invoice excluding taxes | [optional] 
**total_tax** | **float** | Total tax on invoice | [optional] 
**total** | **float** | Total of Invoice tax inclusive (i.e. SubTotal + TotalTax) | [optional] 
**repeating_invoice_id** | **str** | Xero generated unique identifier for repeating invoice template | [optional] 
**id** | **str** | Xero generated unique identifier for repeating invoice template | [optional] 
**has_attachments** | **bool** | Boolean to indicate if an invoice has an attachment | [optional] [readonly] [default to False]
**attachments** | [**List[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 
**approved_for_sending** | **bool** | Boolean to indicate whether the invoice has been approved for sending | [optional] [default to False]
**send_copy** | **bool** | Boolean to indicate whether a copy is sent to sender&#39;s email | [optional] [default to False]
**mark_as_sent** | **bool** | Boolean to indicate whether the invoice in the Xero app displays as \&quot;sent\&quot; | [optional] [default to False]
**include_pdf** | **bool** | Boolean to indicate whether to include PDF attachment | [optional] [default to False]

## Example

```python
from xero_python.models.repeating_invoice import RepeatingInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of RepeatingInvoice from a JSON string
repeating_invoice_instance = RepeatingInvoice.from_json(json)
# print the JSON string representation of the object
print RepeatingInvoice.to_json()

# convert the object into a dict
repeating_invoice_dict = repeating_invoice_instance.to_dict()
# create an instance of RepeatingInvoice from a dict
repeating_invoice_from_dict = RepeatingInvoice.from_dict(repeating_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


