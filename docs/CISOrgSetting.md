# CISOrgSetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cis_contractor_enabled** | **bool** | true or false - Boolean that describes if the organisation is a CIS Contractor | [optional] 
**cis_sub_contractor_enabled** | **bool** | true or false - Boolean that describes if the organisation is a CIS SubContractor | [optional] 
**rate** | **float** | CIS Deduction rate for the organisation | [optional] [readonly] 

## Example

```python
from xero_python.models.cis_org_setting import CISOrgSetting

# TODO update the JSON string below
json = "{}"
# create an instance of CISOrgSetting from a JSON string
cis_org_setting_instance = CISOrgSetting.from_json(json)
# print the JSON string representation of the object
print CISOrgSetting.to_json()

# convert the object into a dict
cis_org_setting_dict = cis_org_setting_instance.to_dict()
# create an instance of CISOrgSetting from a dict
cis_org_setting_from_dict = CISOrgSetting.from_dict(cis_org_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


