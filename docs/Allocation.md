# Allocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_id** | **str** | Xero generated unique identifier | [optional] 
**invoice** | [**Invoice**](Invoice.md) |  | 
**overpayment** | [**Overpayment**](Overpayment.md) |  | [optional] 
**prepayment** | [**Prepayment**](Prepayment.md) |  | [optional] 
**credit_note** | [**CreditNote**](CreditNote.md) |  | [optional] 
**amount** | **float** | the amount being applied to the invoice | 
**var_date** | **str** | the date the allocation is applied YYYY-MM-DD. | 
**is_deleted** | **bool** | A flag that returns true when the allocation is succesfully deleted | [optional] [readonly] 
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

## Example

```python
from xero_python.models.allocation import Allocation

# TODO update the JSON string below
json = "{}"
# create an instance of Allocation from a JSON string
allocation_instance = Allocation.from_json(json)
# print the JSON string representation of the object
print Allocation.to_json()

# convert the object into a dict
allocation_dict = allocation_instance.to_dict()
# create an instance of Allocation from a dict
allocation_from_dict = Allocation.from_dict(allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


