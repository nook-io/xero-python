# Payslips


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payslips** | [**List[Payslip1]**](Payslip1.md) |  | [optional] 

## Example

```python
from xero_python.models.payslips import Payslips

# TODO update the JSON string below
json = "{}"
# create an instance of Payslips from a JSON string
payslips_instance = Payslips.from_json(json)
# print the JSON string representation of the object
print Payslips.to_json()

# convert the object into a dict
payslips_dict = payslips_instance.to_dict()
# create an instance of Payslips from a dict
payslips_from_dict = Payslips.from_dict(payslips_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


