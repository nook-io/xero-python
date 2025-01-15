# EarningsTemplateObject1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**earning_template** | [**EarningsTemplate**](EarningsTemplate.md) |  | [optional] 

## Example

```python
from xero_python.models.earnings_template_object1 import EarningsTemplateObject1

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsTemplateObject1 from a JSON string
earnings_template_object1_instance = EarningsTemplateObject1.from_json(json)
# print the JSON string representation of the object
print EarningsTemplateObject1.to_json()

# convert the object into a dict
earnings_template_object1_dict = earnings_template_object1_instance.to_dict()
# create an instance of EarningsTemplateObject1 from a dict
earnings_template_object1_from_dict = EarningsTemplateObject1.from_dict(earnings_template_object1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


