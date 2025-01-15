# Prepayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | See Prepayment Types | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**var_date** | **str** | The date the prepayment is created YYYY-MM-DD | [optional] 
**status** | **str** | See Prepayment Status Codes | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**line_items** | [**List[LineItem]**](LineItem.md) | See Prepayment Line Items | [optional] 
**sub_total** | **float** | The subtotal of the prepayment excluding taxes | [optional] 
**total_tax** | **float** | The total tax on the prepayment | [optional] 
**total** | **float** | The total of the prepayment(subtotal + total tax) | [optional] 
**reference** | **str** | Returns Invoice number field. Reference field isn&#39;t available. | [optional] [readonly] 
**updated_date_utc** | **str** | UTC timestamp of last update to the prepayment | [optional] [readonly] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**prepayment_id** | **str** | Xero generated unique identifier | [optional] 
**currency_rate** | **float** | The currency rate for a multicurrency prepayment. If no rate is specified, the XE.com day rate is used | [optional] 
**remaining_credit** | **float** | The remaining credit balance on the prepayment | [optional] 
**allocations** | [**List[Allocation]**](Allocation.md) | See Allocations | [optional] 
**payments** | [**List[Payment]**](Payment.md) | See Payments | [optional] 
**applied_amount** | **float** | The amount of applied to an invoice | [optional] 
**has_attachments** | **bool** | boolean to indicate if a prepayment has an attachment | [optional] [readonly] [default to False]
**attachments** | [**List[Attachment]**](Attachment.md) | See Attachments | [optional] 

## Example

```python
from xero_python.models.prepayment import Prepayment

# TODO update the JSON string below
json = "{}"
# create an instance of Prepayment from a JSON string
prepayment_instance = Prepayment.from_json(json)
# print the JSON string representation of the object
print Prepayment.to_json()

# convert the object into a dict
prepayment_dict = prepayment_instance.to_dict()
# create an instance of Prepayment from a dict
prepayment_from_dict = Prepayment.from_dict(prepayment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


