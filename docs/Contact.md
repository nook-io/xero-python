# Contact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | Xero identifier | [optional] 
**merged_to_contact_id** | **str** | ID for the destination of a merged contact. Only returned when using paging or when fetching a contact by ContactId or ContactNumber. | [optional] 
**contact_number** | **str** | This can be updated via the API only i.e. This field is read only on the Xero contact screen, used to identify contacts in external systems (max length &#x3D; 50). If the Contact Number is used, this is displayed as Contact Code in the Contacts UI in Xero. | [optional] 
**account_number** | **str** | A user defined account number. This can be updated via the API and the Xero UI (max length &#x3D; 50) | [optional] 
**contact_status** | **str** | Current status of a contact – see contact status types | [optional] 
**name** | **str** | Full name of contact/organisation (max length &#x3D; 255) | [optional] 
**first_name** | **str** | First name of contact person (max length &#x3D; 255) | [optional] 
**last_name** | **str** | Last name of contact person (max length &#x3D; 255) | [optional] 
**company_number** | **str** | Company registration number (max length &#x3D; 50) | [optional] 
**email_address** | **str** | Email address of contact person (umlauts not supported) (max length  &#x3D; 255) | [optional] 
**contact_persons** | [**List[ContactPerson]**](ContactPerson.md) | See contact persons | [optional] 
**bank_account_details** | **str** | Bank account number of contact | [optional] 
**tax_number** | **str** | Tax number of contact – this is also known as the ABN (Australia), GST Number (New Zealand), VAT Number (UK) or Tax ID Number (US and global) in the Xero UI depending on which regionalized version of Xero you are using (max length &#x3D; 50) | [optional] 
**accounts_receivable_tax_type** | **str** | The tax type from TaxRates | [optional] 
**accounts_payable_tax_type** | **str** | The tax type from TaxRates | [optional] 
**addresses** | [**List[Address]**](Address.md) | Store certain address types for a contact – see address types | [optional] 
**phones** | [**List[Phone]**](Phone.md) | Store certain phone types for a contact – see phone types | [optional] 
**is_supplier** | **bool** | true or false – Boolean that describes if a contact that has any AP  invoices entered against them. Cannot be set via PUT or POST – it is automatically set when an accounts payable invoice is generated against this contact. | [optional] 
**is_customer** | **bool** | true or false – Boolean that describes if a contact has any AR invoices entered against them. Cannot be set via PUT or POST – it is automatically set when an accounts receivable invoice is generated against this contact. | [optional] 
**sales_default_line_amount_type** | **str** | The default sales line amount type for a contact. Only available when summaryOnly parameter or paging is used, or when fetch by ContactId or ContactNumber. | [optional] 
**purchases_default_line_amount_type** | **str** | The default purchases line amount type for a contact Only available when summaryOnly parameter or paging is used, or when fetch by ContactId or ContactNumber. | [optional] 
**default_currency** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**xero_network_key** | **str** | Store XeroNetworkKey for contacts. | [optional] 
**sales_default_account_code** | **str** | The default sales account code for contacts | [optional] 
**purchases_default_account_code** | **str** | The default purchases account code for contacts | [optional] 
**sales_tracking_categories** | [**List[SalesTrackingCategory]**](SalesTrackingCategory.md) | The default sales tracking categories for contacts | [optional] 
**purchases_tracking_categories** | [**List[SalesTrackingCategory]**](SalesTrackingCategory.md) | The default purchases tracking categories for contacts | [optional] 
**tracking_category_name** | **str** | The name of the Tracking Category assigned to the contact under SalesTrackingCategories and PurchasesTrackingCategories | [optional] 
**tracking_category_option** | **str** | The name of the Tracking Option assigned to the contact under SalesTrackingCategories and PurchasesTrackingCategories | [optional] 
**payment_terms** | [**PaymentTerm**](PaymentTerm.md) |  | [optional] 
**updated_date_utc** | **str** | UTC timestamp of last update to contact | [optional] [readonly] 
**contact_groups** | [**List[ContactGroup]**](ContactGroup.md) | Displays which contact groups a contact is included in | [optional] 
**website** | **str** | Website address for contact (read only) | [optional] [readonly] 
**branding_theme** | [**BrandingTheme**](BrandingTheme.md) |  | [optional] 
**batch_payments** | [**BatchPaymentDetails**](BatchPaymentDetails.md) |  | [optional] 
**discount** | **float** | The default discount rate for the contact (read only) | [optional] [readonly] 
**balances** | [**Balances**](Balances.md) |  | [optional] 
**attachments** | [**List[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 
**has_attachments** | **bool** | A boolean to indicate if a contact has an attachment | [optional] [default to False]
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays validation errors returned from the API | [optional] 
**has_validation_errors** | **bool** | A boolean to indicate if a contact has an validation errors | [optional] [default to False]
**status_attribute_string** | **str** | Status of object | [optional] 

## Example

```python
from xero_python.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print Contact.to_json()

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_from_dict = Contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


