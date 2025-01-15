# DeductionType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the earnings rate (max length &#x3D; 100) | [optional] 
**account_code** | **str** | See Accounts | [optional] 
**reduces_tax** | **bool** | Indicates that this is a pre-tax deduction that will reduce the amount of tax you withhold from an employee. | [optional] 
**reduces_super** | **bool** | Most deductions don’t reduce your superannuation guarantee contribution liability, so typically you will not set any value for this. | [optional] 
**is_exempt_from_w1** | **bool** | Boolean to determine if the deduction type is reportable or exempt from W1 | [optional] 
**deduction_type_id** | **str** | Xero identifier | [optional] 
**updated_date_utc** | **str** | Last modified timestamp | [optional] [readonly] 
**deduction_category** | **str** |  | [optional] 
**current_record** | **bool** | Is the current record | [optional] 

## Example

```python
from xero_python.models.deduction_type import DeductionType

# TODO update the JSON string below
json = "{}"
# create an instance of DeductionType from a JSON string
deduction_type_instance = DeductionType.from_json(json)
# print the JSON string representation of the object
print DeductionType.to_json()

# convert the object into a dict
deduction_type_dict = deduction_type_instance.to_dict()
# create an instance of DeductionType from a dict
deduction_type_from_dict = DeductionType.from_dict(deduction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


