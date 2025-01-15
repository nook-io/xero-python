# Overpayments


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination1**](Pagination1.md) |  | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**overpayments** | [**List[Overpayment]**](Overpayment.md) |  | [optional] 

## Example

```python
from xero_python.models.overpayments import Overpayments

# TODO update the JSON string below
json = "{}"
# create an instance of Overpayments from a JSON string
overpayments_instance = Overpayments.from_json(json)
# print the JSON string representation of the object
print Overpayments.to_json()

# convert the object into a dict
overpayments_dict = overpayments_instance.to_dict()
# create an instance of Overpayments from a dict
overpayments_from_dict = Overpayments.from_dict(overpayments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


