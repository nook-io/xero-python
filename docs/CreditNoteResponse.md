# CreditNoteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_note_id** | **str** | Xero Identifier of credit note | [optional] 
**contact** | [**ContactResponse**](ContactResponse.md) |  | [optional] 
**total** | **float** | Total of Invoice tax inclusive (i.e. SubTotal + TotalTax); Not included in summary mode | [optional] 
**line_items** | [**List[LineItemResponse]**](LineItemResponse.md) | Not included in summary mode | [optional] 

## Example

```python
from xero_python.models.credit_note_response import CreditNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditNoteResponse from a JSON string
credit_note_response_instance = CreditNoteResponse.from_json(json)
# print the JSON string representation of the object
print CreditNoteResponse.to_json()

# convert the object into a dict
credit_note_response_dict = credit_note_response_instance.to_dict()
# create an instance of CreditNoteResponse from a dict
credit_note_response_from_dict = CreditNoteResponse.from_dict(credit_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


