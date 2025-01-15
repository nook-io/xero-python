# EmploymentObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**employment** | [**Employment**](Employment.md) |  | [optional] 

## Example

```python
from xero_python.models.employment_object import EmploymentObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmploymentObject from a JSON string
employment_object_instance = EmploymentObject.from_json(json)
# print the JSON string representation of the object
print EmploymentObject.to_json()

# convert the object into a dict
employment_object_dict = employment_object_instance.to_dict()
# create an instance of EmploymentObject from a dict
employment_object_from_dict = EmploymentObject.from_dict(employment_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


