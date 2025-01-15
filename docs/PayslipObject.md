# PayslipObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**pay_slip** | [**Payslip**](Payslip.md) |  | [optional] 

## Example

```python
from xero_python.models.payslip_object import PayslipObject

# TODO update the JSON string below
json = "{}"
# create an instance of PayslipObject from a JSON string
payslip_object_instance = PayslipObject.from_json(json)
# print the JSON string representation of the object
print PayslipObject.to_json()

# convert the object into a dict
payslip_object_dict = payslip_object_instance.to_dict()
# create an instance of PayslipObject from a dict
payslip_object_from_dict = PayslipObject.from_dict(payslip_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


