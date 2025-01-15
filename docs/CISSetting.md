# CISSetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cis_enabled** | **bool** | Boolean that describes if the contact is a CIS Subcontractor | [optional] 
**rate** | **float** | CIS Deduction rate for the contact if he is a subcontractor. If the contact is not CISEnabled, then the rate is not returned | [optional] [readonly] 

## Example

```python
from xero_python.models.cis_setting import CISSetting

# TODO update the JSON string below
json = "{}"
# create an instance of CISSetting from a JSON string
cis_setting_instance = CISSetting.from_json(json)
# print the JSON string representation of the object
print CISSetting.to_json()

# convert the object into a dict
cis_setting_dict = cis_setting_instance.to_dict()
# create an instance of CISSetting from a dict
cis_setting_from_dict = CISSetting.from_dict(cis_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


