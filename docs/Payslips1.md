# Payslips1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**pay_slips** | [**List[Payslip]**](Payslip.md) |  | [optional] 

## Example

```python
from xero_python.models.payslips1 import Payslips1

# TODO update the JSON string below
json = "{}"
# create an instance of Payslips1 from a JSON string
payslips1_instance = Payslips1.from_json(json)
# print the JSON string representation of the object
print Payslips1.to_json()

# convert the object into a dict
payslips1_dict = payslips1_instance.to_dict()
# create an instance of Payslips1 from a dict
payslips1_from_dict = Payslips1.from_dict(payslips1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


