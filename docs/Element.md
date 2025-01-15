# Element


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Array of Validation Error message | [optional] 
**batch_payment_id** | **str** | Unique ID for batch payment object with validation error | [optional] 
**bank_transaction_id** | **str** |  | [optional] 
**credit_note_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**purchase_order_id** | **str** |  | [optional] 

## Example

```python
from xero_python.models.element import Element

# TODO update the JSON string below
json = "{}"
# create an instance of Element from a JSON string
element_instance = Element.from_json(json)
# print the JSON string representation of the object
print Element.to_json()

# convert the object into a dict
element_dict = element_instance.to_dict()
# create an instance of Element from a dict
element_from_dict = Element.from_dict(element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


