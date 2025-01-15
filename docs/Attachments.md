# Attachments


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[Attachment]**](Attachment.md) |  | [optional] 

## Example

```python
from xero_python.models.attachments import Attachments

# TODO update the JSON string below
json = "{}"
# create an instance of Attachments from a JSON string
attachments_instance = Attachments.from_json(json)
# print the JSON string representation of the object
print Attachments.to_json()

# convert the object into a dict
attachments_dict = attachments_instance.to_dict()
# create an instance of Attachments from a dict
attachments_from_dict = Attachments.from_dict(attachments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


