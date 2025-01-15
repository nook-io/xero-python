# Payments


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination1**](Pagination1.md) |  | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**payments** | [**List[Payment]**](Payment.md) |  | [optional] 

## Example

```python
from xero_python.models.payments import Payments

# TODO update the JSON string below
json = "{}"
# create an instance of Payments from a JSON string
payments_instance = Payments.from_json(json)
# print the JSON string representation of the object
print Payments.to_json()

# convert the object into a dict
payments_dict = payments_instance.to_dict()
# create an instance of Payments from a dict
payments_from_dict = Payments.from_dict(payments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


