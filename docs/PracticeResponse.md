# PracticeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xero_partner_since** | **int** | Year of becoming a partner. | [optional] 
**tier** | **str** | Customer tier e.g. Silver | [optional] 
**location** | **str** | Country of location. | [optional] 
**organisation_count** | **int** | Organisation count. | [optional] 
**staff_certified** | **bool** | Staff certified (true/false). | [optional] 

## Example

```python
from xero_python.models.practice_response import PracticeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PracticeResponse from a JSON string
practice_response_instance = PracticeResponse.from_json(json)
# print the JSON string representation of the object
print PracticeResponse.to_json()

# convert the object into a dict
practice_response_dict = practice_response_instance.to_dict()
# create an instance of PracticeResponse from a dict
practice_response_from_dict = PracticeResponse.from_dict(practice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


