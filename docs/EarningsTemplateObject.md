# EarningsTemplateObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**earning_template** | [**EarningsTemplate**](EarningsTemplate.md) |  | [optional] 

## Example

```python
from xero_python.models.earnings_template_object import EarningsTemplateObject

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsTemplateObject from a JSON string
earnings_template_object_instance = EarningsTemplateObject.from_json(json)
# print the JSON string representation of the object
print EarningsTemplateObject.to_json()

# convert the object into a dict
earnings_template_object_dict = earnings_template_object_instance.to_dict()
# create an instance of EarningsTemplateObject from a dict
earnings_template_object_from_dict = EarningsTemplateObject.from_dict(earnings_template_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


