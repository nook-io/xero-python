# Receipt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date of receipt – YYYY-MM-DD | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**line_items** | [**List[LineItem]**](LineItem.md) |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**reference** | **str** | Additional reference number | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**sub_total** | **float** | Total of receipt excluding taxes | [optional] 
**total_tax** | **float** | Total tax on receipt | [optional] 
**total** | **float** | Total of receipt tax inclusive (i.e. SubTotal + TotalTax) | [optional] 
**receipt_id** | **str** | Xero generated unique identifier for receipt | [optional] 
**status** | **str** | Current status of receipt – see status types | [optional] 
**receipt_number** | **str** | Xero generated sequence number for receipt in current claim for a given user | [optional] [readonly] 
**updated_date_utc** | **str** | Last modified date UTC format | [optional] [readonly] 
**has_attachments** | **bool** | boolean to indicate if a receipt has an attachment | [optional] [readonly] [default to False]
**url** | **str** | URL link to a source document – shown as “Go to [appName]” in the Xero app | [optional] [readonly] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**attachments** | [**List[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 

## Example

```python
from xero_python.models.receipt import Receipt

# TODO update the JSON string below
json = "{}"
# create an instance of Receipt from a JSON string
receipt_instance = Receipt.from_json(json)
# print the JSON string representation of the object
print Receipt.to_json()

# convert the object into a dict
receipt_dict = receipt_instance.to_dict()
# create an instance of Receipt from a dict
receipt_from_dict = Receipt.from_dict(receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


