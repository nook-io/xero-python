# BenefitLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefit_type_id** | **str** | Xero identifier for payroll benefit type | [optional] 
**display_name** | **str** | Benefit display name | [optional] 
**amount** | **float** | The amount of the benefit line. | [optional] 
**fixed_amount** | **float** | Benefit fixed amount | [optional] 
**percentage** | **float** | Benefit rate percentage | [optional] 

## Example

```python
from xero_python.models.benefit_line import BenefitLine

# TODO update the JSON string below
json = "{}"
# create an instance of BenefitLine from a JSON string
benefit_line_instance = BenefitLine.from_json(json)
# print the JSON string representation of the object
print BenefitLine.to_json()

# convert the object into a dict
benefit_line_dict = benefit_line_instance.to_dict()
# create an instance of BenefitLine from a dict
benefit_line_from_dict = BenefitLine.from_dict(benefit_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


