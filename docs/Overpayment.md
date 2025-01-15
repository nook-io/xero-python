# Overpayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | See Overpayment Types | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**var_date** | **str** | The date the overpayment is created YYYY-MM-DD | [optional] 
**status** | **str** | See Overpayment Status Codes | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**line_items** | [**List[LineItem]**](LineItem.md) | See Overpayment Line Items | [optional] 
**sub_total** | **float** | The subtotal of the overpayment excluding taxes | [optional] 
**total_tax** | **float** | The total tax on the overpayment | [optional] 
**total** | **float** | The total of the overpayment (subtotal + total tax) | [optional] 
**updated_date_utc** | **str** | UTC timestamp of last update to the overpayment | [optional] [readonly] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**overpayment_id** | **str** | Xero generated unique identifier | [optional] 
**currency_rate** | **float** | The currency rate for a multicurrency overpayment. If no rate is specified, the XE.com day rate is used | [optional] 
**remaining_credit** | **float** | The remaining credit balance on the overpayment | [optional] 
**allocations** | [**List[Allocation]**](Allocation.md) | See Allocations | [optional] 
**applied_amount** | **float** | The amount of applied to an invoice | [optional] 
**payments** | [**List[Payment]**](Payment.md) | See Payments | [optional] 
**has_attachments** | **bool** | boolean to indicate if a overpayment has an attachment | [optional] [readonly] [default to False]
**attachments** | [**List[Attachment]**](Attachment.md) | See Attachments | [optional] 

## Example

```python
from xero_python.models.overpayment import Overpayment

# TODO update the JSON string below
json = "{}"
# create an instance of Overpayment from a JSON string
overpayment_instance = Overpayment.from_json(json)
# print the JSON string representation of the object
print Overpayment.to_json()

# convert the object into a dict
overpayment_dict = overpayment_instance.to_dict()
# create an instance of Overpayment from a dict
overpayment_from_dict = Overpayment.from_dict(overpayment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


