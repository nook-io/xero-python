# Invoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | See Invoice Types | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**line_items** | [**List[LineItem]**](LineItem.md) | See LineItems | [optional] 
**var_date** | **str** | Date invoice was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation | [optional] 
**due_date** | **str** | Date invoice is due – YYYY-MM-DD | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**invoice_number** | **str** | ACCREC – Unique alpha numeric code identifying invoice (when missing will auto-generate from your Organisation Invoice Settings) (max length &#x3D; 255) | [optional] 
**reference** | **str** | ACCREC only – additional reference number | [optional] 
**branding_theme_id** | **str** | See BrandingThemes | [optional] 
**url** | **str** | URL link to a source document – shown as “Go to [appName]” in the Xero app | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**currency_rate** | **float** | The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used. (max length &#x3D; [18].[6]) | [optional] 
**status** | **str** | See Invoice Status Codes | [optional] 
**sent_to_contact** | **bool** | Boolean to set whether the invoice in the Xero app should be marked as “sent”. This can be set only on invoices that have been approved | [optional] 
**expected_payment_date** | **str** | Shown on sales invoices (Accounts Receivable) when this has been set | [optional] 
**planned_payment_date** | **str** | Shown on bills (Accounts Payable) when this has been set | [optional] 
**cis_deduction** | **float** | CIS deduction for UK contractors | [optional] [readonly] 
**cis_rate** | **float** | CIS Deduction rate for the organisation | [optional] [readonly] 
**sub_total** | **float** | Total of invoice excluding taxes | [optional] [readonly] 
**total_tax** | **float** | Total tax on invoice | [optional] [readonly] 
**total** | **float** | Total of Invoice tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts | [optional] [readonly] 
**total_discount** | **float** | Total of discounts applied on the invoice line items | [optional] [readonly] 
**invoice_id** | **str** | Xero generated unique identifier for invoice | [optional] 
**repeating_invoice_id** | **str** | Xero generated unique identifier for repeating invoices | [optional] 
**has_attachments** | **bool** | boolean to indicate if an invoice has an attachment | [optional] [readonly] [default to False]
**is_discounted** | **bool** | boolean to indicate if an invoice has a discount | [optional] [readonly] 
**payments** | [**List[Payment]**](Payment.md) | See Payments | [optional] [readonly] 
**prepayments** | [**List[Prepayment]**](Prepayment.md) | See Prepayments | [optional] [readonly] 
**overpayments** | [**List[Overpayment]**](Overpayment.md) | See Overpayments | [optional] [readonly] 
**amount_due** | **float** | Amount remaining to be paid on invoice | [optional] [readonly] 
**amount_paid** | **float** | Sum of payments received for invoice | [optional] [readonly] 
**fully_paid_on_date** | **str** | The date the invoice was fully paid. Only returned on fully paid invoices | [optional] [readonly] 
**amount_credited** | **float** | Sum of all credit notes, over-payments and pre-payments applied to invoice | [optional] [readonly] 
**updated_date_utc** | **str** | Last modified date UTC format | [optional] [readonly] 
**credit_notes** | [**List[CreditNote]**](CreditNote.md) | Details of credit notes that have been applied to an invoice | [optional] [readonly] 
**attachments** | [**List[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 
**has_errors** | **bool** | A boolean to indicate if a invoice has an validation errors | [optional] [default to False]
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**invoice_addresses** | [**List[InvoiceAddress]**](InvoiceAddress.md) | An array of addresses used to auto calculate sales tax | [optional] 

## Example

```python
from xero_python.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print Invoice.to_json()

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_from_dict = Invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


