# Prepayments


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination1**](Pagination1.md) |  | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**prepayments** | [**List[Prepayment]**](Prepayment.md) |  | [optional] 

## Example

```python
from xero_python.models.prepayments import Prepayments

# TODO update the JSON string below
json = "{}"
# create an instance of Prepayments from a JSON string
prepayments_instance = Prepayments.from_json(json)
# print the JSON string representation of the object
print Prepayments.to_json()

# convert the object into a dict
prepayments_dict = prepayments_instance.to_dict()
# create an instance of Prepayments from a dict
prepayments_from_dict = Prepayments.from_dict(prepayments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


