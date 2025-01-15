# Association


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_with_object** | **bool** | Boolean flag to determines whether the file is sent with the document it is attached to on client facing communications. Note- The SendWithObject element is only returned when using /Associations/{ObjectId} endpoint. | [optional] 
**name** | **str** | The name of the associated file. Note- The Name element is only returned when using /Associations/{ObjectId} endpoint. | [optional] 
**size** | **int** | The size of the associated file in bytes. Note- The Size element is only returned when using /Associations/{ObjectId} endpoint. | [optional] 
**file_id** | **str** | The unique identifier of the file | [optional] 
**object_id** | **str** | The identifier of the object that the file is being associated with (e.g. InvoiceID, BankTransactionID, ContactID) | [optional] 
**object_group** | [**ObjectGroup**](ObjectGroup.md) |  | [optional] 
**object_type** | [**ObjectType**](ObjectType.md) |  | [optional] 

## Example

```python
from xero_python.models.association import Association

# TODO update the JSON string below
json = "{}"
# create an instance of Association from a JSON string
association_instance = Association.from_json(json)
# print the JSON string representation of the object
print Association.to_json()

# convert the object into a dict
association_dict = association_instance.to_dict()
# create an instance of Association from a dict
association_from_dict = Association.from_dict(association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


