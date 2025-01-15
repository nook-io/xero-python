# EarningsTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_template_earning_id** | **str** | The Xero identifier for the earnings template | [optional] 
**rate_per_unit** | **float** | The rate per unit | [optional] 
**number_of_units** | **float** | The rate per unit | [optional] 
**fixed_amount** | **float** | The fixed amount per period | [optional] 
**earnings_rate_id** | **str** | The corresponding earnings rate identifier | [optional] 
**name** | **str** | The read-only name of the Earning Template. | [optional] 

## Example

```python
from xero_python.models.earnings_template import EarningsTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsTemplate from a JSON string
earnings_template_instance = EarningsTemplate.from_json(json)
# print the JSON string representation of the object
print EarningsTemplate.to_json()

# convert the object into a dict
earnings_template_dict = earnings_template_instance.to_dict()
# create an instance of EarningsTemplate from a dict
earnings_template_from_dict = EarningsTemplate.from_dict(earnings_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


