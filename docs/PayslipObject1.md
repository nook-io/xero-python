# PayslipObject1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payslip** | [**Payslip1**](Payslip1.md) |  | [optional] 

## Example

```python
from xero_python.models.payslip_object1 import PayslipObject1

# TODO update the JSON string below
json = "{}"
# create an instance of PayslipObject1 from a JSON string
payslip_object1_instance = PayslipObject1.from_json(json)
# print the JSON string representation of the object
print PayslipObject1.to_json()

# convert the object into a dict
payslip_object1_dict = payslip_object1_instance.to_dict()
# create an instance of PayslipObject1 from a dict
payslip_object1_from_dict = PayslipObject1.from_dict(payslip_object1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


