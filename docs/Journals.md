# Journals


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**journals** | [**List[Journal]**](Journal.md) |  | [optional] 

## Example

```python
from xero_python.models.journals import Journals

# TODO update the JSON string below
json = "{}"
# create an instance of Journals from a JSON string
journals_instance = Journals.from_json(json)
# print the JSON string representation of the object
print Journals.to_json()

# convert the object into a dict
journals_dict = journals_instance.to_dict()
# create an instance of Journals from a dict
journals_from_dict = Journals.from_dict(journals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


