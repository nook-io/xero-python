# DeductionLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deduction_type_id** | **str** | Xero identifier for payroll deduction | [optional] 
**amount** | **float** | The amount of the deduction line | [optional] 
**subject_to_tax** | **bool** | Identifies if the deduction is subject to tax | [optional] 
**percentage** | **float** | Deduction rate percentage | [optional] 

## Example

```python
from xero_python.models.deduction_line import DeductionLine

# TODO update the JSON string below
json = "{}"
# create an instance of DeductionLine from a JSON string
deduction_line_instance = DeductionLine.from_json(json)
# print the JSON string representation of the object
print DeductionLine.to_json()

# convert the object into a dict
deduction_line_dict = deduction_line_instance.to_dict()
# create an instance of DeductionLine from a dict
deduction_line_from_dict = DeductionLine.from_dict(deduction_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


