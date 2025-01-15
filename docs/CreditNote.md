# CreditNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | See Credit Note Types | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**var_date** | **str** | The date the credit note is issued YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation | [optional] 
**due_date** | **str** | Date invoice is due – YYYY-MM-DD | [optional] 
**status** | **str** | See Credit Note Status Codes | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**line_items** | [**List[LineItem]**](LineItem.md) | See Invoice Line Items | [optional] 
**sub_total** | **float** | The subtotal of the credit note excluding taxes | [optional] 
**total_tax** | **float** | The total tax on the credit note | [optional] 
**total** | **float** | The total of the Credit Note(subtotal + total tax) | [optional] 
**cis_deduction** | **float** | CIS deduction for UK contractors | [optional] [readonly] 
**cis_rate** | **float** | CIS Deduction rate for the organisation | [optional] [readonly] 
**updated_date_utc** | **str** | UTC timestamp of last update to the credit note | [optional] [readonly] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**fully_paid_on_date** | **str** | Date when credit note was fully paid(UTC format) | [optional] 
**credit_note_id** | **str** | Xero generated unique identifier | [optional] 
**credit_note_number** | **str** | ACCRECCREDIT – Unique alpha numeric code identifying credit note (when missing will auto-generate from your Organisation Invoice Settings) | [optional] 
**reference** | **str** | ACCRECCREDIT only – additional reference number | [optional] 
**sent_to_contact** | **bool** | Boolean to set whether the credit note in the Xero app should be marked as “sent”. This can be set only on credit notes that have been approved | [optional] [readonly] 
**currency_rate** | **float** | The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used | [optional] 
**remaining_credit** | **float** | The remaining credit balance on the Credit Note | [optional] 
**allocations** | [**List[Allocation]**](Allocation.md) | See Allocations | [optional] 
**applied_amount** | **float** | The amount of applied to an invoice | [optional] 
**payments** | [**List[Payment]**](Payment.md) | See Payments | [optional] 
**branding_theme_id** | **str** | See BrandingThemes | [optional] 
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**has_attachments** | **bool** | boolean to indicate if a credit note has an attachment | [optional] [default to False]
**has_errors** | **bool** | A boolean to indicate if a credit note has an validation errors | [optional] [default to False]
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**invoice_addresses** | [**List[InvoiceAddress]**](InvoiceAddress.md) | An array of addresses used to auto calculate sales tax | [optional] 

## Example

```python
from xero_python.models.credit_note import CreditNote

# TODO update the JSON string below
json = "{}"
# create an instance of CreditNote from a JSON string
credit_note_instance = CreditNote.from_json(json)
# print the JSON string representation of the object
print CreditNote.to_json()

# convert the object into a dict
credit_note_dict = credit_note_instance.to_dict()
# create an instance of CreditNote from a dict
credit_note_from_dict = CreditNote.from_dict(credit_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


