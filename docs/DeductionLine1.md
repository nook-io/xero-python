# DeductionLine1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deduction_type_id** | **str** | Xero deduction type identifier | 
**calculation_type** | [**DeductionTypeCalculationType**](DeductionTypeCalculationType.md) |  | [optional] 
**amount** | **float** | Deduction type amount | [optional] 
**percentage** | **float** | The Percentage of the Deduction | [optional] 
**number_of_units** | **float** | Deduction number of units | [optional] 

## Example

```python
from xero_python.models.deduction_line1 import DeductionLine1

# TODO update the JSON string below
json = "{}"
# create an instance of DeductionLine1 from a JSON string
deduction_line1_instance = DeductionLine1.from_json(json)
# print the JSON string representation of the object
print DeductionLine1.to_json()

# convert the object into a dict
deduction_line1_dict = deduction_line1_instance.to_dict()
# create an instance of DeductionLine1 from a dict
deduction_line1_from_dict = DeductionLine1.from_dict(deduction_line1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


