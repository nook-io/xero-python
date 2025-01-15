# LineItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_id** | **str** | LineItem unique ID | [optional] 
**description** | **str** | Description needs to be at least 1 char long. A line item with just a description (i.e no unit amount or quantity) can be created by specifying just a &lt;Description&gt; element that contains at least 1 character | [optional] 
**quantity** | **float** | LineItem Quantity | [optional] 
**unit_amount** | **float** | LineItem Unit Amount | [optional] 
**item_code** | **str** | See Items | [optional] 
**account_code** | **str** | See Accounts | [optional] 
**account_id** | **str** | The associated account ID related to this line item | [optional] 
**tax_type** | **str** | The tax type from TaxRates | [optional] 
**tax_amount** | **float** | The tax amount is auto calculated as a percentage of the line amount (see below) based on the tax rate. This value can be overriden if the calculated &lt;TaxAmount&gt; is not correct. | [optional] 
**item** | [**LineItemItem**](LineItemItem.md) |  | [optional] 
**line_amount** | **float** | If you wish to omit either the Quantity or UnitAmount you can provide a LineAmount and Xero will calculate the missing amount for you. The line amount reflects the discounted price if either a DiscountRate or DiscountAmount has been used i.e. LineAmount &#x3D; Quantity * Unit Amount * ((100 - DiscountRate)/100) or LineAmount &#x3D; (Quantity * UnitAmount) - DiscountAmount | [optional] 
**tracking** | [**List[LineItemTracking]**](LineItemTracking.md) | Optional Tracking Category – see Tracking.  Any LineItem can have a  maximum of 2 &lt;TrackingCategory&gt; elements. | [optional] 
**discount_rate** | **float** | Percentage discount being applied to a line item (only supported on  ACCREC invoices – ACC PAY invoices and credit notes in Xero do not support discounts | [optional] 
**discount_amount** | **float** | Discount amount being applied to a line item. Only supported on ACCREC invoices and quotes. ACCPAY invoices and credit notes in Xero do not support discounts. | [optional] 
**repeating_invoice_id** | **str** | The Xero identifier for a Repeating Invoice | [optional] 
**taxability** | **str** | The type of taxability | [optional] 
**sales_tax_code_id** | **float** | The ID of the sales tax code | [optional] 
**tax_breakdown** | [**List[TaxBreakdownComponent]**](TaxBreakdownComponent.md) | An array of tax components defined for this line item | [optional] 

## Example

```python
from xero_python.models.line_item import LineItem

# TODO update the JSON string below
json = "{}"
# create an instance of LineItem from a JSON string
line_item_instance = LineItem.from_json(json)
# print the JSON string representation of the object
print LineItem.to_json()

# convert the object into a dict
line_item_dict = line_item_instance.to_dict()
# create an instance of LineItem from a dict
line_item_from_dict = LineItem.from_dict(line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


