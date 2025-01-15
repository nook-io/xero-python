# PurchaseOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**Contact**](Contact.md) |  | [optional] 
**line_items** | [**List[LineItem]**](LineItem.md) | See LineItems | [optional] 
**var_date** | **str** | Date purchase order was issued – YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation | [optional] 
**delivery_date** | **str** | Date the goods are to be delivered – YYYY-MM-DD | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**purchase_order_number** | **str** | Unique alpha numeric code identifying purchase order (when missing will auto-generate from your Organisation Invoice Settings) | [optional] 
**reference** | **str** | Additional reference number | [optional] 
**branding_theme_id** | **str** | See BrandingThemes | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**status** | **str** | See Purchase Order Status Codes | [optional] 
**sent_to_contact** | **bool** | Boolean to set whether the purchase order should be marked as “sent”. This can be set only on purchase orders that have been approved or billed | [optional] 
**delivery_address** | **str** | The address the goods are to be delivered to | [optional] 
**attention_to** | **str** | The person that the delivery is going to | [optional] 
**telephone** | **str** | The phone number for the person accepting the delivery | [optional] 
**delivery_instructions** | **str** | A free text feild for instructions (500 characters max) | [optional] 
**expected_arrival_date** | **str** | The date the goods are expected to arrive. | [optional] 
**purchase_order_id** | **str** | Xero generated unique identifier for purchase order | [optional] 
**currency_rate** | **float** | The currency rate for a multicurrency purchase order. If no rate is specified, the XE.com day rate is used. | [optional] 
**sub_total** | **float** | Total of purchase order excluding taxes | [optional] [readonly] 
**total_tax** | **float** | Total tax on purchase order | [optional] [readonly] 
**total** | **float** | Total of Purchase Order tax inclusive (i.e. SubTotal + TotalTax) | [optional] [readonly] 
**total_discount** | **float** | Total of discounts applied on the purchase order line items | [optional] [readonly] 
**has_attachments** | **bool** | boolean to indicate if a purchase order has an attachment | [optional] [readonly] [default to False]
**updated_date_utc** | **str** | Last modified date UTC format | [optional] [readonly] 
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**attachments** | [**List[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 

## Example

```python
from xero_python.models.purchase_order import PurchaseOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrder from a JSON string
purchase_order_instance = PurchaseOrder.from_json(json)
# print the JSON string representation of the object
print PurchaseOrder.to_json()

# convert the object into a dict
purchase_order_dict = purchase_order_instance.to_dict()
# create an instance of PurchaseOrder from a dict
purchase_order_from_dict = PurchaseOrder.from_dict(purchase_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


