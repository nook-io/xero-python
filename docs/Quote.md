# Quote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** | QuoteID GUID is automatically generated and is returned after create or GET. | [optional] 
**quote_number** | **str** | Unique alpha numeric code identifying a quote (Max Length &#x3D; 255) | [optional] 
**reference** | **str** | Additional reference number | [optional] 
**terms** | **str** | Terms of the quote | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**line_items** | [**List[LineItem]**](LineItem.md) | See LineItems | [optional] 
**var_date** | **str** | Date quote was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation | [optional] 
**date_string** | **str** | Date the quote was issued (YYYY-MM-DD) | [optional] 
**expiry_date** | **str** | Date the quote expires – YYYY-MM-DD. | [optional] 
**expiry_date_string** | **str** | Date the quote expires – YYYY-MM-DD. | [optional] 
**status** | [**QuoteStatusCodes**](QuoteStatusCodes.md) |  | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**currency_rate** | **float** | The currency rate for a multicurrency quote | [optional] 
**sub_total** | **float** | Total of quote excluding taxes. | [optional] [readonly] 
**total_tax** | **float** | Total tax on quote | [optional] [readonly] 
**total** | **float** | Total of Quote tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts | [optional] [readonly] 
**total_discount** | **float** | Total of discounts applied on the quote line items | [optional] [readonly] 
**title** | **str** | Title text for the quote | [optional] 
**summary** | **str** | Summary text for the quote | [optional] 
**branding_theme_id** | **str** | See BrandingThemes | [optional] 
**updated_date_utc** | **str** | Last modified date UTC format | [optional] [readonly] 
**line_amount_types** | [**QuoteLineAmountTypes**](QuoteLineAmountTypes.md) |  | [optional] 
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

## Example

```python
from xero_python.models.quote import Quote

# TODO update the JSON string below
json = "{}"
# create an instance of Quote from a JSON string
quote_instance = Quote.from_json(json)
# print the JSON string representation of the object
print Quote.to_json()

# convert the object into a dict
quote_dict = quote_instance.to_dict()
# create an instance of Quote from a dict
quote_from_dict = Quote.from_dict(quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


