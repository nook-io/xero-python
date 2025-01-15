# PayRunObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**pay_run** | [**PayRun**](PayRun.md) |  | [optional] 

## Example

```python
from xero_python.models.pay_run_object import PayRunObject

# TODO update the JSON string below
json = "{}"
# create an instance of PayRunObject from a JSON string
pay_run_object_instance = PayRunObject.from_json(json)
# print the JSON string representation of the object
print PayRunObject.to_json()

# convert the object into a dict
pay_run_object_dict = pay_run_object_instance.to_dict()
# create an instance of PayRunObject from a dict
pay_run_object_from_dict = PayRunObject.from_dict(pay_run_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


